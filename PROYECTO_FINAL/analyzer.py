# ============================================================
# analyzer.py — Análisis de datos con pandas y numpy
# ============================================================

import pandas as pd
import numpy as np
import config


def analizar(datos):
    """
    Recibe lista de dicts con lecturas y devuelve dict con estadísticas.
    Usa pandas para organización tabular y numpy para cálculos numéricos.
    Retorna None si no hay datos suficientes.
    """
    if not datos or len(datos) < 2:
        return None

    # Crear DataFrame de pandas
    df = pd.DataFrame(datos)

    # Arrays de numpy para cálculos
    voltajes  = df["voltaje"].to_numpy()
    humedades = df["humedad"].to_numpy()
    adcs      = df["adc"].to_numpy()

    # Estadísticas de voltaje 
    promedio     = float(np.mean(voltajes))
    minimo       = float(np.min(voltajes))
    maximo       = float(np.max(voltajes))
    desv_std     = float(np.std(voltajes))

    # Promedio móvil (ventana = 10 muestras)
    serie_pm     = pd.Series(voltajes).rolling(window=10, min_periods=1).mean()
    prom_movil   = float(serie_pm.iloc[-1])

    # Estadísticas de humedad
    prom_humedad = float(np.mean(humedades))
    ult_humedad  = int(df["humedad"].iloc[-1])

    # Clasificación por umbral
    ultimo_v = float(df["voltaje"].iloc[-1])
    if ultimo_v < config.UMBRAL_BAJO:
        estado = "MUY HÚMEDO"
    elif ultimo_v > config.UMBRAL_ALTO:
        estado = "SECO"
    else:
        estado = "NORMAL"

    return {
        "num_muestras":   len(df),
        "ultimo_adc":     int(df["adc"].iloc[-1]),
        "ultimo_voltaje": round(ultimo_v, 3),
        "ultimo_humedad": ult_humedad,
        "promedio":       round(promedio, 3),
        "minimo":         round(minimo, 3),
        "maximo":         round(maximo, 3),
        "desviacion_std": round(desv_std, 3),
        "promedio_movil": round(prom_movil, 3),
        "prom_humedad":   round(prom_humedad, 1),
        "estado":         estado,
    }
