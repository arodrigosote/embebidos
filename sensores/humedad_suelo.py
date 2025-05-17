import Adafruit_DHT
import spidev
import time
from config.pines_config import HUMEDAD_SUELO_CANAL_ADC, DHT_PIN

# Configurar SPI para lectura analógica
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 50000

def leer_canal_analogico(canal):
    """Lee un valor desde el canal especificado del ADC MCP3008."""
    # MCP3008 protocolo: 3 bytes: start bit, config, y dummy byte para recibir datos
    adc = spi.xfer2([1, (8 + canal) << 4, 0])
    # Extraer los 10 bits del resultado (2º byte y 3er byte)
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def leer_humedad_suelo():
    """Leer el valor de humedad del suelo."""
    # Leer desde el canal configurado
    valor = leer_canal_analogico(HUMEDAD_SUELO_CANAL_ADC)
    # Convertir a porcentaje: 0-1023 -> 0-100%
    # Invertido ya que normalmente 0 significa "seco" y 1023 "mojado"
    porcentaje = 100 - (valor * 100 / 1023)
    return round(porcentaje, 2)

def leer_humedad_temperatura():
    """Leer la humedad y temperatura del sensor DHT11."""
    humedad, temperatura = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
    return humedad, temperatura