Software
# Current Status

Currently the team has Setted up the final version of the Jetson Nano, we have finalized the component controllers in python, and we have successfully read data by the Sound Card in the Jetson Nano.
The things that we are currently working on are, developing the component drivers (mainly the sensors and the heaters), developing the Telecoms system, and setting up the SDK for the camera so that we can start developing the camera drivers and test how the data will be saved.

# Non-code-development Tasks

We have bought a new microSD card for the Jetson Nano, and we have setted up the final version of the Jetson Nano. It will be used for the final experiment.
The current rocket-side code requirements have been installed on the Jetson Nano, and the code has been tested on it.
The only thing that is not installed on the Jetson Nano is the SDK for the camera, Iraklis has already done some work on it and accoring to him 2-4 hours of work are left to be done on it. We need this SDK in order to test how the data will be saved and how much processing power will be needed for the camera. Once the SDK is installed we will try to record a short video in MP4 format and see how the Jetson Nano will perform. Iraklis says that by the time the camera setup is ready, this test shouldn't be difficult to perform since there are already some examples on how to do it.

# Rocket-side Code State

As for the rocket-side code, the component controllers have been implemented and are working as expected in Flight Mode. The Sound Card driver is ready and has already been tested successfully on the Jetson Nano with a small preliminary test where Iraklis was changing the voltage by short-circuiting the inputs and verifying that the data was changing accordingly. The heater controllers have also been decoupled and seperated so that the cell and the electronics box can be heated seperately. This was performed in accordance to the feedback of the Mechanical and Electronics teams.
The current stuff that is missing are:
- The drivers for the Motor, Heaters, Sensors and Camera. But the ones for the Camera and the Sensors are being under research and development.
- The support and check for the TEST MODE which also heavily depends on the drivers for the components and the Telecoms system.
- The Telecoms system which is under development as mentioned earlier.

# Task Plan

I think that the task plan that present on each meeting is helpful for everyone to know what we are currently working on and what we are planning to do next. So I will present it here as well.
Currently we are working on the following tasks:
- Finishing the Camera Setup and Drivers which is lead by Iraklis,
- Researching what should be done for the Camera Data in case of a failure which is lead by Iraklis,
- Working on the Telecoms system which is lead by Iraklis and Chrysa,
- And trying to recruit a possible temporary member for our subteam which is lead by Iraklis and Konstantina.

We have paused the task where Iraklis was training Katerina on the GUI since we have decided that it would be better if he focused on the rocket-side and telecoms system for now. We will resume this task once some progress has been made and Iraklis has more time to spare.

Our next tasks are:
- Implementing the Motor drivers since the motor has arrived which will be lead by Iraklis,
- Implementing the Heaters drivers which will probably be lead by Iraklis and Alexis,
- Implementing the Sensor drivers which will be lead by Iraklis,

And the only remaining task as we see it are:
- Correcting the issues of the GUI as pointed out in the IPR2 which will be lead by Iraklis and maybe Katerina.