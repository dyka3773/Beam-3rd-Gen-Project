import Jetson.GPIO as GPIO

# Πληροφορίες για τη βιβλιοθήκη GPIO, τού Jetson, μπορεί να βρει κανείς
# στο: https://github.com/NVIDIA/jetson-gpio

# ΣΗΜΑΝΤΙΚΟ: ΕΙΝΑΙ ΑΠΑΡΑΙΤΗΤΟ ΝΑ ΚΑΤΕΒΑΣΟΥΜΕ ΤΗ ΒΙΒΛΙΟΘΗΚΗ ΣΤΟ JETSON, ΠΡΙΝ ΤΗΝ
# ΧΡΗΣΙΜΟΠΟΙΗΣΟΥΜΕ ΟΠΟΤΕΔΗΠΟΤΕ, ΚΑΙ ΝΑ ΚΑΝΟΥΜΕ CONFIGURE ΤΑ PERMISSIONS!

heater_1_pin = 18  # TODO: Speak with Electrical team about the pins numbers.
heater_2_pin = 19


GPIO.setmode(GPIO.BOARD)
# Ίσως, το συγκεκριμένο, όπως και παρακάτω είναι από τα μόνα που πρέπει
# να κοιτάξουμε, αν δημιουργείται πρόβλημα, γιατί, απ' ό,τι κατάλαβα,
# έχει να κάνει με το σύστημα αρίθμησης των GPIO pins. Οτιδήποτε
# παραπάνω, επειδή έριξα μια ματιά στο documentation τής βιβλιοθήκης,
# πιθανότατα θα μπορεί να βρεθεί σ' αυτό (το documentation). Βλέπουμε...
# Ας γίνει ένα, τουλάχιστον, καλό testing, τώρα, όσο πιο άμεσα γίνεται,
# για να περάσουμε, αν χρειαστεί, και γρήγορα σε βελτιώσεις ή όποιες
# αλλαγές.
GPIO.setup(heater_1_pin, GPIO.OUT)
GPIO.setup(heater_2_pin, GPIO.OUT)


def activate_heater(heater_pin_for_activation):
    """???

    Args:
        heater_pin_for_activation (int): The number of the pin to be activated.
    """
    GPIO.output(heater_pin_for_activation, GPIO.HIGH)


def deactivate_heaters(heater_pin_for_deactivation: int):
    """Έβαλα διαφορετικά ονόματα (heater_pin_for_activation και heater_pin_for_deactivation, 
    πάνω και κάτω, αντίστοιχα) στις μεταβλητές των δύο functions, αν και, ξέρω, δεν παίζει κάποιο ρόλο, 
    για να μην δημιουργούνται μπερδέματα στην ανάγνωση τού κώδικα.

    Args:
        heater_pin_for_deactivation (int): The number of the pin to be deactivated.
    """
    GPIO.output(heater_pin_for_deactivation, GPIO.LOW)
