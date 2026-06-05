# ============================================================
# plotter.py — Generación de gráficas con matplotlib
# ============================================================

import matplotlib
matplotlib.use("Agg")   # Sin GUI, necesario para Flask
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np
import os

CARPETA = "static/plots"

# Paleta de colores consistente
COLOR_SIGNAL  = "#2196F3"
COLOR_MOVIL   = "#F44336"
COLOR_HIST    = "#4CAF50"
COLOR_HUMEDAD = "#9C27B0"


def _preparar_carpeta():
    os.makedirs(CARPETA, exist_ok=True)


def grafica_tiempo(df):
    """Gráfica del voltaje del sensor en función del tiempo."""
    t = df["tiempo_ms"] / 1000
    v = df["voltaje"]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, v, color=COLOR_SIGNAL, linewidth=1.2, alpha=0.9)
    ax.fill_between(t, v, alpha=0.1, color=COLOR_SIGNAL)
    ax.set_title("Voltaje del sensor de humedad en el tiempo", fontsize=13, fontweight="bold")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Voltaje (V)")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_ylim(0, 3.4)
    fig.tight_layout()
    fig.savefig(f"{CARPETA}/sensor_tiempo.png", dpi=120)
    plt.close(fig)


def grafica_histograma(df):
    """Histograma de distribución de voltajes."""
    v = df["voltaje"]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(v, bins=25, color=COLOR_HIST, edgecolor="white", linewidth=0.5)
    ax.axvline(v.mean(), color="red", linestyle="--", linewidth=1.5, label=f"Promedio: {v.mean():.2f} V")
    ax.set_title("Histograma de voltajes medidos", fontsize=13, fontweight="bold")
    ax.set_xlabel("Voltaje (V)")
    ax.set_ylabel("Frecuencia")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.4, axis="y")
    fig.tight_layout()
    fig.savefig(f"{CARPETA}/histograma.png", dpi=120)
    plt.close(fig)


def grafica_promedio_movil(df):
    """Señal original + promedio móvil superpuesto."""
    t  = df["tiempo_ms"] / 1000
    v  = df["voltaje"]
    pm = pd.Series(v.values).rolling(window=10, min_periods=1).mean()

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, v,  color=COLOR_SIGNAL, linewidth=0.8, alpha=0.4, label="Señal")
    ax.plot(t, pm, color=COLOR_MOVIL,  linewidth=2.0, label="Promedio móvil (n=10)")
    ax.set_title("Promedio móvil del sensor de humedad", fontsize=13, fontweight="bold")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Voltaje (V)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_ylim(0, 3.4)
    fig.tight_layout()
    fig.savefig(f"{CARPETA}/promedio_movil.png", dpi=120)
    plt.close(fig)


def grafica_humedad(df):
    """Porcentaje de humedad en el tiempo (gráfica adicional)."""
    t = df["tiempo_ms"] / 1000
    h = df["humedad"]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, h, color=COLOR_HUMEDAD, linewidth=1.5)
    ax.fill_between(t, h, alpha=0.15, color=COLOR_HUMEDAD)
    ax.axhline(y=50, color="orange", linestyle="--", linewidth=1, label="50% humedad")
    ax.set_title("Porcentaje de humedad del suelo", fontsize=13, fontweight="bold")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Humedad (%)")
    ax.set_ylim(0, 105)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    fig.savefig(f"{CARPETA}/humedad_pct.png", dpi=120)
    plt.close(fig)


def generar_graficas(datos):
    """Genera las 4 gráficas. Llama a esta función desde main."""
    if not datos or len(datos) < 5:
        return

    _preparar_carpeta()
    df = pd.DataFrame(datos)

    try:
        grafica_tiempo(df)
        grafica_histograma(df)
        grafica_promedio_movil(df)
        grafica_humedad(df)
        print(f"[Plotter] 4 gráficas generadas en {CARPETA}/")
    except Exception as e:
        print(f"[Plotter] Error al generar gráficas: {e}")
