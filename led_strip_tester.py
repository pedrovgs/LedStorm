from model import Lightning, Color
import time
from led_strip import initialize, trigger_lightning


if __name__ == "__main__":
    print("Let's start strip tester project. You can stop this process by pressing CTRL + C")
    stripes = initialize()
    lightnings = []
    for strip in stripes:
        lightnings.append(Lightning(strip, Color()))
    try:
        while True:
            trigger_lightning(lightnings)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Led strip tester closed by pressing CTRL + C")
