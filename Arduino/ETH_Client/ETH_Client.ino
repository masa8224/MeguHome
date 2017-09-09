#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
byte mac[] = {  
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192, 168, 88, 246);
unsigned int localPort = 8888;      
EthernetUDP Udp;
char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; 
void setup() {  
  pinMode(13,OUTPUT);
  Serial.begin(9600);
  Ethernet.begin(mac,ip);
  Serial.println(Ethernet.localIP()) 
  Udp.begin(localPort);
  Serial.println("Complete");
}
void loop() {
  int packetSize = Udp.parsePacket();
    Udp.read(packetBuffer,UDP_TX_PACKET_MAX_SIZE);
    String command(packetBuffer);    
    if (command.indexOf("on")>0){
      digitalWrite(13,HIGH);
    }
    if (command.indexOf("off")>0){
      digitalWrite(13,LOW);
    }    
    memset(packetBuffer, 0, sizeof(packetBuffer));

}
