import Jetson.GPIO as GPIO

## Πληροφορίες για τη βιβλιοθήκη GPIO, τού Jetson, μπορεί να βρει κανείς 
## στο: https://github.com/NVIDIA/jetson-gpio
## ΣΗΜΑΝΤΙΚΟ: ΕΙΝΑΙ ΑΠΑΡΑΙΤΗΤΟ ΝΑ ΚΑΤΕΒΑΣΟΥΜΕ ΤΗ ΒΙΒΛΙΟΘΗΚΗ ΣΤΟ JETSON, ΠΡΙΝ ΤΗΝ
## ΧΡΗΣΙΜΟΠΟΙΗΣΟΥΜΕ ΟΠΟΤΕΔΗΠΟΤΕ, ΚΑΙ ΝΑ ΚΑΝΟΥΜΕ CONFIGURE ΤΑ PERMISSIONS!

heater_1_pin = 18 
heater_2_pin = 19
## Οι τιμές, εδώ, είναι ενδεικτικές. Μόλις αποφασιστεί από το Electrical ποια pins
## χρησιμοποιούνε οι heaters, τότε και οι τιμές στις μεταβλητές heater_1_pin
## και heater_2_pin θα προσαρμοστούν αναλόγως (για τον ένα και τον άλλο heater) (ή, αν είναι
## παραπάνω τα heaters (pins), τότε τα αντίστοιχα κομμάτια τού driver πολλαπλασιάζονται
## αντιστοίχως).

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

def activate_heater(heater_pin_for_activation):
    GPIO.output(heater_pin_for_activation, GPIO.HIGH)
    ## raise NotImplementedError('This function is not implemented yet')

def deactivate_heaters(heater_pin_for_deactivation): ## Έβαλα διαφορετικά ονόματα
                                                     ## (heater_pin_for_activation και
                                                     ## heater_pin_for_deactivation, πάνω και
                                                     ## κάτω, αντίστοιχα) στις μεταβλητές των
                                                     ## δύο functions, αν και, ξέρω, δεν παίζει
                                                     ## κάποιο ρόλο, για να μην δημιουργούνται
                                                     ## μπερδέματα στην ανάγνωση τού κώδικα.
    GPIO.output(heater_pin_for_deactivation, GPIO.LOW)
    ## raise NotImplementedError('This function is not implemented yet')


## Εναλλακτικό (σαν βιβλιοθήκη που μπορεί να καλείται στο πρόγραμμα που χρειάζεται), αν θέλουμε
## να χρησιμοποιούμε τούς heaters ξεχωριστά. Προσπάθησα... (1) Δεν ξέρω, ακριβώς, αν το έκανα
## σωστά. (2) Δεν ξέρω, αν χρειάζεται, οπότε (γι'αυτό έβαλα και τα comments) θα ρωτούσα και τον
## Ηρακλή και, αν χρειαζόταν, κιόλας, το Electrical.
##
## import Jetson.GPIO as GPIO
##
## class HeaterDriver:
##    def __init__(self, heater_1_pin, heater_2_pin):
##        self.heater_1_pin = heater_1_pin
##        self.heater_2_pin = heater_2_pin
##        self.setup_heaters()
##
##    def setup_heaters(self):
##        GPIO.setmode(GPIO.BCM)
##        GPIO.setup(self.heater_1_pin, GPIO.OUT)
##        GPIO.setup(self.heater_2_pin, GPIO.OUT)
##
##    def activate_heater_1(self):
##        GPIO.output(self.heater_1_pin, GPIO.HIGH)
##
##    def activate_heater_2(self):
##        GPIO.output(self.heater_2_pin, GPIO.HIGH)
##
##    def deactivate_heater_1(self):
##        GPIO.output(self.heater_1_pin, GPIO.LOW)
##
##    def deactivate_heater_2(self):
##        GPIO.output(self.heater_2_pin, GPIO.LOW)
##
##    Παρακάτω, για μια πιο compact χρήση τού driver. Μπορεί η επιρρέπειά του σε σφάλματα να την κάνει χειρότερη,
##    αντί για μια πιο αναλυτική, αλλά straightforward χρήση.
##
##    def activate_heater(self, h):
##        if h = self.heater_1_pin:
##            activate_heater_1()
##        elif h = self.heater_2_pin:  ## Ή else, εφόσον υπάρχει καλή συγγραφή τού κυρίως κώδικα (όπως εξηγώ και κάτω).
##                                     ## (Δίνει η elif περισσότερη ασφάλεια;)
##        ##
##            activate_heater_2()
##        ## Έχει νόημα να κάνουμε κάποια διαδικασία αποσφαλμάτωσης; Προσωπικά, θεωρώ, ότι εφόσον κάνουμε
##        ## καλή εκχώρηση στο κυρίως πρόγραμμα, όπου χρειάζεται ο έλεγχος των heaters, και προσοχή σε συντακτικά,
##        ## δεν θα είναι τόσο κρίσιμη και, έτσι, κρίσιμη η αποσφαλμάτωση. (Το ίδιο, για την αποσφαλμάτωση, ισχύει
##        ## και παρακάτω.)
##
##    def deactivate_heater(self, h):
##        if h = self.heater_1_pin:
##            deactivate_heater_1()
##        elif h = self.heater_2_pin:  ## Ή else (όπως και πάνω).
##            deactivate_heater_2()


## Example usage
##
## import time
## from heater_driver import heater_1_pin, heater_2_pin as h1, h2
##
## try:
##    activate_heater(h1)
##    time.sleep(10)  # Run heater 1 for 10 seconds, before activating heater 2 and
##                    # deactivating heater 1.
##    activate_heater(h2)
##    deactivate_heater(h1) # Activate heater 2 and deactivate heater 1.
##    time.sleep(20) # Run heater 2 for 20 seconds, before deactivating it also.
##    deactivate_heater(h2) # Deactivating heater 2.
##
##    ## Μπορούμε να κάνουμε κι άλλες τροποποιήσεις (το ίδιο ισχύει και στο παράδειγμα με τη
##    ## βιβλιοθήκη, παραπάνω), αν χρειάζεται, όπως να δημιουργήσουμε συναρτήσεις
##    ## activate_heaters και deactivate_heaters, π.χ., για να έλέγξουμε τούς δύο heaters
##    ## ταυτόχρονα (αν, για παράδειγμα, δεν μάς φτάνει η συχνότητα τού Jetson) κ.λπ., αλλά,
##    ## απ' ό,τι καταλαβαίνω, δεν μάς χρειάζεται κάτι παραπάνω.
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
