#
#Author : Juraj Remen
#

from microbit import sleep, display, pin0, uart
from random import randint
import neopixel
from builtins import eval

np = neopixel.NeoPixel(pin0, 6)
new = 0

def clear(pixels):
    for i in range(len(pixels)):
        pixels[i] = (0, 0, 0)
    pixels.show()


def set_color(pixels, color):
    for i in range(len(pixels)):
        pixels[i] = color
    pixels.show()


def set_random_color(pixels, wait):
    for i in range(len(pixels)):
        color = (randint(0, 60), randint(0, 60), randint(0, 60))
        pixels[i] = color
    pixels.show()
    sleep(wait)


def bounce(pixels, color, wait):  # odražanie nefunguje
    clear(pixels)
    n = len(pixels)
    for i in range(2 * n):
        for j in range(n):
            pixels[j] = color
        if (i // n) % 2 == 0:
            pixels[i % n] = (0, 0, 0)
        else:
            pixels[n - 1 - (i % n)] = (0, 0, 0)
        pixels.show()
        sleep(wait)


def cycle(pixels, color, wait):
    clear(pixels)
    for i in range(len(pixels)):
        pixels[i] = color
        pixels.show()
        sleep(wait)
        pixels[i] = (0, 0, 0)
    pixels.show()


def knight_rider(pixels, color, speed):
    clear(pixels)
    for i in range(len(pixels)):
        pixels[i] = color
        pixels[-i - 1] = color
        pixels.show()
        sleep(speed)
        pixels[i] = (0, 0, 0)
        pixels[-i - 1] = (0, 0, 0)
    pixels.show()


def fade(pixels, color, speed):
    set_color(pixels, color)
    n_color = color
    while sum(n_color) > 0:
        sleep(speed)
        n_color = (
            int(n_color[0] // 1.01),
            int(n_color[1] // 1.01),
            int(n_color[2] // 1.01),
        )
        set_color(pixels, n_color)
    set_color(pixels, (0, 0, 0))
    r, g, b = 0, 0, 0
    n_color = (0, 0, 0)
    n_speed = color[0] / 255, color[1] / 255, color[2] / 255
    while sum(n_color) < (sum(color)):
        sleep(speed)
        r += n_speed[0]
        g += n_speed[1]
        b += n_speed[2]
        n_color = (int(r), int(g), int(b))
        set_color(pixels, n_color)


def wheel(pos):
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


def rainbow_cycle(pixels, speed):
    n = len(pixels)
    clear(np)
    sleep(100)
    for j in range(255):
        for i in range(n):
            rc_index = (i * 256 // n) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        sleep(speed)


def part_of_tree(pixels, color, ind, part):
    clear(np)
    sleep(100)
    for i in range(ind, len(pixels), part):
        pixels[i] = color
    pixels.show()


# msg = '{"scenario":"clear","color":[246,4,4],"duration":"100"}'
# msg = '{"scenario":"knight rider","color":[246,4,4],"duration":"100"}'
# msg = '{"scenario":"rainbow","color":[86,61,124],"duration":"85"}'
# msg = '{"scenario":"fade","color":[1,1,124],"duration":"102"}'
msg = '{"scenario":"set color","color":[20,0,0],"duration":102}'
# msg = '{"scenario":"bounce","color":[6,61,1],"duration":"202"}'
# msg = '{"scenario":"cycle","color":[86,61,124],"duration":"85"}'
# msg = '{"scenario":"random color","color":[255,0,0],"duration":"100"}'
# msg = '{"scenario":"part of tree","color":[255,0,0],"index":2,"parts":6}'
while True:
    json = eval(msg)
    if uart.any():
        rcv = uart.readline()
        msg = str(rcv, "utf-8")
    if "scenario" in json:
        scenar = json["scenario"]
        # scenar='cycle'
        color = tuple(json["color"])
        # color=(60,0,0)
        if scenar == "part of tree":
            ind, part = json["index"], json["parts"]
        else:
            cas = int(json["duration"])
        # cas=100
        if scenar == "clear":
            display.show("z")  # zmaž
            clear(np)
            sleep(100)
        elif scenar == "knight rider":
            display.show("k")
            knight_rider(np, color, cas)
        elif scenar == "rainbow":
            display.show("d")
            rainbow_cycle(np, cas)
        elif scenar == "fade":
            display.show("f")
            fade(np, color, cas // 4)
        elif scenar == "set color":
            display.show("s")
            set_color(np, color)
        elif scenar == "bounce":
            display.show("b")
            bounce(np, color, cas)
        elif scenar == "cycle":
            display.show("c")
            cycle(np, color, cas)
        elif scenar == "random color":
            display.show("r")
            set_random_color(np, cas)
        elif scenar == 'part of tree':
            display.show('p')
            part_of_tree(np, color, ind, part)
        else:
            display.show("F")  # error
            sleep(1000)
    else:
        display.show("E")  # error
        sleep(1000)
    sleep(100)
