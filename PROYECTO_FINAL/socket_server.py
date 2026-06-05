# ============================================================
# socket_server.py — Servidor TCP local independiente de Flask
# Prueba con: telnet 127.0.0.1 9000
#         o:  python -c "import socket; s=socket.socket(); s.connect(('127.0.0.1',9000)); print(s.recv(1024).decode()); s.close()"
# ============================================================

import socket
import threading
import json
import config

_resumen = {}
_lock    = threading.Lock()


def actualizar_resumen(stats):
    """Actualiza los datos que el socket entregará a los clientes."""
    global _resumen
    with _lock:
        _resumen = dict(stats) if stats else {}


def _manejar_cliente(conn, addr):
    """Atiende una conexión, envía el resumen y cierra."""
    print(f"[Socket] Cliente conectado desde {addr}")
    try:
        with _lock:
            datos = dict(_resumen)

        if datos:
            respuesta = (
                "=== Estado del Sistema de Humedad ===\n"
                f"ultimo_adc     : {datos.get('ultimo_adc', 'N/A')}\n"
                f"ultimo_voltaje : {datos.get('ultimo_voltaje', 'N/A')} V\n"
                f"ultimo_humedad : {datos.get('ultimo_humedad', 'N/A')} %\n"
                f"promedio       : {datos.get('promedio', 'N/A')} V\n"
                f"minimo         : {datos.get('minimo', 'N/A')} V\n"
                f"maximo         : {datos.get('maximo', 'N/A')} V\n"
                f"desv_std       : {datos.get('desviacion_std', 'N/A')} V\n"
                f"promedio_movil : {datos.get('promedio_movil', 'N/A')} V\n"
                f"muestras       : {datos.get('num_muestras', 0)}\n"
                f"estado         : {datos.get('estado', 'N/A')}\n"
                "=====================================\n"
            )
        else:
            respuesta = "Sin datos disponibles aún. Esperando ESP32...\n"

        conn.sendall(respuesta.encode("utf-8"))

    except Exception as e:
        print(f"[Socket] Error con cliente {addr}: {e}")
    finally:
        conn.close()
        print(f"[Socket] Cliente {addr} desconectado")


def _servidor():
    """Bucle principal del servidor TCP."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((config.SOCKET_HOST, config.SOCKET_PORT))
        srv.listen(5)
        print(f"[Socket] Servidor escuchando en {config.SOCKET_HOST}:{config.SOCKET_PORT}")

        while True:
            try:
                conn, addr = srv.accept()
                threading.Thread(
                    target=_manejar_cliente,
                    args=(conn, addr),
                    daemon=True,
                    name=f"HiloCliente-{addr[1]}"
                ).start()
            except Exception as e:
                print(f"[Socket] Error aceptando conexión: {e}")


def iniciar():
    """Lanza el servidor en un hilo daemon."""
    hilo = threading.Thread(target=_servidor, name="HiloSocket", daemon=True)
    hilo.start()
    return hilo
