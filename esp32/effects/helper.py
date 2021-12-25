from neopixel import NeoPixel


def clear(pixels: NeoPixel):
    for i in range(pixels.n):
        pixels[i] = (0, 0, 0)
    pixels.write()
