#Libraries
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
GPIO_TRIGGER = 10
GPIO_ECHO = 12
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    print("Let's start LedStorm project. You can stop this process by pressing CTRL + C")
    GPIO.output(GPIO_TRIGGER, True)
    try:
        while True:
            time.sleep(0.5)
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
 
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")
        GPIO.cleanup()