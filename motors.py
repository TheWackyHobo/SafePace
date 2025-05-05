import RPi.GPIO as GPIO
import time

GPIOpin = 13
dutyCycle = 0
gpiopin_left = 5
gpio_right = 12

# set pin assignment mode
GPIO.setmode(GPIO.BCM)

# set up pin I/O
GPIO.setup(GPIOpin, GPIO.OUT)
GPIO.setup(gpiopin_left, GPIO.OUT)
GPIO.setup(gpio_right, GPIO.OUT)

# configure pwm channel
pwm = GPIO.PWM(GPIOpin,1000) # PWM(pin, frequency)
left = GPIO.PWM(gpiopin_left,1000) # PWM(pin, frequency)
right = GPIO.PWM(gpio_right,1000)


# pwm control
pwm.start(dutyCycle)  # start(duty_cycle)
left.start(dutyCycle)
right.start(dutyCycle)
def motor (distance, sensor):
    dutyCycle = 100 - (distance / 84 * 100)
    if (sensor == 0x71):
        left.ChangeDutyCycle(dutyCycle)

    if (sensor == 0x70):
        pwm.ChangeDutyCycle(dutyCycle)

    if (sensor == 0x72):
        right.ChangeDutyCycle(dutyCycle)
    #print("Running PWM at:"+str(dutyCycle)+"\n\n\n")
   # print(f"Motor {hex(sensor)} virating")
    time.sleep(.3)
    #pwm.stop()
    #print("Stopping PWM output")
    #GPIO.cleanup()

#distance = 20
#motor(distance)
