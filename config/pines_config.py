"""
Configuración centralizada de los pines GPIO de la Raspberry Pi 4 
para el sistema de control de invernadero.

Este archivo define todos los pines utilizados por los diferentes 
componentes del sistema, facilitando la modificación y el mantenimiento.
"""
import Adafruit_DHT

# ---- SENSORES ----
# Sensor de humedad del suelo (ADC a través de SPI)
# SPI utiliza los pines: 
# - MOSI: GPIO10 (Pin físico 19)
# - MISO: GPIO9 (Pin físico 21)
# - SCLK: GPIO11 (Pin físico 23)
# - CE0: GPIO8 (Pin físico 24)
HUMEDAD_SUELO_CANAL_ADC = 0  # Canal 0 del ADC MCP3008

# Sensor DHT (temperatura y humedad del aire)
DHT_PIN = 4  # GPIO4 (Pin físico 7)
DHT_SENSOR_TYPE = Adafruit_DHT.DHT22  # Tipo de sensor DHT (DHT11, DHT22, etc.)

# Sensor LDR (luz ambiental)
LDR_PIN = 5  # GPIO5 (Pin físico 29)

# ---- ACTUADORES ----
# Bomba de agua
BOMBA_AGUA_PIN = 18  # GPIO18 (Pin físico 12)

# Ventilador
VENTILADOR_PIN = 17  # GPIO17 (Pin físico 11)

# Relé auxiliar
RELE_PIN = 27  # GPIO27 (Pin físico 13)

# ---- PANTALLA LCD ----
# Configuración para LCD con conexión GPIO directa
LCD_RS = 25    # GPIO25 (Pin físico 22)
LCD_EN = 24    # GPIO24 (Pin físico 18)
LCD_D4 = 23    # GPIO23 (Pin físico 16)
LCD_D5 = 17    # GPIO17 (Pin físico 11) - Compartido con VENTILADOR_PIN (¡cuidado!)
LCD_D6 = 18    # GPIO18 (Pin físico 12) - Compartido con BOMBA_AGUA_PIN (¡cuidado!)
LCD_D7 = 22    # GPIO22 (Pin físico 15)
LCD_BACKLIGHT = 4  # GPIO4 (Pin físico 7) - Compartido con DHT_PIN (¡cuidado!)

# Configuración para LCD con conexión I2C
# I2C utiliza:
# - SDA: GPIO2 (Pin físico 3)
# - SCL: GPIO3 (Pin físico 5)
LCD_I2C_ADDRESS = 0x27  # Dirección I2C del módulo LCD

# ---- CONFIGURACIÓN DE COLUMNAS Y FILAS DEL LCD ----
LCD_COLUMNS = 16
LCD_ROWS = 2

# Función para verificar conflictos de pines
def verificar_conflictos():
    """Verifica y reporta posibles conflictos en la asignación de pines."""
    todos_los_pines = {
        "DHT_PIN": DHT_PIN,
        "LDR_PIN": LDR_PIN,
        "BOMBA_AGUA_PIN": BOMBA_AGUA_PIN,
        "VENTILADOR_PIN": VENTILADOR_PIN,
        "RELE_PIN": RELE_PIN
    }
    
    # Solo agregar los pines LCD si no estamos usando I2C
    lcd_pines = {
        "LCD_RS": LCD_RS,
        "LCD_EN": LCD_EN,
        "LCD_D4": LCD_D4,
        "LCD_D5": LCD_D5,
        "LCD_D6": LCD_D6,
        "LCD_D7": LCD_D7,
        "LCD_BACKLIGHT": LCD_BACKLIGHT
    }
    
    # Detectar duplicados
    valores = list(todos_los_pines.values())
    duplicados = []
    
    for nombre, valor in todos_los_pines.items():
        if valores.count(valor) > 1:
            duplicados.append(nombre)
            
    # Verificar conflictos con los pines LCD
    lcd_conflictos = []
    for nombre_lcd, valor_lcd in lcd_pines.items():
        for nombre, valor in todos_los_pines.items():
            if nombre != nombre_lcd and valor == valor_lcd:
                lcd_conflictos.append(f"{nombre_lcd} y {nombre}")
    
    return duplicados, lcd_conflictos

if __name__ == "__main__":
    # Esto permite ejecutar este archivo directamente para verificar conflictos
    duplicados, lcd_conflictos = verificar_conflictos()
    
    if duplicados:
        print("¡ADVERTENCIA! Se detectaron pines duplicados:")
        for pin in duplicados:
            print(f"  - {pin}: GPIO{todos_los_pines[pin]}")
    
    if lcd_conflictos:
        print("\n¡ADVERTENCIA! Posibles conflictos con los pines LCD:")
        for conflicto in lcd_conflictos:
            print(f"  - Conflicto entre {conflicto}")
    
    if not duplicados and not lcd_conflictos:
        print("No se detectaron conflictos en la configuración de pines.")
