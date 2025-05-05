from gpiozero import AngularServo
from time import sleep

# Angiv GPIO-pinnen, som servoens signalledning er tilsluttet
servo = AngularServo(17, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0024)

while True:
    servo.angle = 0    # Flyt til 0 grader
    print("Position: 0°")
    sleep(1)

    servo.angle = 90   # Flyt til 90 grader
    print("Position: 90°")
    sleep(1)

    servo.angle = 180  # Flyt til 180 grader
    print("Position: 180°")
    sleep(1)