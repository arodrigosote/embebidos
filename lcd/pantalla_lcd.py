import Adafruit_CharLCD as LCD

# Configuración de los pines de la Raspberry Pi
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 4

# Definición de columnas y filas del LCD
lcd_columns = 16
lcd_rows = 2

# Inicialización del LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

def mostrar_en_lcd(humedad_suelo, temperatura, humedad_aire, luz_ambiental):
    """Muestra información en la pantalla LCD."""
    pass