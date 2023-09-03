# Software

Up next is the Software section.

# Current Status

Currently the team has Setted up the Jetson Nano, we have implemented some experiment component controllers in python, and we have succesfully read data by the Sound Card.
The things that we are currently working on are, training Katerina on the GUI, Developing the component drivers, and brainstorming on an issue with the camera that we are having.

# Non-code-development Tasks

The Jetson Nano has been set up using a microSD that Iraklis had, just to test whether everything is working correctly and to get a feel of the system.
This card is not the one that we will be using for the final product as it is only 16GB and fairly slow for our needs.
A new card has been ordered and is expected to arrive by the end of next week.
It's worth mentioning though that the Jetson Nano is working as expected and we are going to be testing the current software (Sound Card and the component controllers) on it during this week or the next.

The camera on the other side has caused us some problems.
Even though we have managed to get it working, we are having some issues with the storage size of its data.
During our tests on our Windows PC we noticed that saving video data even though it is very lightweigth in terms of size, it is very heavy in terms of processing power.
While on the other side, saving images is very light in terms of processing power, but very heavy in terms of size.
We are talking about 2.5Gbit/s which will result in about 203GBs for the 650secs of recording during the flight.
Still, we need to coduct the tests in the Jetson Nano to see how it will perform there in terms of processing power.
In order to test that though we need to get the new microSD card.
So this test is postponed for now.

# Rocket-side Code State

Let's talk about something more positive now.
The current state of the code for the rocket side is that the development of the FLIGHT MODE has started and it is going well.
The component timeline controllers for the Sensors, Heaters and the Motors have been implemented and are working as expected.
The data is Stored in an SQLite database the same way as the Ground Station does so that we can use the same code for both sides.

The current stuff that is missing are:
- The drivers for the components, except the Sound Card which is already in a very good state and there are only some minor changes/finetunings that need to be done.
- The controllers for the Sound Card and the Camera which are identical and so they will be implemented together.
- The support and check for the TEST MODE which also heavily depends on the drivers for the components and the Downlink/Uplink communication.

# Task Plan

Like we did on the IPR2, we'd also like to present our current task plan for the next weeks so that you may pose any questions or suggestions that you may have.

Currently we are working on the following tasks:
- Finishing the Sound Card and Camera controller which is lead by Iraklis
- Implementing the drivers for the Sensors which is lead by Iraklis and Mohammed
- Training Katerina on the GUI which is occupies Katerina and Iraklis
- Testing/Fixing the issue with the camera which is lead by Iraklis

Our next tasks are:
- Finishing the drivers for the Sound Card which will be lead by Iraklis in collaboration with the Science and Electronics team
- Develop the code for the Telecoms system which will be lead by Iraklis and Chrysa

And the remaining tasks as we see it are:
- Implementing the drivers for the Heaters which will probably be lead by Iraklis and Alexis
- The Camera drivers which will probably be lead by Iraklis and Mohammed
- The drivers for the Motors which will probably be lead by Mohammed
- Correcting the issues of the GUI as pointed out in the IPR2 which will be lead by Iraklis and maybe Katerina