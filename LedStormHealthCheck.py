import RPi.GPIO as GPIO
import time

def blink():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(18,GPIO.LOW)


if __name__ == '__main__':
    print("Starting health check. You can stop this process by pressing CTRL + C")
    try:
        while True:
            blink()
 
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")
        GPIO.cleanup()