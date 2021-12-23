from time import sleep_ms
from neopixel import NeoPixel

from .helper import clear


class CycleEffect:
    name = 'cycle'
    description = ''
    authors = ('mirek <mirek@namakanyden.sk>')
    code = 1003

    def run(self, pixels: NeoPixel, color: tuple, duration: int, **kwargs): # wait=25):
        delay = duration // pixels.n
        clear(pixels)

        while True:
            for i in range(pixels.n - 1, 0, -1):
                pixels[i % pixels.n] = color
                pixels.write()
                sleep_ms(delay)
                pixels[i] = (0, 0, 0)
                yield
            else:
                pixels.write()

