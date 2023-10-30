#include <Arduino.h>
#include <Ultrasonic.h>
#include <Servo.h>

#define PIN_ESC 3
#define ANALOG_READ_PIN A0
#define TRIGGERPINULTRA 10
#define ECHOPINULTRA 11

Ultrasonic ultrasonic(TRIGGERPINULTRA, ECHOPINULTRA);
Servo servo;

void setup()
{
  Serial.begin(9600);
  servo.attach(PIN_ESC);

  pinMode(ANALOG_READ_PIN, INPUT);

  servo.writeMicroseconds(1000);
}

void loop()
{
  unsigned char type, port, value;

  while (Serial.available())
  {
    type = Serial.read();

    switch (type)
    {
    case '1':
      Serial.println(ultrasonic.read());
      break;

    case '2':
      Serial.println(analogRead(ANALOG_READ_PIN));
      break;

    case '3':
      while (!Serial.available())
        delay(1);

      port = Serial.read();

      pinMode(port, INPUT);
      break;

    case '4':
      while (!Serial.available())
        delay(1);

      port = Serial.read();

      pinMode(port, OUTPUT);
      break;

    case '5':
      while (Serial.available() < 2)
        delay(1);

      port = Serial.read();
      value = Serial.read();

      digitalWrite(port, value == '1' ? HIGH : LOW);
      break;

    case '6':
      while (!Serial.available())
        delay(1);

      value = Serial.read();

      if (value > 100)
        value = 100;

      servo.writeMicroseconds((((int)value) * 10) + 1000);
      break;

    case 'r':
    default:
      break;
    }
  }
}