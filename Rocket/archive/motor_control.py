import Jetson.GPIO as GPIO
from time import sleep

pin = 33				        # PWM pin connected to MCU
GPIO.setwarnings(False)			# disable warnings
GPIO.setmode(GPIO.BOARD)		# set pin numbering system
GPIO.setup(pin, GPIO.OUT)
pi_pwm = GPIO.PWM(pin, 1000)    # create PWM instance with frequency
pi_pwm.start(0)				    # start PWM of required Duty Cycle
while True:
    for duty in range(0, 101, 1):
        pi_pwm.ChangeDutyCycle(duty)  # provide duty cycle in the range 0-100
        sleep(0.01)
        print(duty)
    print("Max Voltage")
    sleep(3)

    for duty in range(100, -1, -1):
        pi_pwm.ChangeDutyCycle(duty)
        print(duty)
        sleep(0.01)
    print("Min Voltage")
    sleep(3)
