def get_readings(sensor):
    # The sense HAT does not include any way to obtain an air quality score via gas measurement,
    # so we can create one using the temperature and humidity reading based on distance from ideal values
    max_iaq = 500
    min_iaq = 25

    temperature_ideal = 25
    temperature_worst_variance = 40

    humidity_ideal = 40
    humidity_worst_variance = 40
    humidity_weighting = 0.25 # this means % of the AQ figure will be humidity, the rest will be temperature

    # Get the current temperature and humidity readings
    current_temperature = sensor.get_temperature()
    current_humidity = sensor.get_humidity()

    # Find out how far from the ideal the current values are
    current_temperature_variance = abs(current_temperature - temperature_ideal)/temperature_worst_variance
    # if the variance is greater than 1 (100%), set it to as a maximum
    # note also that 100% here is the worst possible value
    if current_temperature_variance > 1:
        current_temperature_variance = 1

    # Do the same thing for the humidity reading
    current_humidity_variance = abs(current_humidity - humidity_ideal)/humidity_worst_variance
    if current_humidity_variance > 1:
        current_humidity_variance = 1

    # Scale the current variance measurements in accordance with the weighting to calculate a percentage
    # this gives us a score where 1 is the worst possible value
    air_quality_score = (current_humidity_variance * humidity_weighting) + (current_temperature_variance * (1 - humidity_weighting))
    air_quality_score = air_quality_score * 500

    # As we have a sense HAT we can give an indication of the air quality on the LED matrix
    from ledmatrix import LedMatrix

    display = LedMatrix()
    display.clear()
    if air_quality_score < 100:
        # Happy face!
        face_color = [0, 255, 0]
        face_pixels = [
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 1, 0, 0, 0, 0, 1, 0,
            1, 0, 1, 0, 0, 1, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 0, 0, 1, 0, 1,
            1, 0, 0, 1, 1, 0, 0, 1,
            0, 1, 0, 0, 0, 0, 1, 0,
            0, 0, 1, 1, 1, 1, 0, 0
        ]
    elif air_quality_score < 250:
        # Neutral face
        face_color = [250, 255, 0]
        face_pixels = [
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 1, 0, 0, 0, 0, 1, 0,
            1, 0, 1, 0, 0, 1, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 1, 1, 1, 1, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 1,
            0, 1, 0, 0, 0, 0, 1, 0,
            0, 0, 1, 1, 1, 1, 0, 0
        ]
    else:
        # Sad face
        face_color = [255, 0, 0]
        face_pixels = [
            0, 0, 1, 1, 1, 1, 0, 0,
            0, 1, 0, 0, 0, 0, 1, 0,
            1, 0, 1, 0, 0, 1, 0, 1,
            1, 0, 0, 0, 0, 0, 0, 1,
            1, 0, 0, 1, 1, 0, 0, 1,
            1, 0, 1, 0, 0, 1, 0, 1,
            0, 1, 0, 0, 0, 0, 1, 0,
            0, 0, 1, 1, 1, 1, 0, 0
        ]

    for x in range(64):
        if face_pixels[x] == 1:
            face_pixels[x] = face_color
        elif face_pixels[x] == 0:
            face_pixels[x] = [0,0,0]

    display.set_pixels(face_pixels)

    return [
        {
            'measurement': 'balena-sense',
            'fields': {
                'temperature': float(current_temperature),
                # 'pressure': float(sensor.environ.pressure),
                'humidity': float(current_humidity),
                'air_quality_score': float(air_quality_score)
            }
        }
    ]
