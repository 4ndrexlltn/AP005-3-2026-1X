# Proyecto ESP32 + Flask

## Descripción
Sistema de adquisición de datos desde un potenciómetro usando ESP32,
almacenamiento en CSV y visualización web con Flask.

## Instalación
pip install -r requirements.txt

## Uso

1. Ejecutar captura de datos:
python leer_serial.py

2. Ejecutar servidor web:
python app.py

3. Abrir en navegador:
http://127.0.0.1:5000

## Estructura
- leer_serial.py → adquisición
- app.py → servidor Flask
- templates/index.html → interfaz web
