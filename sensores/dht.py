import Adafruit_DHT

# Configuración del sensor DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def leer_temperatura():
    """Leer la temperatura del sensor DHT."""
    pass

def leer_humedad_aire():
    """Leer la humedad del aire del sensor DHT."""
    pass

def leer_datos_dht():
    """Leer la temperatura y humedad del sensor DHT."""
    humedad, temperatura = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humedad, temperatura