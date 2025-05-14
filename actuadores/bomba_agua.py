import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def encender_bomba():
    """Enciende la bomba de agua."""
    GPIO.output(18, GPIO.HIGH)

def apagar_bomba():
    """Apaga la bomba de agua."""
    GPIO.output(18, GPIO.LOW)

def activar_bomba():
    """Activa la bomba de agua."""
    pass

def desactivar_bomba():
    """Desactiva la bomba de agua."""
    pass

if __name__ == "__main__":
    try:
        while True:
            encender_bomba()
            time.sleep(5)
            apagar_bomba()
            time.sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()