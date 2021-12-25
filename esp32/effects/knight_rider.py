from time import sleep_ms
from neopixel import NeoPixel

from .helper import clear


class KnightRiderEffect:
    name = 'knight rider'
    description = ''
    authors = ('mirek <mirek@namakanyden.sk>')
    code = 1005


    def run(self, pixels: NeoPixel, color: tuple, duration: int, **kwargs):
        """
        knight rider effect
        stolen from: https://learn.adafruit.com/larson-scanner-shades/circuitpython-code
        """
        clear(pixels)

        pos = 2
        direction = 1

        while True:
            pixels[pos - 2] = ([0, 16, 0])  # Dark red
            pixels[pos - 1] = ([0, 128, 0])  # Medium red
            pixels[pos] = ([48, 255, 0])  # brightest
            pixels[pos + 1] = ([0, 128, 0])  # Medium red

            if (pos + 2) < pixels.n:
                # Dark red, do not exceed number of pixels
                pixels[pos + 2] = ([0, 16, 0])

            pixels.write()
            sleep_ms(50)
            yield

            # Rather than being sneaky and erasing just the tail pixel,
            # it's easier to erase it all and draw a new one next time.
            for j in range(-2, 2):
                pixels[pos + j] = (0, 0, 0)
                if (pos + 2) < pixels.n:
                    pixels[pos + 2] = (0, 0, 0)

            # Bounce off ends of strip
            pos += direction
            if pos - 2 < 0:
                pos = 2
                direction = -direction
            elif pos >= (pixels.n - 1):
                pos = pixels.n - 2
                direction = -direction
