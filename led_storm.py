import random
import time
from proximity_sensor import measure_distance_from_sensor
from led_strip import initialize, trigger_lightning
from model import Color, Lightning


MIN_DISTANCE_TO_TRIGGER_LIGHTNING = 50
SLEEP_TIME_BETWEEN_READS = 1


def show_lightning_if_needed(stripes):
    distance = measure_distance_from_sensor()
    distance_is_too_close = distance <= MIN_DISTANCE_TO_TRIGGER_LIGHTNING
    if distance_is_too_close:
        lightnings = []
        for strip in stripes:
            random_color = generate_random_color()
            lightnings.append(Lightning(strip, random_color))
        trigger_lightning(lightnings)
    return distance_is_too_close


def generate_random_color():
    return Color(
        random.randint(
            0, 255), random.randint(
            0, 255), random.randint(
                0, 255))


if __name__ == "__main__":
    print("Let's start LedStorm project. You can stop this process by pressing CTRL + C")
    led_stripes = initialize()
    try:
        while True:
            if show_lightning_if_needed(led_stripes):
                print("Thunder shown! -------->------>------>")
            time.sleep(SLEEP_TIME_BETWEEN_READS)
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")
