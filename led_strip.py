import time
try:
    from rpi_ws281x import Color, Adafruit_NeoPixel
except ImportError:
    print("Error found importing rpi_ws281x library")


# LED strip configuration:
LED_COUNT = 50      # Number of LED pixels.
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_PIN_1 = 18
LED_CHANNEL_1 = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_PIN_2 = 19
LED_CHANNEL_2 = 1       # set to '1' for GPIOs 18, etc
DEFAULT_COLOR = Color(196, 234, 252)

def initialize():
    print("Initializing led stripe")
    strip1 = Adafruit_NeoPixel(
        LED_COUNT,
        LED_PIN_1,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
        LED_CHANNEL_1)
    strip1.begin()
    strip2 = Adafruit_NeoPixel(
        LED_COUNT,
        LED_PIN_2,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
        LED_CHANNEL_2)
    strip2.begin()
    return [strip1, strip2]


def trigger_lightning(stripes, color = DEFAULT_COLOR):
    print("Let's make some noise!")
    for strip in stripes:
        color_thunder(strip, color)
        blink(strip, color)
        turn_off(strip)


def color_thunder(strip, color):
    print("Starting color thunder")
    wait = 1
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait / 10000.0)
        wait = wait + 2
    time.sleep(0.4)
    print("Color thunder done")


def blink(strip, color):
    turn_off(strip)
    fill(strip, color)
    time.sleep(0.2)
    turn_off(strip)
    time.sleep(0.4)
    fill(strip, color)
    time.sleep(0.2)
    turn_off(strip)
    time.sleep(0.1)
    fill(strip, color)


def turn_off(strip):
    fill(strip, Color(0, 0, 0))


def fill(strip, color):
    print("Turning strip off")
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    print("Color thunder done")
