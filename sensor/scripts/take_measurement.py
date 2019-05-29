# This script detects for the presence of either a BME680 sensor on the I2C bus or a Sense HAT
# The BME680 includes sensors for temperature, humidity, pressure and gas content
# The Sense HAT does not have a gas sensor, and so air quality is approximated using temperature and humidity only.

import sys
import time
import smbus

from hts221 import HTS221
from bme680 import BME680
from influxdb import InfluxDBClient

readfrom = 'unset'
bus = smbus.SMBus(1)

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
        time.sleep(5)


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
    measurements = get_readings(sensor)

    count = count + 1
    if count == 10:
        influx_client.write_points(measurements)
        count = 0

    time.sleep(1)
