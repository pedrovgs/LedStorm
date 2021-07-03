import RPi.GPIO as GPIO
import time
 
pin = 21
interval = 1
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

def blink():
    print ("LED on")
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(interval)
    print ("LED off")
    GPIO.output(pin, GPIO.LOW)
    time.sleep(interval)


if __name__ == '__main__':
    print("Starting health check. You can stop this process by pressing CTRL + C")
    try:
        while True:
            blink()
 
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")
        GPIO.cleanup()