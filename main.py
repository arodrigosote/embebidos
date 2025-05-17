# Importaciones de sensores
from sensores.humedad_suelo import leer_humedad_suelo
from sensores.dht import leer_temperatura, leer_humedad_aire
from sensores.ldr import leer_luz_ambiental

# Importaciones de actuadores
from actuadores.bomba_agua import activar_bomba, desactivar_bomba
from actuadores.rele import activar_rele, desactivar_rele, init_rele
from actuadores.ventilador import activar_ventilador, desactivar_ventilador

# Importación de LCD
from lcd.pantalla_lcd import mostrar_en_lcd

# Importación de lógica de control
from control.logica_control import decidir_riego, decidir_ventilacion

# Importación de configuración
from config.configuracion import CONFIG
from config.pines_config import verificar_conflictos  # Para verificar posibles conflictos de pines

import time
import RPi.GPIO as GPIO
import threading

# Estado de los actuadores
estado_actuadores = {
    'bomba': False,
    'ventilador': False,
    'rele': False
}

def inicializar_sistema():
    """Inicializa el sistema: GPIO, sensores y actuadores."""
    # Verificar conflictos de pines
    duplicados, lcd_conflictos = verificar_conflictos()
    if duplicados or lcd_conflictos:
        print("¡ADVERTENCIA! Se detectaron posibles conflictos de pines:")
        if duplicados:
            print("Pines duplicados:", duplicados)
        if lcd_conflictos:
            print("Conflictos con LCD:", lcd_conflictos)
    
    # Inicializar el relé
    init_rele()
    
    # Desactivar todos los actuadores al inicio
    desactivar_bomba()
    desactivar_ventilador()
    desactivar_rele()
    
    print("Sistema inicializado correctamente.")

def leer_sensores():
    """Lee todos los sensores y devuelve sus valores."""
    try:
        humedad_suelo = leer_humedad_suelo()
        temperatura = leer_temperatura()
        humedad_aire = leer_humedad_aire()
        luz_ambiental = leer_luz_ambiental()
        
        datos = {
            'humedad_suelo': humedad_suelo,
            'temperatura': temperatura,
            'humedad_aire': humedad_aire,
            'luz_ambiental': luz_ambiental,
            'timestamp': time.time()
        }
        
        if CONFIG.get('debug', False):
            print(f"Sensores: Temp={temperatura}°C, Hum_Aire={humedad_aire}%, Hum_Suelo={humedad_suelo}%, Luz={luz_ambiental}")
        
        return datos
    except Exception as e:
        print(f"Error al leer sensores: {e}")
        return None

def controlar_actuadores(datos):
    """Controla los actuadores según los datos de los sensores."""
    global estado_actuadores
    
    # Control de riego
    if decidir_riego(datos['humedad_suelo']):
        activar_bomba()
        estado_actuadores['bomba'] = True
    else:
        desactivar_bomba()
        estado_actuadores['bomba'] = False
    
    # Control de ventilación
    if decidir_ventilacion(datos['temperatura'], datos['humedad_aire']):
        activar_ventilador()
        estado_actuadores['ventilador'] = True
    else:
        desactivar_ventilador()
        estado_actuadores['ventilador'] = False
    
    # Relé auxiliar (ejemplo: se activa con baja luminosidad)
    if datos['luz_ambiental'] < 20:  # Valor arbitrario para el ejemplo
        activar_rele()
        estado_actuadores['rele'] = True
    else:
        desactivar_rele()
        estado_actuadores['rele'] = False

def bucle_principal():
    """Bucle principal del sistema."""
    try:
        while True:
            # Leer datos de los sensores
            datos = leer_sensores()
            
            if datos:
                # Controlar actuadores
                controlar_actuadores(datos)
                
                # Mostrar en LCD
                mostrar_en_lcd(
                    datos['humedad_suelo'], 
                    datos['temperatura'], 
                    datos['humedad_aire'], 
                    datos['luz_ambiental']
                )
                
                # Actualizar datos para la webapp
                actualizar_datos(datos, estado_actuadores)
            
            # Esperar el tiempo configurado
            time.sleep(CONFIG.get('intervalo_lectura', 5))
    
    except KeyboardInterrupt:
        print("Programa terminado por el usuario.")
    except Exception as e:
        print(f"Error en el bucle principal: {e}")
    finally:
        # Limpiar GPIOs al terminar
        GPIO.cleanup()
        print("GPIOs liberados.")

def main():
    # Inicialización del sistema
    inicializar_sistema()
    
    # Iniciar aplicación web
    webapp_thread = iniciar_webapp()
    
    # Iniciar bucle principal
    bucle_principal()

if __name__ == "__main__":
    main()