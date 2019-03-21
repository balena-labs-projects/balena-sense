# Approximate air quality reading
# Adapted from: https://raw.githubusercontent.com/pimoroni/bme680-python/master/examples/indoor-air-quality.py
def start_bme680(sensor):
    import bme680
    import time
    global gas_baseline
    # These oversampling settings can be tweaked to
    # change the balance between accuracy and noise in
    # the data.
    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

    sensor.set_gas_heater_temperature(320)
    sensor.set_gas_heater_duration(150)
    sensor.select_gas_heater_profile(0)

    # start_time and curr_time ensure that the
    # burn_in_time (in seconds) is kept track of.

    start_time = time.time()
    curr_time = time.time()
    burn_in_time = 300

    burn_in_data = []


    # Collect gas resistance burn-in values, then use the average
    # of the last 50 values to set the upper limit for calculating
    # gas_baseline.
    print('Collecting gas resistance burn-in data for 5 min\n')
    while curr_time - start_time < burn_in_time:
        curr_time = time.time()
        if sensor.get_sensor_data() and sensor.data.heat_stable:
            gas = sensor.data.gas_resistance
            burn_in_data.append(gas)
            timeleft = 300 - (curr_time - start_time)
            timeleft = int(round(timeleft))
            print('Gas: {0} Ohms. Starting data collection loop in {1:d} seconds'.format(gas, timeleft))
            time.sleep(1)

    gas_baseline = sum(burn_in_data[-50:]) / 50.0

    print('Burn-in complete!\n')
    return gas_baseline



def get_readings(sensor):
    global gas_baseline
    # Set the humidity baseline to 40%, an optimal indoor humidity.
    hum_baseline = 40.0

    # This sets the balance between humidity and gas reading in the
    # calculation of air_quality_score (25:75, humidity:gas)
    hum_weighting = 0.25

    if sensor.get_sensor_data() and sensor.data.heat_stable:
        gas = sensor.data.gas_resistance
        gas_offset = gas_baseline - gas

        hum = sensor.data.humidity
        hum_offset = hum - hum_baseline

        # Calculate hum_score as the distance from the hum_baseline.
        if hum_offset > 0:
            hum_score = (100 - hum_baseline - hum_offset)
            hum_score /= (100 - hum_baseline)
            hum_score *= (hum_weighting * 100)

        else:
            hum_score = (hum_baseline + hum_offset)
            hum_score /= hum_baseline
            hum_score *= (hum_weighting * 100)

        # Calculate gas_score as the distance from the gas_baseline.
        if gas_offset > 0:
            gas_score = (gas / gas_baseline)
            gas_score *= (100 - (hum_weighting * 100))

        else:
            gas_score = 100 - (hum_weighting * 100)

        # Calculate air_quality_score.
        air_quality_score = hum_score + gas_score

        return [
            {
                'measurement': 'balena-sense',
                'fields': {
                    'temperature': float(sensor.data.temperature),
                    'pressure': float(sensor.data.pressure),
                    'humidity': float(sensor.data.humidity),
                    'air_quality_score': float(air_quality_score)
                }
            }
        ]
