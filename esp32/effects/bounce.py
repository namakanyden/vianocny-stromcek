from time import sleep_ms
from neopixel import NeoPixel

from .helper import clear


class BounceEffect:
    name = 'bounce'
    description = ''
    authors = ('mirek <mirek@namakanyden.sk>')
    code = 1000
    
    def run(self, pixels: NeoPixel, color: tuple, duration: int, **kwargs):
        # setup
        delay = duration // pixels.n
        clear(pixels)

        # loop
        n = pixels.n
        while True:
            for i in range(2 * pixels.n):
                for j in range(pixels.n):
                    pixels[j] = (color[0], color[1], color[2])
                if (i // pixels.n) % 2 == 0:
                    pixels[i % pixels.n] = (0, 0, 0)
                else:
                    # pixels[pixels.n – 1 – (i % pixels.n)] = (0, 0, 0)
                    pixels[n - 1 - (i % n)] = (0, 0, 0)
                    #pixels[i % pixels.n] = (0,0,0)
                pixels.write()
                sleep_ms(delay)
                yield
