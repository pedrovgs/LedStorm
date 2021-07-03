import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
 
GPIO_TRIGGER = 10
GPIO_ECHO = 12
 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def measureDistanceFromSensor():
    print ("Requesting distance measure")
    triggerDistanceMeasureSignal()
    distance = readDistanceUsingTimeElapsedBetweenEchos()
    print ("Distance measured = ", distance, "cm")
    return distance

def triggerDistanceMeasureSignal():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

def readDistanceUsingTimeElapsedBetweenEchos():
    StartTime = time.time()
    StopTime = time.time()
    print ("Starting distance read")
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance