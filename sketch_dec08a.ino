#include <Servo.h>

#define Servo_pin 5

Servo servo;
int x;
int y;
int prevX;
int prevY;

void setup() {
  Serial.begin(9600);
  servo.attach(Servo_pin);
  servo.write(90);
  Serial.println("setup()");
}

void servoPosition(){
  if(prevX != x){
    int servoX = map(x, 600, 0, 70, 179);
    servoX = min(servoX, 179);
    servoX = max(servoX, 70);
    servo.write(servoX);
  }
}

void loop() {
  if(Serial.available()>0){
      x = Serial.parseInt();
      Serial.println(x);
      servoPosition();
      
    }
    while(Serial.available()> 0){
      Serial.read();
    }
    delay(1000);
}
