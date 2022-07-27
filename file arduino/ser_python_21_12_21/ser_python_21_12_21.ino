int a,b,c,d,e;

void setup() {
  Serial.begin(115200);
  pinMode(2,INPUT);
//  pinMode(3,INPUT);
//  pinMode(4,INPUT);
//  pinMode(5,INPUT);
//  pinMode(6,INPUT);
 // a=0;
  
}

void loop() {
  a = digitalRead(2);
//  b = digitalRead(3);
//  c = digitalRead(4);
//  d = digitalRead(5);
//  e = digitalRead(6);
  sensor_a();
//  sensor_b();
//  sensor_c();
//  sensor_d();
//  sensor_e();
  delay(500);
}

void sensor_a(){
  if(a==1){
    Serial.write('1');
//    Serial.println("S1 off");
  }
  else{
    Serial.write('9');    
//    Serial.println("S1 On");
  } 
}
