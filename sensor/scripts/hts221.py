# Modified/classified from https://raw.githubusercontent.com/ControlEverythingCommunity/HTS221/master/Python/HTS221.py
import smbus
import time

class HTS221:
    temperature_units = 'C'

    data = None
    data_timestamp = 0

    def __init__(self, temperature_units = 'C'):
        if temperature_units != 'C':
            self.temperature_units = 'F'

        self.bus = smbus.SMBus(1)

        # HTS221 address, 0x5F(95)
        # Select average configuration register, 0x10(16)
        #		0x1B(27)	Temperature average samples = 256, Humidity average samples = 512
        self.bus.write_byte_data(0x5F, 0x10, 0x1B)
        # HTS221 address, 0x5F(95)
        # Select control register1, 0x20(32)
        #		0x85(133)	Power ON, Continuous update, Data output rate = 1 Hz
        self.bus.write_byte_data(0x5F, 0x20, 0x85)

        time.sleep(0.5)

        # HTS221 address, 0x5F(95)
        # Read Calibration values from non-volatile memory of the device
        # Humidity Calibration values
        # Read data back from 0x30(48), 1 byte
        val = self.bus.read_byte_data(0x5F, 0x30)
        H0 = val / 2

        # Read data back from 0x31(49), 1 byte
        val = self.bus.read_byte_data(0x5F, 0x31)
        H1 = val /2

        # Read data back from 0x36(54), 2 bytes
        val0 = self.bus.read_byte_data(0x5F, 0x36)
        val1 = self.bus.read_byte_data(0x5F, 0x37)
        H2 = ((val1 & 0xFF) * 256) + (val0 & 0xFF)

        # Read data back from 0x3A(58), 2 bytes
        val0 = self.bus.read_byte_data(0x5F, 0x3A)
        val1 = self.bus.read_byte_data(0x5F, 0x3B)
        H3 = ((val1 & 0xFF) * 256) + (val0 & 0xFF)

        self.humidity_calibration = [H0, H1, H2, H3]

        # Temperature Calibration values
        # Read data back from 0x32(50), 1 byte
        T0 = self.bus.read_byte_data(0x5F, 0x32)
        T0 = (T0 & 0xFF)

        # Read data back from 0x32(51), 1 byte
        T1 = self.bus.read_byte_data(0x5F, 0x33)
        T1 = (T1 & 0xFF)

        # Read data back from 0x35(53), 1 byte
        raw = self.bus.read_byte_data(0x5F, 0x35)
        raw = (raw & 0x0F)

        # Convert the temperature Calibration values to 10-bits
        T0 = ((raw & 0x03) * 256) + T0
        T1 = ((raw & 0x0C) * 64) + T1

        # Read data back from 0x3C(60), 2 bytes
        val0 = self.bus.read_byte_data(0x5F, 0x3C)
        val1 = self.bus.read_byte_data(0x5F, 0x3D)
        T2 = ((val1 & 0xFF) * 256) + (val0 & 0xFF)

        # Read data back from 0x3E(62), 2 bytes
        val0 = self.bus.read_byte_data(0x5F, 0x3E)
        val1 = self.bus.read_byte_data(0x5F, 0x3F)
        T3 = ((val1 & 0xFF) * 256) + (val0 & 0xFF)

        self.temperature_calibration = [T0, T1, T2, T3]


    def read_data(self):
        if self.data_timestamp < (int(round(time.time() * 1000)) - 1000):
            self.data = self.bus.read_i2c_block_data(0x5F, 0x28 | 0x80, 4)
            self.data_timestamp = int(round(time.time() * 1000))

    def get_temperature(self):
        self.read_data()

        temp = (self.data[3] * 256) + self.data[2]
        if temp > 32767 :
        	temp -= 65536
        cTemp = ((self.temperature_calibration[1] - self.temperature_calibration[0]) / 8.0) * (temp - self.temperature_calibration[2]) / (self.temperature_calibration[3] - self.temperature_calibration[2]) + (self.temperature_calibration[0] / 8.0)
        fTemp = (cTemp * 1.8 ) + 32

        if self.temperature_units == 'F':
            return fTemp
        else:
            return cTemp


    def get_humidity(self):
        self.read_data()

        humidity = (self.data[1] * 256) + self.data[0]
        humidity = ((1.0 * self.humidity_calibration[1]) - (1.0 * self.humidity_calibration[0])) * (1.0 * humidity - 1.0 * self.humidity_calibration[2]) / (1.0 * self.humidity_calibration[3] - 1.0 * self.humidity_calibration[2]) + (1.0 * self.humidity_calibration[0])

        return humidity
