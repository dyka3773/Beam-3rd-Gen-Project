################################ pwm_for_servos_example.py ###################################
# Peter Halverson Nov. 1, 2014
# The LabJack U3 can output two pulse-width modulated signals.  You could use it to control
# two servo motors.
#
# PWM signal 0 comes out of the FI04 screw terminal.
# PWM signal 1 comes out of the FI05 screw terminal.  (Strange, but that's the way it is.)
#
# Documentation that allowed me to write this code is at
# http://labjack.com/support/u6/users-guide/2.9.1.1
# and in u3.py
import time

import u3
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

device = u3.U3()  # Opens first found U3 over USB
# d.configIO() # FIXME: Check if this is necessary
device.configIO(NumberOfTimersEnabled=2)
# TODO: Document what these parameters do
device.configTimerClock(
    TimerClockBase=3,
    TimerClockDivisor=1
)


# This combination selects the 48 MHz timebase.
# The PWM frequency will be 48 MHz/(15*2^16) which works out to 48.82 Hz, close to
# the 50 Hz standard for analog servos.
# Various frequencies are available.  0.06 to 732 Hz in mode 0.  15.26 to 187500 Hz in mode 1
# See the documentation.

# This example allows the LabJack U3 conrol two analog servos using PWM.
# The control signals will come out of the FIO4 and FIO5 screw terminals.
# The PWM control number can be from 0 to 65535.

# Entering 0 will cause the PWM output to be high 100% of the time.
# Entering 32768 will cause the PWM output to be high 50% of the time.
# Entering 65535 will cause the PWM output to be high almost 0% of the time.


## MUST CONNECT TO FIO5 FOR MODE 1 ##
value = 32768  # 50% duty cycle

config = u3.Timer1Config  # Timer1Config is a class

logging.info("Starting PWM at 50% duty cycle")
device.getFeedback(config(TimerMode=1, Value=value))


# Starting the motor slowly and then increasing the speed gradually until we manually set it to 100%
for i in range(0, 3):
    time.sleep(2)
    value = int(value/4)
    device.getFeedback(config(TimerMode=1, Value=value))
    logging.info(f"Value: {value}")

logging.info("Starting PWM at 100% duty cycle")
device.getFeedback(config(TimerMode=1, Value=0))

time.sleep(20)  # 20 seconds of emulsification

logging.info("Stopping PWM")
device.getFeedback(config(TimerMode=1, Value=65535))
device.close()  # Close the device
