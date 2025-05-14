def controlar_riego(humedad_suelo, umbral_humedad):
    """Controla el sistema de riego según la humedad del suelo."""
    if humedad_suelo < umbral_humedad:
        activar_riego()
    else:
        desactivar_riego()

def controlar_ventilacion(temperatura, humedad_aire, umbral_temperatura, umbral_humedad):
    """Controla el sistema de ventilación según la temperatura y la humedad del aire."""
    if temperatura > umbral_temperatura or humedad_aire > umbral_humedad:
        activar_ventilacion()
    else:
        desactivar_ventilacion()

def decidir_riego(humedad_suelo):
    """Decide si se debe activar el riego según la humedad del suelo."""
    pass

def decidir_ventilacion(temperatura, humedad_aire):
    """Decide si se debe activar la ventilación según temperatura y humedad del aire."""
    pass