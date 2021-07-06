import time
from led_strip import initialize, trigger_lightning


if __name__ == "__main__":
    print("Let's start LedStorm project. You can stop this process by pressing CTRL + C")
    strip = initialize()
    try:
        while True:
            trigger_lightning(strip)
            time.sleep(5)
    except KeyboardInterrupt:
        print("LedStorm closed by pressing CTRL + C")
