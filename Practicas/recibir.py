import spidev
import time

spi = spidev.SpiDev() # Crear una instancia de SPI
spi.open(0, 0) # Abrir el bus SPI (bus 0, dispositivo 0)
spi.max_speed_hz = 50000

resp = spi.xfer2([0x01])
time.sleep(.1)

resp = spi.xfer2([0x00])
print("Respuesta: ", resp[0])