import subprocess
import json
import threading
import io
import time
from bme280 import BME280

class ENVIROPLUS:

    def __init__(self):
        try:
            self.bme280 = BME280()
        except ImportError:
            print('Failed to load Enviro Plus BME280 module')
        
        try:
            from enviroplus import gas
        except ImportError as e:
            print(e)

        self.sensor = 'enviroplus'

    def get_readings(self, sensor):
        current_temperature = self.bme280.get_temperature()
        current_pressure = self.bme280.get_pressure()
        current_humidity = self.bme280.get_humidity()

        return [
            {
                'measurement': 'balena-sense',
                'fields': {
                    'temperature': float(current_temperature),
                    'pressure': float(current_pressure),
                    'humidity': float(current_humidity)
                }
            }
        ]
