# ============================================================
# web_app.py — Servidor web con Flask
# http://127.0.0.1:5000
# ============================================================

from flask import Flask, render_template
import serial_reader
import analyzer
import thingspeak_client
import config

app = Flask(__name__)


@app.route("/")
def index():
    datos = serial_reader.obtener_datos()
    stats = analyzer.analizar(datos)
    estado_ts = thingspeak_client.obtener_estado()
    return render_template("index.html", stats=stats,estado_ts=estado_ts,config_puerto=config.PUERTO_SERIAL)


@app.route("/datos")
def datos_json():
    """Endpoint simple para verificar datos en crudo (JSON)."""
    from flask import jsonify
    datos = serial_reader.obtener_datos()
    ultimos = datos[-20:] if len(datos) > 20 else datos
    return jsonify(ultimos)


def iniciar():
    """Inicia Flask. Bloquea el hilo que lo llame."""
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False,
    )
