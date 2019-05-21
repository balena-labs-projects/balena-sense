import struct

class LedMatrix():
    def __init__(self):
        self._fb_device = '/dev/fb1'

        self._pix_map = [
             [0,  1,  2,  3,  4,  5,  6,  7],
             [8,  9, 10, 11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20, 21, 22, 23],
            [24, 25, 26, 27, 28, 29, 30, 31],
            [32, 33, 34, 35, 36, 37, 38, 39],
            [40, 41, 42, 43, 44, 45, 46, 47],
            [48, 49, 50, 51, 52, 53, 54, 55],
            [56, 57, 58, 59, 60, 61, 62, 63]
        ]

    def _pack_bin(self, pix):
        """
        Internal. Encodes python list [R,G,B] into 16 bit RGB565
        """

        r = (pix[0] >> 3) & 0x1F
        g = (pix[1] >> 2) & 0x3F
        b = (pix[2] >> 3) & 0x1F
        bits16 = (r << 11) + (g << 5) + b
        return struct.pack('H', bits16)

    def set_pixels(self, pixel_list):
        """
        Accepts a list containing 64 smaller lists of [R,G,B] pixels and
        updates the LED matrix. R,G,B elements must intergers between 0
        and 255
        """

        if len(pixel_list) != 64:
            raise ValueError('Pixel lists must have 64 elements')

        for index, pix in enumerate(pixel_list):
            if len(pix) != 3:
                raise ValueError('Pixel at index %d is invalid. Pixels must contain 3 elements: Red, Green and Blue' % index)

            for element in pix:
                if element > 255 or element < 0:
                    raise ValueError('Pixel at index %d is invalid. Pixel elements must be between 0 and 255' % index)

        with open(self._fb_device, 'wb') as f:
            map = self._pix_map
            for index, pix in enumerate(pixel_list):
                # Two bytes per pixel in fb memory, 16 bit RGB565
                f.seek(map[index // 8][index % 8] * 2)  # row, column
                f.write(self._pack_bin(pix))

    def clear(self, *args):
        """
        Clears the LED matrix with a single colour, default is black / off

        e.g. ap.clear()
        or
        ap.clear(r, g, b)
        or
        colour = (r, g, b)
        ap.clear(colour)
        """

        black = (0, 0, 0)  # default

        if len(args) == 0:
            colour = black
        elif len(args) == 1:
            colour = args[0]
        elif len(args) == 3:
            colour = args
        else:
            raise ValueError('Pixel arguments must be given as (r, g, b) or r, g, b')

        self.set_pixels([colour] * 64)
