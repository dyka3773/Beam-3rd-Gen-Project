import math


def calibrate_temperature_reading(voltage_in: float):
    """Calibrates the temperature reading from the thermistor.

    Args:
        voltage_in (float): The voltage read from the thermistor.

    Returns:
        float: The calibrated temperature reading.
    """
    V_t = 5  # Vcc (power supply) voltage from LabJack

    R_k = 10000  # Thermistor's resistance

    T_0 = 298.15  # Room temperature in Kelvin

    B = 3984  # Beta value

    R_0 = 1000  # Resistance next to the thermistor in ohms

    R_measured = (voltage_in/V_t)*R_k  # Calculated resistance of thermistor

    # Final temperature in Celsius.
    therm_temp = ((T_0*B)/(B+T_0*math.log(R_measured/R_0))-273.15)

    return therm_temp


def ilias_calibrate_temperature_reading(voltage_in: float):
    """Calibrates the temperature reading from the thermistor.

    Args:
        voltage_in (float): The voltage read from the thermistor.

    Returns:
        float: The calibrated temperature reading.
    """
    # Αυτή είναι η τιμή τής (συνολικής) τάσης στο κύκλωμα τού voltage divider (Vcc (power supply)). (Εδώ είναι mock, στο πλαίσιο τού αρχικού κώδικα.)
    # Όπως αναφέρω και παρακάτω, το LabJack-LV έχει (για τη δική μας χρήση) ένα range (για ανάγνωση) 0-2,44V. Θα χρειαστεί, είτε άμεσα, είτε με κάποιον
    # (επιπλέον) divider, να δώσουμε στο κύκλωμα τού thermistor κατάλληλη τάση (Vcc) (όπως την αναφέρω και παρακάτω, 2,44V (ή πολύ κοντά, από κάτω)).
    # Εικάζω ότι θα λειτουργήσει αποδοτικά (ειδικά, εδώ, από πλευράς range και ανάλυσης(-ευαισθησίας)). Ό,τι χρειάζεται, γενικά, το αναδιαμορφώνουμε.
    V_t = 5

    # Η τιμή τής γνωστής αντίστασης στον (διπλό) voltage divider μας. (Εδώ είναι mock, στο πλαίσιο τού αρχικού κώδικα.) Γενικά, νομίζω, είναι καλό η τιμή
    # να είναι συγκρίσιμη με αυτή (τη μέση;) τού thermistor (πληροφοριακά, εδώ λαμβάνω υπόψη το ένα από τα δύο (και το τρίτο στη
    # λίστα) thermistors που έχει στα datasheets του το Electrical, το οποίο, όπως αναφέρω και παρακάτω, ανεβάζω στο archive).
    R_k = 10000

    # Τόσο είναι σε Kelvin η θερμοκρασία δωματίου, 25oC. Θερμοκρασίες Kelvin είναι αυτές που επεξεργάζεται η εξίσωση, παρακάτω.
    T_0 = 298.15

    # Η συγκεκριμένη τιμή λέγεται beta value και είναι χαρακτηριστική για κάθε thermistor. Το μοντέλο, παρακάτω, είναι ένα κοινό μοντέλο υπολογισμού τής θερμοκρασίας (τού thermistor) από την τιμή τής αντίστασής
    # του. Ας ξεκινήσουμε με αυτό και, αν χρειαστούμε βελτιώσεις, θα περάσουμε σε ένα, υπάρχει η πιθανότητα, πιο ακριβές μοντέλο (τότε, αν είναι, θα γράψω και ένα πρόγραμμα για το ανάλογο calibration, με το
    # μοντέλο εδώ δεν χρειάζεται κάποιου είδους calibration, γιατί οι τιμές που χρησιμοποιεί δίνονται συχνά (όπως και εδώ) εργοστασιακά για το εκάστοτε thermistor). Μικρή τελευταία σημείωση: χρησιμοποίησα μια
    # τιμή από τη λίστα στο datasheet, για το thermistor, που αφήνω στο archive. Επέλεξα το τρίτο από τη λίστα (γιατί πολλά από αυτά στη λίστα είχαν αυτό το beta value, οπότε το θεώρησα πιθανότερο να πέσω μέσα).
    # Αν χρειαστεί να κάνουμε κάποια αλλαγή, ανάλογα με το thermistor που αξιοποιεί το Electrical, θα το αλλάξουμε όπως χρειάζεται.
    B = 3575

    # Αυτή είναι η αντίσταση τού (τρίτου στη λίστα, όπως ανέφερα) thermistor στους 25oC.
    R_0 = 10000

    V_in = voltage_in

    # Αυτή είναι η εξίσωση, όπως υπολόγισα, για τον υπολογισμό τής αντίστασης τού thermistor από (διπλό) voltage divider. Αν υπάρχει
    # κάποιο λάθος, την αλλάζουμε.
    R_measured = (V_in/V_t)*R_k

    # Η συγκεκριμένη είναι η "Εξίσωση Β" (με beta value) που είναι μία από τις οποίες
    # χρησιμοποιούνται για την προσέγγιση θερμοκρασίας για thermistor, σύμφωνα με τη βιβλιογραφία μου.
    # Είναι μια πρώτη (ίσως και αρκετή) καλή προσέγγιση που μπορούμε να χρησιμοποιήσουμε. Αν
    # χρειαστεί κάποια αλλαγή, θα το δούμε. Η συγκεκριμένη είναι χωρίς κάποια ανάγκη για calibration,
    # οπότε είναι έτοιμη προς χρήση. Το τεστ θα δείξει και αν μάς κάνει.
    therm_temp = ((T_0*B)/(B+T_0*math.log(R_measured/R_0))-273.15)

    # Αυτή είναι η τελική μετρούμενη θερμοκρασία (τού thermistor (!) (ίσως να 'ναι σημαντική αυτή η αναφορά (για κάποιο time delay κ.λπ.))).
    return therm_temp
