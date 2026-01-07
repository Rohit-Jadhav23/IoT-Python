#include<WiFiClient.h>
#include<ESP8266WiFi.h>
#include<ESP8266WebServer.h>

const char *ssid = "$dvd$";
const char *password = "dvd12345";

ESP8266WebServer webServer(80);

void welcome(){
  webServer.send(200, "text/html", "Welcome to NodeMCU Web Server");
}

void led_on(){
  digitalWrite(D0, LOW);
  webServer.send(200, "text/html", "LED is Turned ON");
}

void led_off(){
  digitalWrite(D0, HIGH);
  webServer.send(200, "text/html", "LED is Turned OFF");
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.flush();

  pinMode(D0, OUTPUT);
  digitalWrite(D0, HIGH);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.println("Connecting to a WiFi");
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(500);
  }

  Serial.println("\n WiFi is connected");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());

  webServer.on("/welcome", HTTP_GET, welcome);
  webServer.on("/ledon", HTTP_GET, led_on);
  webServer.on("/ledoff", HTTP_GET, led_off);

  webServer.begin();
  Serial.println("Web Server is started");
}

void loop() {
  // put your main code here, to run repeatedly:
  webServer.handleClient();
}




