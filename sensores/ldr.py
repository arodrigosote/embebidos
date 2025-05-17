import RPi.GPIO as GPIO
import time
from config.pines_config import LDR_PIN

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)

def leer_luz_ambiental():
    """Leer el nivel de luz ambiental (LDR)."""
    # Implementación basada en la medición de tiempo de carga/descarga del condensador
    # Se usa un enfoque digital para el LDR
    if GPIO.input(LDR_PIN):
        return 100  # Alto nivel de luz (día)
    else:
        return 0    # Bajo nivel de luz (noche)

def main():
    try:
        while True:
            luz = leer_luz_ambiental()
            print(f"Nivel de luz: {luz}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programa terminado.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()