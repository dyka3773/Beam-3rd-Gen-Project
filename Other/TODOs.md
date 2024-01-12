# Things to do

## Ground Station

- [X] Decouple the info section so that it presents the same data everywhere without having to copy paste the code. (Have a single source of truth)
- [ ] Modify the Ground Station README to have a "How to use" section and run it by someone who has never used it before.
- [X] Present everything in a single window:
  - [X] "Health" monitoring indicators (e.g. power is received, camera is on/off, LEDs are on/off, …) to indicate that the experiment is working properly.
  - [X] Indicators showing which rocket signals (LO, SODS, SOE) have been received.
- [X] Add a Receiver that runs on the ground station and receives the data from the rocket.


## Rocket

- [X] Make sure that every event that is after liftoff is taking into account whether the LO signal has been received or not at some point in time.
- **Maybe** also have a config file that says whether we should run the motor or not (for testing purposes).
- [X] Shift the motor timeline +13secs to the right
- [X] Shift the end to the timeline and Power off earlier because there will be a landing much earlier than expected. Also consult with the team and previous experiment data to see when the power should be turned off and when the landing is expected to happen.
- [ ] Calibrate thermistor values (Offloaded some work to @KonstadinaN)
- [ ] Rocket signal recognition testing or change of pins