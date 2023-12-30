# Things to do

## Ground Station

- [ ] Decouple the info section so that it presents the same data everywhere without having to copy paste the code. (Have a single source of truth)
- [ ] Modify the Ground Station README to have a "How to use" section and run it by someone who has never used it before.
- [ ] Present everything in a single window:
  - [ ] "Health" monitoring indicators (e.g. power is received, camera is on/off, LEDs are on/off, …) to indicate that the experiment is working properly.
  - [ ] Indicators showing which rocket signals (LO, SODS, SOE) have been received.


## Rocket

- [ ] Make sure that every event that is after liftoff is taking into account whether the LO signal has been received or not at some point in time.