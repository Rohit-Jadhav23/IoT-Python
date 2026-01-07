#include<ESP8266WiFi.h>
#include<ESP8266HTTPClient.h>
#include<WiFiClient.h>

const char *ssid = "$dvd$";
const char *password = "dvd12345";

const char *server_IP = "192.168.233.172";
unsigned int port = 3000; 


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi");
  while(WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(1000);
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());

}

void loop() {
  // put your main code here, to run repeatedly:
  float value = analogRead(A0);

  // create a request boay - JSON
  String body = "{\"temperature\" : " + String(value) + ",\"name\" : \"NodeMCU1\", \"city\" : \"City1\", \"age\": 32}";
  Serial.println(body);

  char url[64];
  sprintf(url, "http://%s:%s/temperature", server_IP, port);

  WiFiClient client;
  HTTPClient HTTPclient;
  HTTPclient.begin(client, url);
  HTTPclient.addHeader("content-type", "Application/JSON");

  int statusCode = HTTPclient.POST(body);
  Serial.println("StatusCode : " + String(statusCode));
  HTTPclient.end();

  delay(10000);
}



