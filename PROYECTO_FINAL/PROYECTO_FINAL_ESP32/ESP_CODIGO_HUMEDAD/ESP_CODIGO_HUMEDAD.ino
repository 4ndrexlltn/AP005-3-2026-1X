// ============================================================
// ESP32 - Sensor de Humedad Capacitivo
// Proyecto Final Python - Programación Aplicada 2025-3
// Pin ADC: GPIO34
// Formato envío: tiempo_ms,adc,voltaje
// ============================================================

const int PIN_ADC     =35;
const float V_REF     = 3.3;
const int ADC_MAX     = 4095;

// ---- Calibración: ajustar sensor ----
const int ADC_SECO    = 3100;   // Sensor al aire
const int ADC_MOJADO  = 900;    // Sensor en agua
// -------------------------------------------

unsigned long t0;

void setup() {
  Serial.begin(115200);
  t0 = millis();
  delay(500);
  Serial.println("# ESP32 Humedad Capacitivo - INICIO");
}

void loop() {
  int adc = analogRead(PIN_ADC);
  float voltaje = (adc * V_REF) / ADC_MAX;
  unsigned long t_ms = millis() - t0;

  // Porcentaje de humedad (0% seco - 100% mojado)
  int humedad = map(adc, ADC_SECO, ADC_MOJADO, 0, 100);
  humedad = constrain(humedad, 0, 100);

  // Formato: tiempo_ms,adc,voltaje
  Serial.print(t_ms);
  Serial.print(",");
  Serial.print(adc);
  Serial.print(",");
  Serial.println(voltaje, 2);

  delay(200);  // 5 muestras por segundo
}