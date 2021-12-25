from neopixel import NeoPixel

from .helper import clear


class LightUpPartOfTree:
    name = 'part of tree'
    description = ''
    authors = ('mirek <mirek@namakanyden.sk>')
    code = 1006


    def run(self, pixels: NeoPixel, color: tuple, index: int, parts: int, **kwargs):
        clear(pixels)

        group = pixels.n / parts
        start_idx = int(pixels.n - group * (index + 1))
        last_idx = int(start_idx + group)

        for i in range(start_idx, last_idx + 1):
            pixels[i] = color
        pixels.write()
