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

device = u3.U3()

# d.configIO() # FIXME: Check if this is necessary

device.configIO(NumberOfTimersEnabled=2)

# TODO: Document what these parameters do
device.configTimerClock(
    TimerClockBase=3,
    TimerClockDivisor=1
)

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
