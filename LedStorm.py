from ProximitySensor import measureDistanceFromSensor
from LedStrip import triggerLightning
import time

SLEEP_TIME_AFTER_LIGHTNING = 3
SLEEP_TIME_WITHOUT_LIGHTNING = 0.25
 
if __name__ == '__main__':
    print("Let's start LedStorm project. You can stop this process by pressing CTRL + C")
    try:
        while True:
            distance = measureDistanceFromSensor()
            if (distance < 50):
                triggerLightning()
                time.sleep(SLEEP_TIME_AFTER_LIGHTNING)
            else:
                time.sleep(SLEEP_TIME_WITHOUT_LIGHTNING)
 
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")