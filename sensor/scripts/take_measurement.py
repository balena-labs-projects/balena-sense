# This script detects for the presence of either a BME680 sensor on the I2C bus or a Sense HAT
# The BME680 includes sensors for temperature, humidity, pressure and gas content
# The Sense HAT does not have a gas sensor, and so air quality is approximated using temperature and humidity only.

import sys
import time
import smbus
import os

from hts221 import HTS221
from bme680 import BME680
from influxdb import InfluxDBClient

readfrom = 'unset'
bus = smbus.SMBus(1)

def apply_offsets(measurements):
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

# First, check to see if there is a BME680 on the I2C bus
try:
    bus.write_byte(0x76, 0)
except IOError:
    print('BME680 not found on 0x76, trying 0x77')
else:
    readfrom = 'bme680'

# If we didn't find it on 0x76, look on 0x77
if readfrom == 'unset':
    try:
        bus.write_byte(0x77, 0)
    except IOError:
        print('BME680 not found on 0x77')
    else:
        readfrom = 'bme680'


# If no BME680, is there a Sense HAT?
if readfrom == 'unset':
    try:
        bus.write_byte(0x5F, 0)
    except:
        print('Sense HAT not found')
    else:
        readfrom = 'sense-hat'
        print('Using Sense HAT for readings (no gas measurements)')

        # Import the sense hat methods
        import sense_hat_air_quality

        sensor = HTS221()
        get_readings = sense_hat_air_quality.get_readings
else:
        print('Using BME680 for readings')

        sensor = BME680()
        get_readings = sensor.get_readings


# If this is still unset, no sensors were found; quit!
if readfrom == 'unset':
    print('No suitable sensors found! Exiting.')
    sys.exit()

# Create the database client, connected to the influxdb container, and select/create the database
influx_client = InfluxDBClient('influxdb', 8086, database='balena-sense')
influx_client.create_database('balena-sense')

# Start the main loop taking readings every 1 second and recording every 10 seconds
count = 0
while True:
    time.sleep(10)
    measurements = apply_offsets(get_readings(sensor))
    influx_client.write_points(measurements)
