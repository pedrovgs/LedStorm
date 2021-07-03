#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 5
GPIO_ECHO = 6
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    print ("Starting measure process")
    # set Trigger to LOW
    GPIO.output(GPIO_TRIGGER, False)
    print ("Trigger pin set to false")
    time.sleep(0.00002)
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    print ("Trigger pin set to true")
    # set Trigger after 0.05ms to LOW
    time.sleep(0.00005)
    GPIO.output(GPIO_TRIGGER, False)
    print ("Trigger pin set to false")
    StartTime = time.time()
    StopTime = time.time()
    print ("Waiting for first echo value")
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    print ("Waiting for last echo value")
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    print ("Waiting echo value received")
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    print ("Meassure process finished with distance = %.1f cm" % distance)
    return distance
 
if __name__ == '__main__':
    print("Let's start LedStorm project. You can stop this process by pressing CTRL + C")
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")
        GPIO.cleanup()