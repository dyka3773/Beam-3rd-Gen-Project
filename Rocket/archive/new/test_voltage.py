import RPi.GPIO as GPIO
from time import sleep

pin = 33				        # PWM pin connected to MCU
GPIO.setwarnings(False)			# disable warnings
GPIO.setmode(GPIO.BOARD)		# set pin numbering system
GPIO.setup(pin,GPIO.LOW)
#pi_pwm = GPIO.PWM(pin, 1000)    # create PWM instance with frequency
#pi_pwm.start(0)				    # start PWM of required Duty Cycle













