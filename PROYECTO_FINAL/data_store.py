# ============================================================
# data_store.py — Almacenamiento de datos en archivo CSV
# ============================================================

import csv
import os
import config

_ultimo_guardado = 0   # Índice del último dato guardado


def inicializar_csv():
    """Crea la carpeta data/ y el CSV con encabezados si no existe."""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(config.ARCHIVO_CSV):
        with open(config.ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["tiempo_ms", "adc", "voltaje", "humedad"])
        print(f"[CSV] Archivo creado: {config.ARCHIVO_CSV}")
    else:
        print(f"[CSV] Usando archivo existente: {config.ARCHIVO_CSV}")


def guardar_nuevos(datos):
    """
    Recibe la lista completa de datos y guarda solo los nuevos
    (los que aún no se han escrito en el CSV).
    """
    global _ultimo_guardado

    nuevos = datos[_ultimo_guardado:]
    if not nuevos:
        return 0

    with open(config.ARCHIVO_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for d in nuevos:
            writer.writerow([d["tiempo_ms"], d["adc"], d["voltaje"], d["humedad"]])

    _ultimo_guardado += len(nuevos)
    print(f"[CSV] Guardados {len(nuevos)} registros. Total: {_ultimo_guardado}")
    return len(nuevos)


def leer_csv():
    """Lee el CSV completo y devuelve lista de dicts (útil para debug)."""
    if not os.path.exists(config.ARCHIVO_CSV):
        return []
    filas = []
    with open(config.ARCHIVO_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            filas.append({
                "tiempo_ms": int(fila["tiempo_ms"]),
                "adc":       int(fila["adc"]),
                "voltaje":   float(fila["voltaje"]),
                "humedad":   int(fila["humedad"]),
            })
    return filas
