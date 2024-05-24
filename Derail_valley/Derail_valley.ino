
int throttle_pin = A0;
int combined_brake_pin = A1;
int reverser_pin = 52;

void setup() {
  Serial.begin(9600);
  pinMode(throttle_pin,INPUT);
  pinMode(combined_brake_pin,INPUT);
  pinMode(reverser_pin,INPUT_PULLUP);
 int reverser_reader = 0; 
}

void loop() {
  int throttle_reader =analogRead(throttle_pin);
  int combined_brake_reader = analogRead(combined_brake_pin);
  int reverser_reader;

  int throttle = map(throttle_reader,0,1023,0,10);
  int train_brake =map(combined_brake_reader,0,1023,0,12);
  int ind_brake = train_brake-4;
  if (ind_brake < 0) ind_brake = 0;

  if (digitalRead(reverser_pin) == LOW )
  {
    reverser_reader = reverser_reader + 1;
  }
  if (digitalRead(reverser_pin) == HIGH )
  {
    reverser_reader = 0;
  }
  

Serial.print(throttle);
Serial.print(" ");
Serial.print(train_brake);
Serial.print(" ");
Serial.print(ind_brake);
Serial.print("\n");


}
