#include<ESP8266WiFi.h>
#include<WiFiClient.h>
#include<ESP8266HTTPClient.h>

const char *ssid = "SUNBEAM";
const char *password = "1010101010";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.flush();

  pinMode(A0, INPUT);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi");
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(500);
  }
  
  Serial.println("WiFi is connected !!!");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());

}

void loop() {
  // put your main code here, to run repeatedly:
  float value = analogRead(A0);
  String body = "{ \"location\":\"Nira\", \"value\": " + String(value) + "}";
  Serial.println(body);

  WiFiClient wifi;
  HTTPClient httpClient;
  httpClient.begin(wifi, "http://172.18.4.155:4000/ldr");
  httpClient.addHeader("Content-type", "application/JSON");

  int status = httpClient.POST(body);
  Serial.println("Status : " + String(status));
  
  delay(10000);
}







