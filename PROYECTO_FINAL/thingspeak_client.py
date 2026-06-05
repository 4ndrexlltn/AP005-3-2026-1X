# ============================================================
# thingspeak_client.py — Envío periódico de datos a ThingSpeak
# ============================================================

import requests
import threading
import time
import config

_datos   = {}
_lock    = threading.Lock()
_ultimo_envio = 0
_estado_envio = "Esperando primer envío..."


def actualizar_datos(stats):
    """Actualiza los datos para el próximo envío."""
    global _datos
    with _lock:
        _datos = dict(stats) if stats else {}


def obtener_estado():
    """Devuelve el estado del último envío (para la página web)."""
    return _estado_envio


def _enviar():
    """Hilo: envía datos a ThingSpeak cada N segundos."""
    global _ultimo_envio, _estado_envio

    while True:
        time.sleep(1)
        ahora = time.time()

        if ahora - _ultimo_envio < config.THINGSPEAK_INTERVALO:
            continue

        with _lock:
            datos = dict(_datos)

        if not datos:
            continue

        # Convertir estado textual a numérico
        estado_num = {"MUY HÚMEDO": 0, "NORMAL": 1, "SECO": 2}.get(
            datos.get("estado", "NORMAL"), 1
        )

        payload = {
            "api_key": config.THINGSPEAK_API_KEY,
            "field1":  datos.get("ultimo_adc", 0),
            "field2":  datos.get("ultimo_voltaje", 0),
            "field3":  datos.get("promedio_movil", 0),
            "field4":  estado_num,
        }

        try:
            resp = requests.get(
                config.THINGSPEAK_URL,
                params=payload,
                timeout=10
            )
            _ultimo_envio = time.time()

            if resp.text.strip() == "0":
                _estado_envio = f"⚠️ Error ThingSpeak (respuesta 0). Verifica la API Key."
            else:
                _estado_envio = (
                    f"✅ Enviado a ThingSpeak | "
                    f"Entrada #{resp.text.strip()} | "
                    f"V={datos.get('ultimo_voltaje')} V | "
                    f"H={datos.get('ultimo_humedad')}% | "
                    f"Estado={datos.get('estado')}"
                )
            print(f"[ThingSpeak] {_estado_envio}")

        except requests.RequestException as e:
            _estado_envio = f"❌ Error de red: {e}"
            print(f"[ThingSpeak] {_estado_envio}")


def iniciar():
    """Lanza el hilo de envío."""
    hilo = threading.Thread(target=_enviar, name="HiloThingSpeak", daemon=True)
    hilo.start()
    return hilo
