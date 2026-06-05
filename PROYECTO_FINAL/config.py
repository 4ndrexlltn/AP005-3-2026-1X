# ============================================================
# config.py — Configuración central del sistema
# ============================================================

# --- Puerto Serial ---

PUERTO_SERIAL = "COM4"
BAUDRATE      = 115200

# --- Archivo de datos ---
ARCHIVO_CSV = "data/lecturas.csv"

# --- Servidor Socket TCP ---
SOCKET_HOST = "127.0.0.1"
SOCKET_PORT = 9000

# --- Flask ---
FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000

# --- ThingSpeak ---
THINGSPEAK_URL     = "https://api.thingspeak.com/update"
THINGSPEAK_API_KEY = "TU_API_KEY_AQUI"   # <-- Reemplaza con tu clave
THINGSPEAK_INTERVALO = 15                # Segundos entre envíos

# --- Umbrales del sensor capacitivo de humedad ---
# El sensor es INVERSAMENTE proporcional:
#   Voltaje ALTO   → suelo SECO
#   Voltaje BAJO   → suelo HÚMEDO
UMBRAL_BAJO  = 1.2   # Debajo de esto → MUY HÚMEDO
UMBRAL_ALTO  = 2.2   # Encima de esto → SECO

# --- Calibración ADC ---
ADC_SECO   = 3100
ADC_MOJADO = 900
