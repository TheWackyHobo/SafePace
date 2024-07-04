import RPi.GPIO as GPIO
import time

GPIOpin = 12
dutyCycle = 0
def motor(distance):
    # set pin assignment mode

    dutyCycle = 100 - (distance / 84 * 100)
    GPIO.setmode(GPIO.BCM)

    # set up pin I/O
    GPIO.setup(GPIOpin, GPIO.OUT)

    # configure pwm channel
    pwm = GPIO.PWM(GPIOpin,1000) # PWM(pin, frequency)

    # pwm control
    pwm.start(dutyCycle)  # start(duty_cycle)
    print("Running PWM at:"+str(dutyCycle))
    time.sleep(1)
    #pwm.stop()
    #print("Stopping PWM output")
    GPIO.cleanup()

#distance = 75
#motor(distance)

