# configuracion.py

CONFIG = {
    # Umbrales para activar actuadores
    'umbral_humedad_suelo': 30,  # Activar riego cuando humedad < 30%
    'umbral_temperatura': 28,    # Activar ventilación cuando temperatura > 28°C
    'umbral_humedad_aire': 70,   # Activar ventilación cuando humedad > 70%
    
    # Configuración de sensores
    'intervalo_lectura': 5,     # Intervalo entre lecturas (segundos)
    
    # Duración de activación de actuadores
    'duracion_riego': 10,       # Tiempo de riego (segundos)
    
    # Configuración del sistema
    'debug': True,              # Modo debug para imprimir información
}