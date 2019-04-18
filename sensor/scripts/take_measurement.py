#!/usr/local/bin/python

# This script detects for the presence of either a BME680 sensor on the I2C bus or a Sense HAT
# The BME680 includes sensors for temperature, humidity, pressure and gas content
# The Sense HAT does not have a gas sensor, and so air quality is approximated using temperature and humidity only.

import sys
import bme680
import time
from sense_hat import SenseHat
from influxdb import InfluxDBClient

readfrom = 'unset'

# First, check to see if there is a BME680 on the I2C bus
try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    print 'BME680 not found on 0x76, trying 0x77'
else:
    readfrom = 'bme680'

# If we didn't find it on 0x76, look on 0x77
if readfrom == 'unset':
    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
    except IOError:
        print 'BME680 not found on 0x77'
    else:
        readfrom = 'bme680'


# If no BME680, is there a Sense HAT?
if readfrom == 'unset':
    try:
        sensor = SenseHat()
    except:
        print 'Sense HAT not found'
    else:
        readfrom = 'sense-hat'
        print 'Using Sense HAT for readings (no gas measurements)'
        # Import the sense hat methods
        import sense_hat_air_quality
        get_readings = sense_hat_air_quality.get_readings
else:
        print 'Using BME680 for readings'
        # Import the bme680 methods and nitialise the bme680 burnin
        import bme680_air_quality
        bme680_air_quality.start_bme680(sensor)
        get_readings = bme680_air_quality.get_readings

# If this is still unset, no sensors were found; quit!
if readfrom == 'unset':
    sys.exit()

# Create the database client, connected to the influxdb container, and select/create the database
influx_client = InfluxDBClient('influxdb', 8086, database='balena-sense')
influx_client.create_database('balena-sense')


while True:
    measurements = get_readings(sensor)
    influx_client.write_points(measurements)
    time.sleep(10)
