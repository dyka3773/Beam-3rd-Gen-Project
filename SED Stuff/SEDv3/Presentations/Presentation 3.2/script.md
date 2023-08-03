## Current Status

TODO: Complete this section

## In General

- **Data Storage:** There have been some changes and refinements in the calculations of the Data Storage due to the choices of the team on the system components. Luckily these changes have been for the better and the possible Data Storage required has been reduced.
  	- The video data requirements have reached a new lower bound of 2GBs. This is due to the fact that the camera picked by the team supports a different video format than the one used in the previous calculations. The new format is potentially more efficient and requires less storage space.
 	 - The sound card data requirements have been greatly reduced from Gigabytes to Megabytes. The change has occurred by testing the sound card. We were far off in our previous calculations but the news is good.
- **Data Format:** The data format of the Sensors and the events has been updated due to the requirement of having multiple possible readers and writers. The new format is an SQLite database file, this allows us to have concurrency and multiple readers and writers. The format is also very easy to read and write from and to.
- **Flowcharts** have been updated to reflect the changes in the Timeline and the comeback of the heaters. Essentially, the only component that has been affected is the Sound Card Controller, it will now have the same timeline as the Camera Controller.
- **Microcontroller:** Since our camera doesn't support the Raspberry Pi that was in our previous plans, we have decided to use a Jetson Nano as it was suggested to us by JAI. Jetson is similar to Raspberry in many aspects so the change shouldn't pose a problem. It is here already, it arrived on tuesday but we haven't had the time to test it yet. We will start working on it asap.

## Ground Station

- GUI: The GUI was completely rebuilt using a different framework, Flask, which is more suitable for the task and Iraklis is more familiar with. The design hasn't changed significantly but the code is much more efficient and easier to maintain. 
 
We also created a tool to test it with fake data, simulating the data that will be received from the rocket. We will demonstrate it to you after the presentation during the software demo.

It is fully functional it will just need to be tied with the system that will be used to receive the data from the rocket. Until that is ready we will also make some extra improvements to some stuff that we are not happy with. The info section needs to change in every page for example, and also the Test pages need to work serially instead of waiting for the whole test to pass to display the results. Also if one thing fails the whole test should fail immediately. These are minor things that we will fix in the next few weeks.

- Telecoms: The telecom side of the ground station is still in a foundational stage. Since the team has acquired the REXUS Service Module Simulator the team will be able to test the telecomm system in a more realistic environment and development will be accelerated. We are currently in a stage of collecting our questions to send to the mentor that you suggested during the previous catch-up meeting.

## State of the Team

The state of the subteam isn't at its best.
The current members are Iraklis (Me) and Mohammed, and we are both very busy with our jobs and university responsibilities. We are trying to do our best but we are struggling.
There have been attempts to recruit new members but they have been unsuccessful.

## Task Plan

Currently we are working on the following tasks:
- Mohammed is working on the sensors reading because he already has experience with that from his bachelor thesis.
- I am working on the storage of the data on the rocket side, where I'll be following the same approach as the ground station, using an SQLite database file.
- We'll both be working on the Jetson Nano by the end of next week.
- Since the data storage is not going to take much time (I hope), I will start studying how to implement what the Electrical team has already done for the Sound Card in Python for the Jetson Nano.

## Data transmission (Hidden)

We have recently found a way to optimize the data transmission and reduce the amount of data that needs to be transmitted. The idea is to use a compression flag system where for each component state that we used to have a flag that would indicate whether the component is on or off, we will now have a cumulative flag that will indicate the state of all the components. This will reduce the amount of data that needs to be transmitted by a factor of 0.1kbit/s for the Downlink and allow the Uplink to send multiple commands packed in one command. The only downside is that the data will be less readable but is not much work to decode it.

I understand we have tasks that have higher priority so we will not work on this until we are comfortable enough time-wise.