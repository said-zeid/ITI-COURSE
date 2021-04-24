#define channel_A 2
#define channel_b 3
int counter=0;


void setup() {
  // put your setup code here, to run once:
  int counter=0;
  Serial.begin(9600);
  pinMode(channel_A,INPUT);
  pinMode(channel_b,INPUT);
  attachInterrupt(digitalPinToInterrupt(channel_A), Aisr, CHANGE);
  attachInterrupt(digitalPinToInterrupt(channel_b), Bisr, CHANGE);


}

void loop() {
  // put your main code here, to run repeatedly:
Serial.println(counter);
}
void Aisr() {
  if((( digitalRead(channel_A)==HIGH && digitalRead(channel_b)==LOW )||(digitalRead(channel_A)==LOW && digitalRead(channel_b)==HIGH))){
    counter++;
    }
    else{
      counter--;
      }
  
}
void Bisr() {
  if((( digitalRead(channel_A)==HIGH && digitalRead(channel_b)==HIGH )||(digitalRead(channel_A)==LOW && digitalRead(channel_b)==LOW))){
    counter++;
    }
    else{
      counter--;
      }
  
}
