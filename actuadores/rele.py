import RPi.GPIO as GPIO

class Rele:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.desactivar_rele()

    def activar_rele(self):
        """Activa el relé."""
        GPIO.output(self.pin, GPIO.HIGH)

    def desactivar_rele(self):
        """Desactiva el relé."""
        GPIO.output(self.pin, GPIO.LOW)