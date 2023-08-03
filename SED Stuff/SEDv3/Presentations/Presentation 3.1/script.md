## General Stuff

- Data Storage: There have been some changes and refinements in the calculations of the Data Storage due to the choices of the team on the system components. Luckily these changes have been for the better and the possible Data Storage has been reduced.
  - The video data requirements have reached a new lower bound of 2GBs. This is due to the fact that the camera picked by the team supports a different video format than the one used in the previous calculations. The new format is potentially more efficient and requires less storage space.
  - The sound card data requirements have been greatly reduced from Gigabytes to Megabytes. The change has occurred by testing the sound card. We were far off in our previous calculations but the news is good.
- Flowcharts have been updated to reflect the changes in the Timeline and the comeback of the heaters. Essentially, the only component that has been affected is the Sound Card Controller, it will now have the same timeline as the Camera Controller.
- Microcontroller: Since our camera doesn't support the Raspberry Pi that was in our previous plans, we have decided to use a Jetson Nano as it was suggested to us by JAI. Jetson is similar to Raspberry in many aspects so the change shouldn't pose a problem.

## Ground Station

- GUI: The GUI is almost ready and fully functional. It needs some more tests with data being created live but other than that it is ready to be used and integrated with the rest of the system.

It was rebuilt using a different framework, Flask, which is more suitable for the task and Iraklis is more familiar with. The design hasn't changed significantly but the code is much more efficient and easier to maintain.

We could show you some screenshots of the GUI after the presentation if you are interested.

- Telecoms: The telecom side of the ground station is still in a foundational stage. Since the team has acquired the REXUS Service Module Simulator the team will be able to test the telecomm system in a more realistic environment and development will be accelerated.

## State of the Team

The state of the subteam is not good. Iraklis is the only one who's available to work and even his schedule is very crowded. There have been attempts to recruit new members but they have been unsuccessful. The subteam is in a very bad situation and we are not sure how to proceed, please advise.

## Data transmission (Hidden)

We have recently found a way to optimize the data transmission and reduce the amount of data that needs to be transmitted. The idea is to use a compression flag system where for each component state that we used to have a flag that would indicate whether the component is on or off, we will now have a cumulative flag that will indicate the state of all the components. This will reduce the amount of data that needs to be transmitted by a factor of 0.1kbit/s for the Downlink and allow the Uplink to send multiple commands packed in one command. The only downside is that the data will be less readable but is not much work to decode it.

I understand we have tasks that have higher priority so we will not work on this until we are comfortable enough time-wise.