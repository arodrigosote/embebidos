import RPi.GPIO as GPIO
from config.pines_config import VENTILADOR_PIN

# Inicialización del GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(VENTILADOR_PIN, GPIO.OUT)

def activar_ventilador():
    """Activa el ventilador."""
    GPIO.output(VENTILADOR_PIN, GPIO.HIGH)
    print("Ventilador activado")

def desactivar_ventilador():
    """Desactiva el ventilador."""
    GPIO.output(VENTILADOR_PIN, GPIO.LOW)
    print("Ventilador desactivado")