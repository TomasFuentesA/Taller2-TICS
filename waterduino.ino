#include <Servo.h>

Servo palanca;

int grados;

int baselineTemp = 0;
int celsius = 0;
int fahrenheit = 0;

int Intensidad = 0;
int luzOut = 0;
int pinFoto = A1;
int pinLed = 2;

int pinLed2 = 3;
int pinTMP = 0;
float valorTMP = 0;


int cm1 = 0;
int const pinD1= 5;
int cm2 = 0;
int const pinD2= 6;
float caudal;
float largo_tubo = 0.5;
float diametro = 0.04;
float radio;
float area;
float pi=3.1416;

int tiempo_riego = 15;
float consumo;

long readUltrasonicDistance(int pin)
{
  pinMode(pin, OUTPUT);  
  digitalWrite(pin, LOW);
  delayMicroseconds(2);
  digitalWrite(pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(pin, LOW);
  pinMode(pin, INPUT);
  return pulseIn(pin, HIGH);
}

void setup()
{
  pinMode(A0, INPUT);Serial.begin(9600); //Sensor de temp

  pinMode(A1, INPUT); //Fotoresistencia	
  pinMode(pinLed, OUTPUT); //Sensor de humedad
  
  pinMode(pinLed2, OUTPUT);
  
  Serial.begin(9600);
  digitalWrite(pinLed2, LOW);
  palanca.attach(4);
  
}
void loop()
{ 
  cm1 = 0.01723 * readUltrasonicDistance(pinD1);
  cm2 = 0.01723 * readUltrasonicDistance(pinD2);
  valorTMP= analogRead(pinTMP);
  Intensidad = analogRead(pinFoto);
  
  luzOut = ((long)Intensidad*1000*10)/((long)15*10*(1024 - Intensidad));
  luzOut = map(luzOut,3,1298,0,100);

  celsius = round(((5*valorTMP*100)/1024)-50);
  Serial.print("La intensidiad de la luz es: ");
  Serial.print(luzOut);
  Serial.print('\n');
  Serial.print("La temperatura es: ");
  Serial.print(celsius);
  Serial.print('\n');
  
  
  
  if(Intensidad > 500 and valorTMP > 125 and valorTMP <= 160){ 
  	digitalWrite(pinLed, HIGH);
    digitalWrite(pinLed2, HIGH);//Si hay luz ambiente prende el bombillo
    Serial.print("Condiciones optimas para el riego");
    Serial.print('\n');
    
    delay(5000);
    grados = 90; //map(analogRead(A2), 0, 1023, 0, 180);
  	palanca.write(grados);
    radio = diametro/2;
    area = pi*radio*radio;
    caudal = ((area*largo_tubo)/0.1);
    consumo = caudal*tiempo_riego*60;
    Serial.print("El caudal es: ");
    Serial.print(consumo);
    Serial.print('\n');
    
    } 
 else {
    
  	digitalWrite(pinLed, LOW);
    digitalWrite(pinLed2, LOW);//Si no hay luz ambiente apaga el bombillo
  	grados = 0;
  	palanca.write(grados);
    delay(5000);
  }
}