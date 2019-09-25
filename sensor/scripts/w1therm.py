import subprocess
import json
import threading
import io
import time
from w1thermsensor import W1ThermSensor

class W1THERM:

    def __init__(self, sid):
        self.sensor = W1ThermSensor(sensor_id=sid)

    def get_readings(self, sensor):
        current_temperature = self.sensor.get_temperature()
        return [
            {
                'measurement': 'balena-sense',
                'fields': {
                    'temperature': float(current_temperature)
                }
            }
        ]
