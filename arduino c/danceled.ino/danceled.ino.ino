int x = 100;
int y = 200;
int ledred = 13;
int ledyellow = 12;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledred, OUTPUT);
  pinMode(ledyellow, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledred, LOW);
  delay(x);
  digitalWrite(ledred, HIGH);
  delay(y);
  digitalWrite(ledred, LOW);
  delay(y);
  digitalWrite(ledred, HIGH);
  delay(y);
  digitalWrite(ledyellow, HIGH);
  delay(x);
  digitalWrite(ledyellow, LOW);
  delay(x);
  digitalWrite(ledyellow, HIGH);
  delay(x);
  digitalWrite(ledyellow, LOW);
  delay(x);
  digitalWrite(ledred, LOW);
  delay(x);
  digitalWrite(ledred, HIGH);
  delay(x);
  digitalWrite(ledred, HIGH);
  delay(y);
  digitalWrite(ledred, LOW);
  delay(y);
  digitalWrite(ledyellow, HIGH);
  delay(y);
  digitalWrite(ledyellow, LOW);
  delay(y);
  digitalWrite(ledyellow, HIGH);
  delay(y);
  digitalWrite(ledyellow, LOW);
  delay(y);
  digitalWrite(ledred, LOW);
  delay(x);
  digitalWrite(ledred, HIGH);
  delay(x);
}
