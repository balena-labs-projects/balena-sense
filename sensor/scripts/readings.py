#!/usr/local/bin/python
import time
import bme680

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

if sensor.get_sensor_data():
    timestamp  = int(round(time.time() * 1000))

    output = 'balena-sense temperature={0:.2f},pressure={1:.2f},humidity={2:.3f}'.format(
        sensor.data.temperature,
        sensor.data.pressure,
        sensor.data.humidity)

    print(output)
