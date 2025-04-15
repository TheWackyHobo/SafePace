import RPi.GPIO as GPIO
import time
#this one works
BUTTON_PIN = 22  # GPIO pin number for the button

GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Use internal pull-up resistor

try:
    print("Press the button on GPIO 22...")
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Button pressed (pulled LOW)
            print("Button was pushed!")
            time.sleep(0.5)  # Delay to prevent multiple prints

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.cleanup()  # Clean up GPIO settings
