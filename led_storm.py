import time
from proximity_sensor import measure_distance_from_sensor
from led_stripe import trigger_lightning


MIN_DISTANCE_TO_TRIGGER_LIGHTNING = 50
SLEEP_TIME_AFTER_LIGHTNING = 3
SLEEP_TIME_WITHOUT_LIGHTNING = 0.25


def show_lightning_if_needed():
    distance = measure_distance_from_sensor()
    distance_is_too_close = 0 <= distance <= MIN_DISTANCE_TO_TRIGGER_LIGHTNING
    if distance_is_too_close:
        trigger_lightning()
    return distance_is_too_close


if __name__ == "__main__":
    print("Let's start LedStorm project. You can stop this process by pressing CTRL + C")
    try:
        while True:
            if show_lightning_if_needed():
                time.sleep(SLEEP_TIME_AFTER_LIGHTNING)
            else:
                time.sleep(SLEEP_TIME_WITHOUT_LIGHTNING)
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")
