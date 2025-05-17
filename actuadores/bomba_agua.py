import RPi.GPIO as GPIO
import time
from config.pines_config import BOMBA_AGUA_PIN

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BOMBA_AGUA_PIN, GPIO.OUT)

def encender_bomba():
    """Enciende la bomba de agua."""
    GPIO.output(BOMBA_AGUA_PIN, GPIO.HIGH)

def apagar_bomba():
    """Apaga la bomba de agua."""
    GPIO.output(BOMBA_AGUA_PIN, GPIO.LOW)

def activar_bomba():
    """Activa la bomba de agua."""
    encender_bomba()
    print("Bomba de agua activada")

def desactivar_bomba():
    """Desactiva la bomba de agua."""
    apagar_bomba()
    print("Bomba de agua desactivada")

if __name__ == "__main__":
    try:
        while True:
            encender_bomba()
            time.sleep(5)
            apagar_bomba()
            time.sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()