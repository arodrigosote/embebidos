import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO
LDR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)

def leer_luz_ambiental():
    """Leer el nivel de luz ambiental (LDR)."""
    pass

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