#include <Servo.h>

Servo s;

void setup() {
  Serial.begin(9600);
  s1.attach(9);
  s2.attach(10);
  s3.attach(11);
}

void loop() {
  if (Serial.available()) {
    // Read full line until newline
    String data = Serial.readStringUntil('\n');

    // Find commas
    int c1 = data.indexOf(',');
    int c2 = data.indexOf(',', c1 + 1);

    // Extract values
    int x = data.substring(0, c1).toInt();
    int y = data.substring(c1 + 1, c2).toInt();
    int z = data.substring(c2 + 1).toInt();

    // Use values
    s.write(x);  // Servo angle
    s2.write(y);
    s3.write(z);
  }
}