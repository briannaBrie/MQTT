#write a python app that will subscribe to a telemetry data from ESP32 ramp sensor.
#Let it transform received data from your custom format to JSON format and then 
# just write it to log file(will send it to REST API later).
# Add a timestamp to your json

import paho.mqtt.client as mqtt
import requests
import json
from datetime import datetime
import os

def on_connect(client, userdata, flags, rc):
    print("connected to a broker")

    #def on_subscribe(client, userdata, mid, granted_qos):
    client.subscribe("Ramps/take_picture")#if yes take a picture of the number plate and send it to Azure on Rest API
    print("Subscribed to picture topics")
    client.subscribe("Ramps/is_valid")#change the message format and send it to arduino
    print("Subscribed to valid topic")
    client.subscribe("Ramps/#")#subscribes to all ramps/ topics
    print("Subscribed to all topics")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))#print the received topic name and topic data

    #if the topic is take_picture
    if(msg.payload == "take_picture"):
        print("Take a picture an then send it to ana")
    #if the topic is take_picture
    elif (msg.payload == "is_valid"):
        if("yes"):
            print("Vehicle validated")
        elif("no"):
            print("Vehicle not validated")
    """
    #payload = msg.payload.decode('utf-8')
    #parts = payload.split(',')
    #json_data={}
    #json_data['question'] = int(parts[0])
    #json_data['take_picture'] = int(parts[1])
    #json_data['createdon'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    #json_string = json.dumps(json_data)
    
    r=requests.post("test.mosquitto.org", headers=headers, data = msg.payload)
    if(r.status_code ==200):
        print('Saved to database')
    else:
        print("Error:"+str(r.status_code))
        #to write to the log file
    with open('home/pi/telemetry.log','a+') as f:
        f.write(msg.payload)
        f.write('\n')
        #to send data to REST API
        r=requests.post("test.mosquitto.org", headers=headers, data = msg.payload)
    """

def on_disconnect(clietn,userdata,rc):
    print('Disconnected from a broker')

#Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
#client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect('test.mosquitto.org', 1883, 60)
#client.subscribe('home/pi/Documents/telemetry.log')
client.loop_forever()



