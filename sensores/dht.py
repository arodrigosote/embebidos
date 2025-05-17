import Adafruit_DHT
from config.pines_config import DHT_PIN, DHT_SENSOR_TYPE

# Configuración del sensor DHT
DHT_SENSOR = DHT_SENSOR_TYPE  # Obtenido de pines_config.py

def leer_temperatura():
    """Leer la temperatura del sensor DHT."""
    humedad, temperatura = leer_datos_dht()
    if temperatura is not None:
        return round(temperatura, 2)
    return 0.0

def leer_humedad_aire():
    """Leer la humedad del aire del sensor DHT."""
    humedad, temperatura = leer_datos_dht()
    if humedad is not None:
        return round(humedad, 2)
    return 0.0

def leer_datos_dht():
    """Leer la temperatura y humedad del sensor DHT."""
    humedad, temperatura = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humedad, temperatura