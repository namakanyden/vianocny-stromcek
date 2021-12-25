# https://randomnerdtutorials.com/micropython-ws2812b-addressable-rgb-leds-neopixel-esp32-esp8266/

from time import sleep_ms
from neopixel import NeoPixel


class RainbowEffect:
    name = 'rainbow'
    description = ''
    authors = ('mirek <mirek@namakanyden.sk>')
    code = 1007


    def _wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)


    def run(self, pixels: NeoPixel, duration: int, **kwargs):
        delay = duration // pixels.n
        
        while True:
            for j in range(255):
                for i in range(pixels.n):
                    rc_index = (i * 256 // pixels.n) + j
                    pixels[i] = self._wheel(rc_index & 255)
                pixels.write()
                sleep_ms(delay)
                yield
