#include <dht.h>

int data;
dht DHT;

#define DHT11_PIN 7

void setup() 
{ 
  Serial.begin(9600); 
}
 
void loop() 
{

  
while (Serial.available())
  {
    data = Serial.read();
  }

  int chk = DHT.read11(DHT11_PIN);
  //Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  //Serial.print("Humidity = ");
  Serial.println(DHT.humidity);
  delay(2000);
}
