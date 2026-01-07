void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  float value = analogRead(A0);
  Serial.printf("Sensor value : %f\n", value);
  delay(2000);
}
