import subprocess
import json
import threading
import io

class BME680:
    data = None

    def __init__(self, readfrom):
        if readfrom == 'bme680secondary':
            self.command = '/usr/src/app/bsec_bme680_linux/bsec_bme680 secondary'
        else:
            self.command = '/usr/src/app/bsec_bme680_linux/bsec_bme680'

        self.capture_thread = threading.Thread(target=self.capture)
        self.capture_thread.start()

    def capture(self):
        # Start the process and commence capture and parsing of the output
        process = subprocess.Popen([self.command], stdout=subprocess.PIPE)

        for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
            self.data = json.loads(line.strip())

        rc = process.poll()
        return rc

    def get_readings(self, sensor):
        return [
            {
                'measurement': 'balena-sense',
                'fields': {
                    'temperature': float(self.data['temperature']),
                    'pressure': float(self.data['pressure']),
                    'humidity': float(self.data['humidity']),
                    'air_quality_score': float(self.data['iaq']),
                    'air_quality_score_accuracy': int(self.data['iaq_accuracy']),
                    'eco2_ppm': float(self.data['eco2_ppm']),
                    'bvoce_ppm': float(self.data['bvoce_ppm'])
                }
            }
        ]
