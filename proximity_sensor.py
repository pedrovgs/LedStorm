import time
from RPi import GPIO

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 10
GPIO_ECHO = 12

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def measure_distance_from_sensor():
    print("Requesting distance measure")
    trigger_distance_measure_signal()
    distance = read_distance_using_time_elapsed_between_echos()
    print("Measured Distance = %.1f cm" % distance)
    return distance


def trigger_distance_measure_signal():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)


def read_distance_using_time_elapsed_between_echos():
    start_time = time.time()
    stop_time = time.time()
    print("Starting distance read")
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    TimeElapsed = stop_time - start_time
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance