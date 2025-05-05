from gpiozero import Servo
from time import sleep
from signal import pause


servo = Servo(23)  
#sætter 
servo.mid()
sleep(1)

# Min position (0 grader – juster om nødvendigt)
servo.min()
sleep(1)

# Stop signalet – ved at sætte servoen til mid eller None (valgfrit)
servo.detach()  # Stopper PWM-signal

# Alternativt kan du lade programmet køre og holde servoen i position
# pause()  # holder programmet i gang
