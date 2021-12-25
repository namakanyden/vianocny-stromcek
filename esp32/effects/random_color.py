from random import randint
from time import sleep_ms
from neopixel import NeoPixel


class RandomColorEffect:
    name = 'random color'
    description = 'Random color is set to every NeoPixel.'
    authors = ('mirek <mirek@namakanyden.sk>')
    code = 1008
    
    def run(self, pixels: NeoPixel, duration: int, **kwargs):
       
        while True:
            for i in range(pixels.n):
                red = randint(0, 255)
                green = randint(0, 255)
                blue = randint(0, 255)
                pixels[i] = (red, green, blue)
            pixels.write()
            sleep_ms(duration)
            yield
