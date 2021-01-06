# https://randomnerdtutorials.com/micropython-ws2812b-addressable-rgb-leds-neopixel-esp32-esp8266/
import time
import random

from helper import Color


def clear(pixels):
    print('>> running clear')
    for i in range(pixels.n):
        pixels[i] = (0, 0, 0)
    pixels.write()
    

def set_color(pixels, color):
    print('>> running set color')
    for i in range(pixels.n):
        pixels[i] = (color.r, color.g, color.b)
    pixels.write()
    
    
def set_random_color(pixels, wait):
    print('>> running set_random_color')
    while True:
        for i in range(pixels.n):
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.write()
        time.sleep_ms(wait)
        yield
  
  
def bounce(pixels, color, wait, once = False):
    clear(pixels)
    print('>> running bounce')
    
    n = pixels.n
    while True:
        for i in range(2 * pixels.n):
            for j in range(pixels.n):
                pixels[j] = (color.r, color.g, color.b)
            if (i // pixels.n) % 2 == 0:
                pixels[i % pixels.n] = (0, 0, 0)
            else:
                #pixels[pixels.n – 1 – (i % pixels.n)] = (0, 0, 0)
                pixels[n - 1 - (i % n)] = (0, 0, 0)
                #pixels[i % pixels.n] = (0,0,0)
            pixels.write()
            time.sleep_ms(wait)
            yield
            
        if once == True:
            break
    
    
def cycle(pixels, color, wait = 25, once = False):
    clear(pixels)
    print('>> running cycle')
    
    while True:
        for i in range(pixels.n - 1, 0, -1):
            pixels[i % pixels.n] = color.as_tuple() #(color.r, color.g, color.b)
            pixels.write()
            time.sleep_ms(wait)
            pixels[i] = (0, 0, 0)
            yield
        else:
            pixels.write()
            
        if once == True:
            break


def wheel(pos):
    #Input a value 0 to 255 to get a color value.
    #The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def rainbow_cycle(pixels, wait, once = False):
    print('>> running rainbow_cycle')
    clear(pixels)
    
    while True:
        for j in range(255):
            for i in range(pixels.n):
                rc_index = (i * 256 // pixels.n) + j
                pixels[i] = wheel(rc_index & 255)
            pixels.write()
            time.sleep_ms(wait)
            yield
            
        if once == True:
            break
    
    
def fade(pixels, color, delay, once=False):
    clear(pixels)
    print('>> running fade')
    
    while True:
        for i in range(0, 4 * 256, 8):
            for j in range(pixels.n):
                if (i // 256) % 2 == 0:
                    val = i & 0xff
                else:
                    val = 255 - (i & 0xff)
                pixels[j] = (val, color.g, color.b)
            pixels.write()
            time.sleep_ms(delay)
            yield
            
        if once == True:
            break
        
        
def dim_color(color, width):
    print(color)
    print(color.value)
    return (((color.value & 0xff0000)//width)& 0xff0000) + (((color.value & 0x00ff00)//width) & 0x00FF00) + (((color.value & 0x0000FF)//width)&0x0000FF)

    
def knight_rider(pixels, color, speed):
    """
    knight rider effect
    stolen from: https://learn.adafruit.com/larson-scanner-shades/circuitpython-code
    """
    clear(pixels)
    print('>> running knight rider')
    
    pos = 0
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
        time.sleep_ms(50)
        yield
     
        # Rather than being sneaky and erasing just the tail pixel,
        # it's easier to erase it all and draw a new one next time.
        for j in range(-2, 2):
            pixels[pos + j] = (0, 0, 0)
            if (pos + 2) < pixels.n:
                pixels[pos + 2] = (0, 0, 0)
     
        # Bounce off ends of strip
        pos += direction
        if pos < 0:
            pos = 1
            direction = -direction
        elif pos >= (pixels.n - 1):
            pos = pixels.n - 2
            direction = -direction


def light_up_part_of_tree(pixels, color, parts, index):
    clear(pixels)
    print('>> running light up part of the tree')
    
    group = pixels.n / parts
    start_idx = int(pixels.n - group * (index + 1))
    last_idx = int(start_idx + group)
    
    for i in range(start_idx, last_idx + 1):
        pixels[i] = color.as_tuple()
    pixels.write()
    

def demo(pixels):
    print('>> running demo')
    
    while True:
        # cycle
        cycle(pixels, (255, 255, 255), 25, once = True)

        # bounce
        bounce(pixels, (0, 0, 128), 60, once = True)

        # fade in/out
        fade(pixels, once = True)
