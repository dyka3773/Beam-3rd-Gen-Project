import Jetson.GPIO as GPIO

## Πληροφορίες για τη βιβλιοθήκη GPIO, τού Jetson, μπορεί να βρει κανείς 
## στο: https://github.com/NVIDIA/jetson-gpio
## ΣΗΜΑΝΤΙΚΟ: ΕΙΝΑΙ ΑΠΑΡΑΙΤΗΤΟ ΝΑ ΚΑΤΕΒΑΣΟΥΜΕ ΤΗ ΒΙΒΛΙΟΘΗΚΗ ΣΤΟ JETSON, ΠΡΙΝ ΤΗΝ
## ΧΡΗΣΙΜΟΠΟΙΗΣΟΥΜΕ ΟΠΟΤΕΔΗΠΟΤΕ, ΚΑΙ ΝΑ ΚΑΝΟΥΜΕ CONFIGURE ΤΑ PERMISSIONS!

heater_1_pin = as_epileksei_to_electrical_1
heater_2_pin = as_epileksei_to_electrical_2
## as_epileksei_to_electrical_1 και as_epileksei_to_electrical_2 είναι τα pins (int, αν έχει
## κάποια σημασία) (ή, αν είναι παραπάνω τα heaters (pins), τότε τα αντίστοιχα κομμάτια τού
## driver πολλαπλασιάζονται αντιστοίχως)

GPIO.setmode(GPIO.BCM) ## Ίσως, το συγκεκριμένο, όπως και παρακάτω είναι από τα μόνα που πρέπει
                       ## να κοιτάξουμε, αν δημιουργείται πρόβλημα, γιατί, απ' ό,τι κατάλαβα,
                       ## έχει να κάνει με το σύστημα αρίθμησης των GPIO pins. Οτιδήποτε
                       ## παραπάνω, επειδή έριξα μια ματιά στο documentation τής βιβλιοθήκης,
                       ## πιθανότατα θα μπορεί να βρεθεί σ' αυτό (το documentation). Βλέπουμε...
                       ## Ας γίνει ένα, τουλάχιστον, καλό testing, τώρα, όσο πιο άμεσα γίνεται,
                       ## για να περάσουμε, αν χρειαστεί, και γρήγορα σε βελτιώσεις ή όποιες
                       ## αλλαγές.
##
GPIO.setup(heater_1_pin, GPIO.OUT)
GPIO.setup(heater_2_pin, GPIO.OUT)

def activate_heaters():
    GPIO.output(heater_1_pin, GPIO.HIGH)
    GPIO.output(heater_2_pin, GPIO.HIGH)
    ## raise NotImplementedError('This function is not implemented yet')

def deactivate_heaters():
    GPIO.output(heater_1_pin, GPIO.LOW)
    GPIO.output(heater_2_pin, GPIO.LOW)
    ## raise NotImplementedError('This function is not implemented yet')

## Εναλλακτικό (σαν βιβλιοθήκη που μπορεί να καλείται στο πρόγραμμα που χρειάζεται), αν θέλουμε
## να χρησιμοποιούμε τούς heaters ξεχωριστά. Προσπάθησα... (1) Δεν ξέρω, ακριβώς, αν το έκανα
## σωστά. (2) Δεν ξέρω, αν χρειάζεται, οπότε (γι'αυτό έβαλα και τα comments) θα ρωτούσα και τον
## Ηρακλή και, αν χρειαζόταν, κιόλας, το Electrical.
##
## import Jetson.GPIO as GPIO
##
## class HeaterDriver:
##    def __init__(self, heater_pin):
##        self.heater_pin = heater_pin
##        self.setup_heater()
##
##    def setup_heater(self):
##        GPIO.setmode(GPIO.BCM)
##        GPIO.setup(self.heater_pin, GPIO.OUT)
##
##    def activate_heater(self):
##        GPIO.output(self.heater_pin, GPIO.HIGH)
##
##    def deactivate_heater(self):
##        GPIO.output(self.heater_pin, GPIO.LOW)



## Example usage
##
## import time
##
## try:
##    activate_heaters()
##    time.sleep(10)  # Run heater for 10 seconds
##    deactivate_heaters()
##
## except KeyboardInterrupt:
##    GPIO.cleanup()  # Cleanup GPIO on keyboard interrupt
##
## GPIO.cleanup()  # Cleanup GPIO when done

## or

## from heater_driver import HeaterDriver
##
## heater_1_pin = 18
##
## heater_1 = HeaterDriver(heater_1_pin)
##
## heater_1.activate_heater()
##
## ...
##
## heater_1.deactivate_heater()
##
## ...
##
## GPIO.cleanup()
