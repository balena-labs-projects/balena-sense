# Credit: https://github.com/youkidearitai/rpi-sensors
import smbus
import time

class Lps25hsensor:
    address = 0x5c

    PRESS_OUT_XL = 0x28
    PRESS_OUT_L = 0x29
    PRESS_OUT_H = 0x2A

    def __init__(self, smbus_addr = 1):
        self.bus = smbus.SMBus(smbus_addr)

    def setup(self):
        try:
            self.bus.write_i2c_block_data(self.address, 0x00, [])
        except OSError as e:
            print(e)

        time.sleep(0.1)

    def read(self):
        try:
            self.bus.write_i2c_block_data(self.address, 0x20, [0x90])
        except OSError as e:
            print(e)

        time.sleep(0.05)

        pressure = (
          self.read_i2c_block(self.PRESS_OUT_XL) << 0 |
          self.read_i2c_block(self.PRESS_OUT_L) << 8 |
          self.read_i2c_block(self.PRESS_OUT_H) << 16
        )
        pressure = pressure / 4096

        return pressure

    def read_i2c_block(self, register):
        blocks = self.bus.read_i2c_block_data(self.address, register, 1)
        return blocks[0]