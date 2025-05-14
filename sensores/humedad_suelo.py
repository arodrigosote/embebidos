import Adafruit_DHT

# Configuración del sensor de humedad del suelo
SENSOR_PIN = 4

def leer_humedad_suelo():
    """Leer el valor de humedad del suelo."""
    pass

def leer_humedad_temperatura():
    """Leer la humedad y temperatura del sensor DHT11."""
    humedad, temperatura = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, SENSOR_PIN)
    return humedad, temperatura