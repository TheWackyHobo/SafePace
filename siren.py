import RPi.GPIO as GPIO
import time


def beep():
    try:
        beep = 0
        BUZZER_PIN = 4  # Any GPIO pin (example: GPIO 4, Pin 7)
        FREQ = 1000  # Frequency in Hz
        PERIOD = 1.0 / FREQ  # Time per cycle (T = 1/f)
        HALF_PERIOD = PERIOD / 2  # Half cycle for square wave

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUZZER_PIN, GPIO.OUT)
        while True:
            beep += 1
            for i in range(500):
                FREQ += 2
                HALF_PERIOD = (1 / FREQ) / 2
                GPIO.output(BUZZER_PIN, GPIO.HIGH)  # ON
                time.sleep(HALF_PERIOD)  # Wait half-period
                GPIO.output(BUZZER_PIN, GPIO.LOW)   # OFF
                time.sleep(HALF_PERIOD)  # Wait half-period
            for i in range(500):
                FREQ -= 2
                HALF_PERIOD = (1 / FREQ) / 2
                GPIO.output(BUZZER_PIN, GPIO.HIGH)  # ON
                time.sleep(HALF_PERIOD)  # Wait half-period
                GPIO.output(BUZZER_PIN, GPIO.LOW)   # OFF
                time.sleep(HALF_PERIOD)  # Wait half-period
            if (beep == 3):
                break
    except KeyboardInterrupt:
        pass  # Stop on CTRL+C

    GPIO.cleanup()  # Reset GPIOs 

# def main():
#     beep()
    
# if __name__ == "__main__":
#     main()