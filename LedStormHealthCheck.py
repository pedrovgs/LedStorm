import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

def blink():
    print ("LED on")
    time.sleep(1)
    GPIO.output(18,GPIO.HIGH)
    print ("LED off")
    time.sleep(1)
    GPIO.output(18,GPIO.LOW)


if __name__ == '__main__':
    print("Starting health check. You can stop this process by pressing CTRL + C")
    try:
        while True:
            blink()
 
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")
        GPIO.cleanup()