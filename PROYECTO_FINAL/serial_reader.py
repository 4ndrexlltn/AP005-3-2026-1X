# ============================================================
# serial_reader.py — Lectura continua del puerto serial UART
# ============================================================

import serial
import threading
import config

# ----- Estado compartido -----
_datos  = []          # Lista de dicts con todas las lecturas
_lock   = threading.Lock() #Evita que varios hilos modifiquen una variable al mismo tiempo
_activo = True

def leer_serial():
    """Hilo principal: lee líneas del ESP32 y las almacena."""
    global _activo
    try:
        ser = serial.Serial(config.PUERTO_SERIAL, config.BAUDRATE, timeout=2)
        print(f"[Serial] Conectado a {config.PUERTO_SERIAL} a {config.BAUDRATE} bps")

        while _activo:
            try:
                linea = ser.readline().decode("utf-8", errors="ignore").strip()
            except Exception:
                continue

            # Ignorar comentarios y líneas vacías
            if not linea or linea.startswith("#"):
                continue

            partes = linea.split(",")
            if len(partes) != 3:
                continue

            try:
                tiempo  = int(partes[0])
                adc     = int(partes[1])
                voltaje = float(partes[2])

                # Calcular % humedad en Python también
                humedad = int(
                    100 * (config.ADC_SECO - adc) /
                    max(1, config.ADC_SECO - config.ADC_MOJADO)
                )
                humedad = max(0, min(100, humedad))

                dato = {
                    "tiempo_ms": tiempo,
                    "adc":       adc,
                    "voltaje":   voltaje,
                    "humedad":   humedad,
                }

                with _lock:
                    _datos.append(dato)

                print(f"[Serial] t={tiempo}ms  ADC={adc}  V={voltaje:.2f}  H={humedad}%")

            except ValueError:
                pass   # Línea malformada, se descarta

        ser.close()

    except serial.SerialException as e:
        print(f"[Serial] ERROR: {e}")
        print("[Serial] Verifica el puerto en config.py")


def obtener_datos():
    """Devuelve copia thread-safe de todos los datos."""
    with _lock:
        return list(_datos)


def detener():
    global _activo
    _activo = False


def iniciar():
    """Lanza el hilo de lectura serial."""
    hilo = threading.Thread(target=leer_serial, name="HiloSerial", daemon=True)
    hilo.start()
    return hilo
