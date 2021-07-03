import time
from proximity_sensor import measure_distance_from_sensor
from led_strip import trigger_lightning


MIN_DISTANCE_TO_TRIGGER_LIGHTNING = 50
SLEEP_TIME_AFTER_LIGHTNING = 3
SLEEP_TIME_WITHOUT_LIGHTNING = 0.25

if __name__ == "__main__":
    print("Let's start LedStorm project. You can stop this process by pressing CTRL + C")
    try:
        while True:
            distance = measure_distance_from_sensor()
            if distance < MIN_DISTANCE_TO_TRIGGER_LIGHTNING:
                trigger_lightning()
                time.sleep(SLEEP_TIME_AFTER_LIGHTNING)
            else:
                time.sleep(SLEEP_TIME_WITHOUT_LIGHTNING)

    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")
