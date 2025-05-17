import serial
import I2C_LCD_driver
import time

# Configurar puerto serial
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
ser.flush()

# Inicializar LCD
lcd = I2C_LCD_driver.lcd()

# Mensajes a mostrar
mensajes = {
    "mat": "FSE 2025-2",
    "brig": "GPO. 6 BRIGADA 2",
    "etemp": "TEMPERATURA:",
    "ehum": "HUMEDAD:",
    "nodata": "Sin Datos..."
}

# --------------------------------------------------------
# Maneja la recepcion de datos UART
# --------------------------------------------------------
def recibir_datos_serial(max_buffer=100):
    """Lee datos desde el puerto UART y los separa en temperatura y humedad.
    Limpia el buffer si detecta un error o un desbordamiento."""
    if ser.in_waiting > 0:
        # Verificar si el buffer está demasiado lleno
        if ser.in_waiting > max_buffer:
            print("[UART] Buffer de entrada lleno. Limpiando...")
            ser.reset_input_buffer()
            return None, None

        # Leer datos
        line = ser.readline().decode('utf-8').strip()
        print(f"[UART] Datos recibidos: {line}")
        # Validar Datos 
        try:
            temperaturaStr, humedadStr = line.split(',')
            return temperaturaStr.strip(), humedadStr.strip()
        except ValueError:
            print("\t\u21B3 Error al separar los datos: Datos inválidos")
            ser.reset_input_buffer()
    else: print("[UART] Buffer de entrada vacío")
    return None, None

# --------------------------------------------------------
# Da formato a los datos para una correcta visualización
# --------------------------------------------------------
def formatear_datos(temp_str, hum_str):
    """Formatea la temperatura como: EEE.DD°C, y la humedad como: HHH%"""
    # Temperatura
    ent, dec = temp_str.split('.')
    dec = dec[:2].ljust(2, '0') # 2 decimales
    ent = ent.rjust(3, ' ') # tres digitos enteros
    temp_format = f"{ent}.{dec}" + chr(223) + "C" # e.g. _25.34°C
    #223 es carácter ° en charmap A00 de los LCD
    # Humedad
    hum_format = hum_str.rjust(3, '0') # tres digitos enteros
    hum_format = f"{hum_format}" + "%" # e.g. 017%

    return temp_format, hum_format

# --------------------------------------------------------
# Controla la escritura de mensajes en una posicion dada
# --------------------------------------------------------
def escribir_mensaje(msg, row=1, col=0, t=0, clr=True):
    """Controla la escritura de mensajes en el LCD 16x2 a traves de 
    una comunicacion I2C empleando i2C_LCD_driver"""
    if (clr):
        lcd.lcd_clear()
    lcd.lcd_display_string_pos(msg, row, col)
    time.sleep(t)

# --------------------------------------------------------
# Muestra los datos en el LCD con formato personalizado
# --------------------------------------------------------
def mostrar_datos_lcd(temp, hum):
    """Muestra los datos recibidos en el LCD """
    temp_forma, hum_forma = formatear_datos(temp,hum)
    # Mostar temperatura
    escribir_mensaje(mensajes["etemp"], 1, 2) # encabezado temperatura
    escribir_mensaje(temp_forma, 2, 4, 2, clr=False)
    
    # Mostar humedad
    escribir_mensaje(mensajes["ehum"], 1, 4) # encabezado humedad
    escribir_mensaje(hum_forma, 2, 6, 2, clr=False)

def main():
    try:
        while True:
            escribir_mensaje(mensajes["mat"], 1, 3)
            escribir_mensaje(mensajes["brig"], 2, 0, 1.5, clr=False)

            temp, hum = recibir_datos_serial()
            if temp and hum:
                mostrar_datos_lcd(temp, hum)
            else:
                #print("Sin datos o datos inválidos.")
                escribir_mensaje(mensajes["nodata"], 1, 2, 1.5)
    except KeyboardInterrupt:
        print("Programa terminado por usuario.")
    finally:
        lcd.lcd_clear()
        ser.close()

if __name__ == '__main__':
    main()
