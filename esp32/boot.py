from machine import Pin, reset
from neopixel import NeoPixel
import esp

from settings import NEOPIXEL


# disable debug
esp.osdebug(None)

# init neopixel
pixels = NeoPixel(Pin(NEOPIXEL['pin']), NEOPIXEL['pixels'])


