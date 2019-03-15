#!/usr/local/bin/python

# Approximate air quality reading
# Adapted from: https://github.com/G6EJD/BME680-Example/blob/master/ESP32_bme680_CC_demo_02.ino#L81-L131

hum_weighting = 0.25
gas_weighting = 0.75

hum_reference = 40;

current_humidity = float(open("/sys/bus/iio/devices/iio:device0/in_humidityrelative_input").read())
gas_reference = int(open("/sys/bus/iio/devices/iio:device0/in_resistance_input").read())

if current_humidity >= 38 and current_humidity <= 42:
    hum_score = 0.25*100
else:
    if current_humidity < 38:
        hum_score = 0.25/hum_reference*current_humidity*100
    else:
        hum_score = ((-0.25/(100-hum_reference)*current_humidity)+0.416666)*100

gas_lower_limit = 5000   # Bad air quality limit
gas_upper_limit = 50000  # Good air quality limit

if gas_reference > gas_upper_limit:
    gas_reference = gas_upper_limit

if gas_reference < gas_lower_limit:
    gas_reference = gas_lower_limit

gas_score = (0.75/(gas_upper_limit-gas_lower_limit)*gas_reference -(gas_lower_limit*(0.75/(gas_upper_limit-gas_lower_limit))))

gas_score = gas_score * 100

air_quality_score = (100-(hum_score + gas_score))*5
print air_quality_score
