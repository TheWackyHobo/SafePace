import RPi.GPIO as GPIO
import time

GPIOpin = 12
dutyCycle = 0

# set pin assignment mode
GPIO.setmode(GPIO.BCM)

# set up pin I/O
GPIO.setup(GPIOpin, GPIO.OUT)

# configure pwm channel
pwm = GPIO.PWM(GPIOpin,1000) # PWM(pin, frequency)

# pwm control
pwm.start(dutyCycle)  # start(duty_cycle)
def motor (distance):
    dutyCycle = 100 - (distance / 84 * 100)
    pwm.ChangeDutyCycle(dutyCycle)
    #print("Running PWM at:"+str(dutyCycle)+"\n\n\n")
    time.sleep(1)
    #pwm.stop()
    #print("Stopping PWM output")
    #GPIO.cleanup()

#distance = 20
#motor(distance)

