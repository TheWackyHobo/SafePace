import RPi.GPIO as GPIO
import time



def light():
    try:
        flashes = 0
        LIGHT_PIN = 16  # Any GPIO pin (example: GPIO 4, Pin 7)
        FREQ = 5  # Frequency in Hz
        PERIOD = 1.0 / FREQ  # Time per cycle (T = 1/f)
        HALF_PERIOD = PERIOD / 2  # Half cycle for square wave
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LIGHT_PIN, GPIO.OUT)
        while True:
            flashes += 1
            GPIO.output(LIGHT_PIN, GPIO.HIGH)  # ON
            time.sleep(HALF_PERIOD)  # Wait half-period
            GPIO.output(LIGHT_PIN, GPIO.LOW)   # OFF
            time.sleep(HALF_PERIOD)  # Wait half-period
            if (flashes == 12):
                  break
            
    except KeyboardInterrupt:
        pass  # Stop on CTRL+C

    #GPIO.cleanup()  # Reset GPIOs 

# def main():
#     light()

# if __name__ == "__main__":
#     main()
