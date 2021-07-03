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
    print ("Starting measure")
    # set Trigger to HIGH
    print ("Setting trigger to true")
    GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
    # set Trigger after 0.00001 = 0.01ms to LOW
    time.sleep(0.00001)
    print ("Setting trigger to false")
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)
    StartTime = time.time()
    StopTime = time.time()
    print ("Waiting for first echo value")
    # save StartTime
    while True:
            StartTime = time.time()
            if GPIO.input(GPIO_ECHO) == GPIO.HIGH:
                break
    print ("Waiting for last echo value")
    # save time of arrival
    while True:
            StopTime = time.time()
            if GPIO.input(GPIO_ECHO) == GPIO.LOW:
                break
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
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)
    try:
        while True:
            time.sleep(0.5)
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
 
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")
        GPIO.cleanup()