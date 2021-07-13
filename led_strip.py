import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
try:
    from rpi_ws281x import Color, Adafruit_NeoPixel
except ImportError:
    print("Error found importing rpi_ws281x library")


# LED strip configuration:
LED_COUNT = 50          # Number of LED pixels.
LED_FREQ_HZ = 800000    # LED signal frequency in hertz
LED_DMA = 10            # DMA channel to use for generating signal
LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest
LED_INVERT = False      # True to invert the signal
LED_PIN_1 = 18          # GPIO pin 18
LED_CHANNEL_1 = 0       # set to '0' for GPIOs 18, etc.
LED_PIN_2 = 19          # GPIO pin 19
LED_CHANNEL_2 = 1       # set to '1' for GPIOs 19, etc.

DEFAULT_COLOR = Color(196, 234, 252)

def initialize():
    print("Initializing led strip 1")
    strip1 = Adafruit_NeoPixel(
        LED_COUNT,
        LED_PIN_1,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
        LED_CHANNEL_1)
    strip1.begin()
    print("Led strip 1 intialized")
    time.sleep(1) # Needed to ensure both leds are initialized properly
    print("Initializing led strip 2")
    strip2 = Adafruit_NeoPixel(
        LED_COUNT,
        LED_PIN_2,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
        LED_CHANNEL_2)
    strip2.begin()
    print("Led strip 2 intialized")
    return [strip1, strip2]


def trigger_lightning(lightnings):
    pool = ThreadPoolExecutor(len(lightnings))
    futures = []
    print("Let's make some noise!")
    for lightning in lightnings:
        future = pool.submit(show_lightning, lightning.strip, lightning.color)
        futures.append(future)
    print("Waitining for lightnings to be done")
    for waitingFuture in as_completed(futures):
        print(waitingFuture.result())
    print("Lightning request accomplished")

def show_lightning(strip, color):
    adafruitColor = Color(color.red, color.green, color.blue)
    # Wait a random amount of time before showing the lightning
    time.sleep(random.uniform(0.0, 1.5))
    color_thunder(strip, adafruitColor)
    blink(strip, adafruitColor)
    turn_off(strip)
    return "Lightning shown!"

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
