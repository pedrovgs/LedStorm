from ProximitySensor import measureDistanceFromSensor
from LedStrip import triggerLightning
import time

MIN_DISTANCE_TO_TRIGGER_LIGHTNING = 50
SLEEP_TIME_AFTER_LIGHTNING = 3
SLEEP_TIME_WITHOUT_LIGHTNING = 0.25
 
if __name__ == '__main__':
    print("Let's start LedStorm project. You can stop this process by pressing CTRL + C")
    try:
        while True:
            distance = measureDistanceFromSensor()
            if (distance < MIN_DISTANCE_TO_TRIGGER_LIGHTNING):
                triggerLightning()
                time.sleep(SLEEP_TIME_AFTER_LIGHTNING)
            else:
                time.sleep(SLEEP_TIME_WITHOUT_LIGHTNING)
 
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")