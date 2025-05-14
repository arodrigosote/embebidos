# Importaciones de sensores
from sensores.humedad_suelo import leer_humedad_suelo
from sensores.dht import leer_temperatura, leer_humedad_aire
from sensores.ldr import leer_luz_ambiental

# Importaciones de actuadores
from actuadores.bomba_agua import activar_bomba, desactivar_bomba
from actuadores.rele import activar_rele, desactivar_rele
from actuadores.ventilador import activar_ventilador, desactivar_ventilador

# Importación de LCD
from lcd.pantalla_lcd import mostrar_en_lcd

# Importación de lógica de control
from control.logica_control import decidir_riego, decidir_ventilacion

# Importación de configuración
from config.configuracion import CONFIG

# Importación de la app web
from webapp.app import iniciar_webapp

def main():
    # Inicialización de sensores y actuadores
    # (Aquí puedes agregar inicializaciones si es necesario)

    # Ejemplo de lectura de sensores
    humedad_suelo = leer_humedad_suelo()
    temperatura = leer_temperatura()
    humedad_aire = leer_humedad_aire()
    luz_ambiental = leer_luz_ambiental()

    # Ejemplo de lógica de control
    if decidir_riego(humedad_suelo):
        activar_bomba()
    else:
        desactivar_bomba()

    if decidir_ventilacion(temperatura, humedad_aire):
        activar_ventilador()
    else:
        desactivar_ventilador()

    # Mostrar información en LCD
    mostrar_en_lcd(humedad_suelo, temperatura, humedad_aire, luz_ambiental)

    # Iniciar aplicación web (en segundo plano o hilo aparte si es necesario)
    iniciar_webapp()

if __name__ == "__main__":
    main()