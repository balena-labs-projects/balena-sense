# This script detects for the presence of either a BME680 sensor on the I2C bus or a Sense HAT
# The BME680 includes sensors for temperature, humidity, pressure and gas content
# The Sense HAT does not have a gas sensor, and so air quality is approximated using temperature and humidity only.

import sys
import time
import smbus
import os
import json

from hts221 import HTS221
from bme680 import BME680
from http.server import HTTPServer, BaseHTTPRequestHandler

class balenaSense():
    readfrom = 'unset'
    bus = smbus.SMBus(1)

    def __init__(self):
        # First, check to see if there is a BME680 on the I2C bus
        try:
            self.bus.write_byte(0x76, 0)
        except IOError:
            print('BME680 not found on 0x76, trying 0x77')
        else:
            self.readfrom = 'bme680primary'

        # If we didn't find it on 0x76, look on 0x77
        if self.readfrom == 'unset':
            try:
                self.bus.write_byte(0x77, 0)
            except IOError:
                print('BME680 not found on 0x77')
            else:
                self.readfrom = 'bme680secondary'


        # If no BME680, is there a Sense HAT?
        if self.readfrom == 'unset':
            try:
                self.bus.write_byte(0x5F, 0)
            except:
                print('Sense HAT not found')
            else:
                self.readfrom = 'sense-hat'
                print('Using Sense HAT for readings (no gas measurements)')

                # Import the sense hat methods
                import sense_hat_air_quality

                self.sensor = HTS221()
        else:
                print('Using BME680 for readings')

                # Import the BME680 methods
                self.sensor = BME680(self.readfrom)


        # If this is still unset, no sensors were found; quit!
        if self.readfrom == 'unset':
            print('No suitable sensors found! Exiting.')
            sys.exit()

    def sample(self):
        if self.readfrom == 'sense-hat':
            return self.apply_offsets(sense_hat_air_quality.get_readings(self.sensor))
        else:
            return self.apply_offsets(self.sensor.get_readings(self.sensor))


    def apply_offsets(self, measurements):
        # Apply any offsets to the measurements before storing them in the database
        if os.environ.get('BALENASENSE_TEMP_OFFSET') != None:
            measurements[0]['fields']['temperature'] = measurements[0]['fields']['temperature'] + float(os.environ['BALENASENSE_TEMP_OFFSET'])

        if os.environ.get('BALENASENSE_HUM_OFFSET') != None:
            measurements[0]['fields']['humidity'] = measurements[0]['fields']['humidity'] + float(os.environ['BALENASENSE_HUM_OFFSET'])

        if os.environ.get('BALENASENSE_ALTITUDE') != None:
            # if there's an altitude set (in meters), then apply a barometric pressure offset
            altitude = float(os.environ['BALENASENSE_ALTITUDE'])
            measurements[0]['fields']['pressure'] = measurements[0]['fields']['pressure'] * (1-((0.0065 * altitude) / (measurements[0]['fields']['temperature'] + (0.0065 * altitude) + 273.15))) ** -5.257

        return measurements



class balenaSenseHTTP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        measurements = balenasense.sample()
        self.wfile.write(json.dumps(measurements[0]['fields']).encode('UTF-8'))

    def do_HEAD(self):
        self._set_headers()


# Start the server to answer requests for readings
balenasense = balenaSense()

while True:
    server_address = ('', 80)
    httpd = HTTPServer(server_address, balenaSenseHTTP)
    print('Sensor HTTP server running')
    httpd.serve_forever()
