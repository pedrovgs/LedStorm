from rpi_ws281x import *
import time

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def initialize():
    print ("Initializing led stripe")
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    return strip

def trigger_lightning(strip):
    print ("Let's make some noise!")
    color = Color(196, 234, 252)
    color_thunder(strip, color)
    blink(strip, color)
    turn_off(strip)

def color_thunder(strip, color):
    print ("Starting color thunder")
    wait = 1
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait/10000.0)
        wait_ms = wait + 2
    time.sleep(0.4)
    print ("Color thunder done")

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
    print ("Turning strip off")
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    print ("Color thunder done")
