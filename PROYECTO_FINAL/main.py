# ============================================================
# main.py — Archivo principal del sistema de monitoreo
# Ejecutar: python main.py
# ============================================================

import threading
import time

import config
import serial_reader
import data_store
import analyzer
import plotter
import socket_server
import thingspeak_client
import web_app


def hilo_procesamiento():
    """
    Hilo 4: cada 2 segundos guarda datos nuevos en CSV,
    genera gráficas y actualiza socket y ThingSpeak.
    """
    while True:
        time.sleep(2)

        datos = serial_reader.obtener_datos()

        # Guardar nuevos datos en CSV
        data_store.guardar_nuevos(datos)

        # Analizar
        stats = analyzer.analizar(datos)

        if stats:
            # Actualizar módulos que dependen del análisis
            socket_server.actualizar_resumen(stats)
            thingspeak_client.actualizar_datos(stats)

            # Generar gráficas (solo si hay suficientes datos)
            if stats["num_muestras"] >= 5:
                plotter.generar_graficas(datos)


def main():
    print("=" * 50)
    print("  Sistema de Monitoreo de Humedad - ESP32")
    print("  Programación Aplicada 2025-3")
    print("=" * 50)

    # 1. Inicializar CSV
    data_store.inicializar_csv()

    # 2. Lanzar hilos
    serial_reader.iniciar()          # Hilo 1: lectura UART
    socket_server.iniciar()          # Hilo 2: servidor TCP
    thingspeak_client.iniciar()      # Hilo 3: envío ThingSpeak

    hilo_proc = threading.Thread(    # Hilo 4: análisis + CSV + gráficas
        target=hilo_procesamiento,
        name="HiloProcesamiento",
        daemon=True,
    )
    hilo_proc.start()

    print(f"\n[Info] Página web  → http://{config.FLASK_HOST}:{config.FLASK_PORT}")
    print(f"[Info] Socket TCP  → telnet {config.SOCKET_HOST} {config.SOCKET_PORT}")
    print(f"[Info] Puerto serial: {config.PUERTO_SERIAL}")
    print("[Info] Presiona Ctrl+C para detener\n")

    # Flask corre en el hilo principal (necesario para werkzeug)
    web_app.iniciar()


if __name__ == "__main__":
    main()
