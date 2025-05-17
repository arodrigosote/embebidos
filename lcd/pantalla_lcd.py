import Adafruit_CharLCD as LCD
import I2C_LCD_driver
from config.pines_config import (
    LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7, 
    LCD_BACKLIGHT, LCD_COLUMNS, LCD_ROWS, LCD_I2C_ADDRESS
)

# Inicialización del LCD - Versión con I2C
try:
    # Pasar la dirección I2C correcta si está personalizada en el módulo
    I2C_LCD_driver.ADDRESS = LCD_I2C_ADDRESS
    lcd_i2c = I2C_LCD_driver.lcd()
    use_i2c = True
    print("Usando LCD con I2C")
except:
    # Fallback a la versión con pines GPIO
    lcd = LCD.Adafruit_CharLCD(
        LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7, 
        LCD_COLUMNS, LCD_ROWS, LCD_BACKLIGHT
    )
    use_i2c = False
    print("Usando LCD con pines GPIO")

def mostrar_en_lcd(humedad_suelo, temperatura, humedad_aire, luz_ambiental):
    """Muestra información en la pantalla LCD."""
    # Formatear la información
    linea1 = f"T:{temperatura:.1f}C H:{humedad_aire:.1f}%"
    linea2 = f"Suelo:{humedad_suelo:.1f}% L:{luz_ambiental}"
    
    if use_i2c:
        lcd_i2c.lcd_clear()
        lcd_i2c.lcd_display_string(linea1, 1)
        lcd_i2c.lcd_display_string(linea2, 2)
    else:
        lcd.clear()
        lcd.message(linea1 + "\n" + linea2)
    
    print(f"LCD: {linea1} | {linea2}")