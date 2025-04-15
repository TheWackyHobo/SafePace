import RPi.GPIO as GPIO
import time

BUTTON_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_callback(channel):
    print("Button was pushed!")

try:
    print("Press the button on GPIO 27...")
    # Add falling edge detection on the button pin with debounce
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=200)

    # Keep the script running
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.cleanup()
