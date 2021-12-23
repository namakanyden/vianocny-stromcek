from machine import Pin, reset, WDT
from neopixel import NeoPixel
import esp

from config import NEOPIXEL, WDT_TIMEOUT
import logging

#logging.set_level(logging.ERROR)


# disable debug
esp.osdebug(None)

# set Watchdog first
#wdt = WDT(timeout = WDT_TIMEOUT)

# init neopixel
pixels = NeoPixel(Pin(NEOPIXEL['pin']), NEOPIXEL['pixels'])
