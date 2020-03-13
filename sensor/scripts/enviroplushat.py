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
            self.gas = gas
        except ImportError as e:
            print(e)
        try:
            # Transitional fix for breaking change in LTR559
            from ltr559 import LTR559
            self.ltr559 = LTR559()
        except ImportError:
            import self.ltr559
        
        self.sensor = 'enviroplus'

    def get_readings(self, sensor):
        current_temperature = self.bme280.get_temperature()
        current_pressure = self.bme280.get_pressure()
        current_humidity = self.bme280.get_humidity()
        current_lux = self.ltr559.get_lux()
        current_gas = self.gas.read_all()
        current_oxidising = current_gas.oxidising / 1000
        current_reducing = current_gas.reducing / 1000
        current_nh3 = current_gas.nh3 / 1000
        return [
            {
                'measurement': 'balena-sense',
                'fields': {
                    'temperature': float(current_temperature),
                    'pressure': float(current_pressure),
                    'humidity': float(current_humidity),
                    'light': float(current_lux),
                    'oxidising': float(current_oxidising),
                    'reducing': float(current_reducing),
                    'nh3': float(current_nh3)
                }
            }
        ]
