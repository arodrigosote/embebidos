import I2C_LCD_driver
import time

# Inicializar el LCD
lcd = I2C_LCD_driver.lcd()
#lcd.backlight(0)

mensajes = [
    "   FSE 2025-2    ", "BRIGADA02 GPO.06",
    "VERANO PERALTA","MARIA FERNANDA", "JACOBO RUIZ", "JESUS JAVIER",
    "GARCES ANGULO" ,"CARLOS ALBERTO", "SOTELO RAMIREZ", "AXEL RODRIGO",
    "SAUCEDO CHAVARRIA" ,"DIEGO"
]

for i in range(len(mensajes)):
    lcd.lcd_clear()
    if i % 2 != 0:
        lcd.lcd_display_string(mensajes[i], 2)
        lcd.lcd_display_string(mensajes[i-1], 1)
        
    time.sleep(0.5)
    