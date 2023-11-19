import Jetson.GPIO as GPIO

LO_pin = 26
SOE_pin = 27
SODS_pin = 28   ## Mock values here...

GPIO.setmode(BCM)

GPIO.setup(LO_pin, GPIO.IN)
GPIO.setup(SOE_pin, GPIO.IN)
GPIO.setup(SODS_pin, GPIO.IN)

def rocket_signal():
  signal = "initialising_string"
  
  LO_pin_state = GPIO.input(LO_pin)
  SOE_pin_state = GPIO.input(SOE_pin)
  SODS_pin_state = GPIO.input(SODS_pin)

  if LO_pin_state == GPIO.HIGH:
    signal = "LO"

  if SOE_pin_state == GPIO.HIGH:
    signal = "SOE"

  if SODS_pin_state == GPIO.HIGH:
    signal = "SODS"

  GPIO.cleanup()  ## Don't really know how to use this method. I saw it widely used (and understood that it's useful to
                  ## re-initialise GPIO pins' states, but don't know when it's needed, dangers of leaving GPIO pins' states 
                  ## as they were and whatnot...) and included that in my code. Lastly, in my estimation, running 
                  ## GPIO.cleanup() in each one of our GPIO utilising modules, snippets etc. would possibly mess with the 
                  ## overall GPIO setup, which might be dangerous because it is not singly used (by one module, system etc.)
                  ## but, if I consider it rightly, concurrently, very likely, by multiple parts and ends of our entire 
                  ## experiment's software system.

  return signal



##  or
##
##
##  def rocket_signal():
##    signal="initialising_string"
##  
##    LO_pin_state=GPIO.input(LO_pin)
##    if LO_pin_state==GPIO.HIGH:
##      signal="LO"
##
##    SOE_pin_state=GPIO.input(SOE_pin)
##    if SOE_pin_state==GPIO.HIGH:
##      signal="SOE"
##
##    SODS_pin_state=GPIO.input(SODS_pin)
##    if SODS_pin_state==GPIO.HIGH:
##      signal="SODS"
##
##    GPIO.cleanup()
##
##    return signal
##
##
##  or
##
##
##  def read_signals_pins:
##    LO_pin_state=GPIO.input(LO_pin)
##    SOE_pin_state=GPIO.input(SOE_pin)
##    SODS_pin_state=GPIO.input(SODS_pin)
##  
##    return LO_pin_state, SOE_pin_state, SODS_pin_state
##
##  def rocket_signal():
##    signal="initialising_string"
##
##    read_signals_pins()
##  
##    if (LO_pin_state==GPIO.HIGH && SOE_pin_state==GPIO.LOW && SODS_pin_state==GPIO.LOW):
##      signal="LO"
##
##    if (LO_pin_state==GPIO.LOW && SOE_pin_state==GPIO.HIGH && SODS_pin_state==GPIO.LOW):
##      signal="SOE"
##
##    if (LO_pin_state==GPIO.LOW && SOE_pin_state==GPIO.LOW && SODS_pin_state==GPIO.HIGH):
##      signal="SODS"
##
##    GPIO.cleanup()
##
##    return signal
##
##
##  or ... (My main, maybe somewhat anxiously driven, concerns were in regard to execution time (time needed between code actions
##         and how it could affect good (time-wise, I thought) parameterising of the conditions and, thus, seamless function of 
##         the application code for its signal reporting purposes (say, (time) trustworthiness)) and condition collision issues. 
##         These have driven my alternative implementations in the above comments. Other forms of implementation, regarding 
##         various concerns and parameters to keep in mind, could be, timely, discussed. Though, if such an implementation as 
##         above (even the first, to be truthful) is enough for our needs, we could very well go on with that version.)
