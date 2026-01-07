void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.flush();

  delay(2000);
  Serial.println("serial port setup is done");
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("inside loop()");
  delay(2000);
}
