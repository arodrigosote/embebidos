import RPi.GPIO as GPIO
from config.pines_config import RELE_PIN

# Inicializar la instancia global del relé
rele_instance = None

def init_rele():
    global rele_instance
    if rele_instance is None:
        rele_instance = Rele(RELE_PIN)
    return rele_instance

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

def activar_rele():
    """Activa el relé."""
    rele = init_rele()
    rele.activar_rele()
    print("Relé activado")

def desactivar_rele():
    """Desactiva el relé."""
    rele = init_rele()
    rele.desactivar_rele()
    print("Relé desactivado")