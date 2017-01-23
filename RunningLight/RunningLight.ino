uint8_t pin;

void setup()
{
  for (pin = 2; pin < 20; pin++) {
    pinMode(pin, OUTPUT);
  }
}

void loop()
{
  for (pin = 2; pin < 20; pin++) {
    digitalWrite(pin, HIGH);
    delay(100);
    digitalWrite(pin, LOW);
  }
}
