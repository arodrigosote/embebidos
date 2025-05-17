import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, device 0 (CE0)
spi.max_speed_hz = 50000

def get_temp():
    response = spi.xfer2([1])  # 1 para pedir temperatura
    return response[0]

def get_humidity():
    response = spi.xfer2([2])  # 2 para pedir humedad
    return response[0]

try:
    while True:
        temp = get_temp()
        hum = get_humidity()
        print(f"FSE 2025-2 BRIGADA 02 GRUPO 06, TEMPERATURA {temp}°C")
        time.sleep(3)
except KeyboardInterrupt:
    spi.close()