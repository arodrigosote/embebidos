import os
import time
import datetime
import requests
import json
import RPi.GPIO as GPIO
from flask import Flask, render_template, jsonify, request
import threading

app = Flask(__name__)

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pines de los sensores
PIR_PIN = 17
DHT_PIN = 4

# Pines de los actuadores
LED_PIN = 27
BUZZER_PIN = 22

# Configuración de los pines como entrada o salida
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(DHT_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Estado inicial de los actuadores
GPIO.output(LED_PIN, GPIO.LOW)
GPIO.output(BUZZER_PIN, GPIO.LOW)

# Función para leer el sensor PIR
def leer_pir():
    return GPIO.input(PIR_PIN)

# Función para leer el sensor DHT11
def leer_dht11():
    # Código para leer el sensor DHT11
    pass

# Función para encender el LED
def encender_led():
    GPIO.output(LED_PIN, GPIO.HIGH)

# Función para apagar el LED
def apagar_led():
    GPIO.output(LED_PIN, GPIO.LOW)

# Función para encender el buzzer
def encender_buzzer():
    GPIO.output(BUZZER_PIN, GPIO.HIGH)

# Función para apagar el buzzer
def apagar_buzzer():
    GPIO.output(BUZZER_PIN, GPIO.LOW)

# Variables para almacenar los últimos datos de sensores
datos_sensores = {
    'humedad_suelo': 0,
    'temperatura': 0,
    'humedad_aire': 0,
    'luz_ambiental': 0,
    'timestamp': 0
}

# Estado de los actuadores
estado_actuadores = {
    'bomba': False,
    'ventilador': False,
    'rele': False
}

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener el estado de los sensores
@app.route('/api/sensores', methods=['GET'])
def obtener_estado_sensores():
    pir_estado = leer_pir()
    dht11_estado = leer_dht11()
    return jsonify({'pir': pir_estado, 'dht11': dht11_estado})

# Ruta para encender el LED
@app.route('/led/encender', methods=['POST'])
def ruta_encender_led():
    encender_led()
    return jsonify({'mensaje': 'LED encendido'})

# Ruta para apagar el LED
@app.route('/led/apagar', methods=['POST'])
def ruta_apagar_led():
    apagar_led()
    return jsonify({'mensaje': 'LED apagado'})

# Ruta para encender el buzzer
@app.route('/buzzer/encender', methods=['POST'])
def ruta_encender_buzzer():
    encender_buzzer()
    return jsonify({'mensaje': 'Buzzer encendido'})

# Ruta para apagar el buzzer
@app.route('/buzzer/apagar', methods=['POST'])
def ruta_apagar_buzzer():
    apagar_buzzer()
    return jsonify({'mensaje': 'Buzzer apagado'})

@app.route('/api/actuadores')
def get_actuadores():
    return jsonify(estado_actuadores)

def actualizar_datos(datos, estado):
    global datos_sensores, estado_actuadores
    datos_sensores = datos
    estado_actuadores = estado

def iniciar_webapp(host='0.0.0.0', port=5000, debug=False):
    """Inicia la aplicación web en un hilo separado."""
    def run_app():
        app.run(host=host, port=port, debug=debug)
    
    # Iniciar la app en un hilo separado para no bloquear el programa principal
    webapp_thread = threading.Thread(target=run_app)
    webapp_thread.daemon = True  # El hilo se detendrá cuando el programa principal termine
    webapp_thread.start()
    print(f"Aplicación web iniciada en http://{host}:{port}")
    return webapp_thread

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)