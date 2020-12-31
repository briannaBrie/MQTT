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

    #if yes take a picture of the number plate and send it to Azure on Rest API
    client.subscribe("Ramps/take_picture")
    print("Subscribed to picture topics")
    client.subscribe("Ramps/is_valid")
    print("Subscribed to valid topic")
    client.subscribe("Ramps/#")
    print("Subscribed to all topics")

def on_message(client, userdata, msg):
    #print the received topic name and topic data
    print(msg.topic+" "+str(msg.payload))

    #if the topic is take_picture
    if(msg.payload == "take_picture"):
        print("Take a picture an then send it to ana")
    #if the topic is take_picture
    elif (msg.payload == "is_valid"):
        if("yes"):
            print("Vehicle validated")
        elif("no"):
            print("Vehicle not validated")

def on_disconnect(clietn,userdata,rc):
    print('Disconnected from a broker')

#Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect('test.mosquitto.org', 1883, 60)
client.loop_forever()



