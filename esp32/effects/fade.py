from time import sleep_ms
from neopixel import NeoPixel

from .helper import clear


class FadeEffect:
    name = 'fade'
    description = ''
    authors = ('mirek <mirek@namakanyden.sk>')
    code = 1004


    def run(self, pixels: NeoPixel, color: tuple, duration: int, **kwargs):
        delay = duration // pixels.n
        clear(pixels)

        while True:
            for i in range(0, 4 * 256, 8):
                for j in range(pixels.n):
                    if (i // 256) % 2 == 0:
                        val = i & 0xff
                    else:
                        val = 255 - (i & 0xff)
                    pixels[j] = (val, color[1], color[2])
                pixels.write()
                sleep_ms(delay)
                yield
