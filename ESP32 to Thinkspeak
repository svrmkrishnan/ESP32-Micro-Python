import wifict                                    #refer wifict program, i saved the wifi program in my machine
from umqtt.robust import MQTTClient
import time




t = 30
h = 40


myMqttClient = bytes("client_"+str(10), 'utf-8')

THINGSPEAK_URL = b"mqtt.thingspeak.com" 
THINGSPEAK_USER_ID = b'user id '
THINGSPEAK_MQTT_API_KEY = b'mqtt apk'
client = MQTTClient(client_id=myMqttClient, 
                    server=THINGSPEAK_URL, 
                    user=THINGSPEAK_USER_ID, 
                    password=THINGSPEAK_MQTT_API_KEY, 
                    ssl=False)
                    
client.connect()

THINGSPEAK_CHANNEL_ID = 'channel id'
THINGSPEAK_CHANNEL_WRITE_API_KEY = 'write api key'
 
while True:
    
    topic = bytes(("channels/"+ THINGSPEAK_CHANNEL_ID + "/publish/"+ THINGSPEAK_CHANNEL_WRITE_API_KEY),'utf-8')
    payload = bytes("field1="+str(t)+"&field2="+str(h),'utf-8')               
    client.publish(topic, payload)
    print(topic,payload)
    time.sleep(10)                                                            
    
    
      
    
        
      
       
        
        


