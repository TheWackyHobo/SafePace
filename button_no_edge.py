import RPi.GPIO as GPIO
import time

def was_button_pressed(pin=22, wait_time=0.5):
    """
    Waits for a short duration and checks if the button on the given pin was pressed.
    
    Args:
        pin (int): GPIO pin using BCM numbering.
        wait_time (float): Seconds to wait before checking.

    Returns:
        bool: True if button was pressed, False otherwise.
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        #print(f"You have {wait_time} seconds to press the button...")
        time.sleep(wait_time)
        pressed = GPIO.input(pin) == GPIO.LOW
       # if pressed:
            #print("Button was pushed!")
            
        #else:
            #print("Button not pressed.")
        return pressed
    finally:
        #GPIO.cleanup()
        return pressed

# Example call
#button_was_pressed = was_button_pressed()
#print("Returned:", button_was_pressed)
