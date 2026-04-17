#include <WiFi.h>

const char* ssid = "MIREYA ";
const char* password = "52081344";
WiFiServer server(3306);
WiFiClient client;

int listaPines[8] = {15, 2, 4, 16, 17, 5, 18, 19};
const int pinEntradaPulsador = 23;



void conectarWiFi(){
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi");
  while (WiFi.status() != WL_CONNECTED){
    Serial.println(WiFi.status());
    delay(500);
    Serial.println(".");
  }
  Serial.println();
  Serial.println("WiFi conectada");
  Serial.println("IP del ESP32");
  Serial.println(WiFi.localIP());
}


void setup() {
  Serial.begin(115200);
  pinMode(pinEntradaPulsador, INPUT);
  for(int i = 0; i < 8; i++) {
    Serial.println(listaPines[i]);
    pinMode(listaPines[i], OUTPUT);
  }
  delay(500);
  conectarWiFi();
  server.begin();
  Serial.println("Servidor TCP iniciando en puerto 3306");
  Serial.println("Comandos: 0, 1, 2, 3, 4, 5, 6, 7, 8 o q");

}

void loop() {
  if(!client || !client.connected()){
    WiFiClient nuevoCliente = server.available();
    if(nuevoCliente){
      client = nuevoCliente;
      Serial.println("Cliente Conectado");
      client.println("Conectado al ESP32");
      client.println("Comandos 0, 1, 2, 3, 4, 5, 6, 7, 8 o q");
    }
  }
   if(client && client.connected()){
      while (client.available() > 0){
        char c = client.read();
        activacionLeds(c, listaPines);

      }
    }
}

void activacionLeds(char c, int listaPinesSalida[8]){
  switch(c){
    case '0':
      activarSecuenciaBasicaLeds(listaPinesSalida);
      break;

    case '1':
      digitalWrite(15, HIGH);
      desactivarLeds(c, listaPinesSalida);
      Serial.println("Seleccion 1: LED pin 15 encendido fijo");
      break;

    case '2':
      digitalWrite(2, HIGH);
      desactivarLeds(c, listaPinesSalida);
      Serial.println("Seleccion 2: LED pin 2 encendido fijo");
      break;
    
    case '3':
     digitalWrite(4, HIGH);
      desactivarLeds(c, listaPinesSalida);
      Serial.println("Seleccion 4: LED pin 4 encendido fijo");
     break;

    default: 
      Serial.print("Comando no valido: ");
      Serial.println(c);
      Serial.println("Usar 0, 1, 2, 3, 4, 6, 7, 8 o q");
      break;
  }
}


void desactivarLeds(char c, int listaPinesSalida[8]){
  int valor = c - '0';
  for (int i = 0; i < 8; i++) {
    if (listaPinesSalida[i] != valor){
      digitalWrite(listaPinesSalida[i], LOW);
      delay(500);
    }
  }
}


void activarSecuenciaBasicaLeds(int listaPinesSalida[8]){
  for (int i = 0; i < 8; i++) {
          revisaryActivarDesactivarFuncionBoton(listaPinesSalida);
          digitalWrite(listaPinesSalida[i], HIGH);
          delay(500);
          digitalWrite(listaPinesSalida[i], LOW);
  }
  for (int i = 8; i > 0; i--) {
          revisaryActivarDesactivarFuncionBoton(listaPinesSalida);
          digitalWrite(listaPinesSalida[i], HIGH);
          delay(500);
          digitalWrite(listaPinesSalida[i], LOW);
  }
}

void revisaryActivarDesactivarFuncionBoton(int listaPinesSalida[8]){
  int EstadoBoton = digitalRead(pinEntradaPulsador);
  if(EstadoBoton == HIGH){
    for(int i = 0; i < 8 ; i +=2){
      digitalWrite(listaPinesSalida[i], HIGH);
    }
  }
  else{
    for(int i = 0; i < 8 ; i +=2){
      digitalWrite(listaPinesSalida[i], LOW);
    }
  }
}
