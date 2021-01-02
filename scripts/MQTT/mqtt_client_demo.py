#MQTT Client demo
#Continuosly monitor two different MQTT topics for data
#check if the received data matches two predefined commands

import paho.mqtt.client as mqtt

#the callback for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags,rc):
    print("connected with the result code"+str(rc))

    #Subscribing on on_connect() - if we lose connection and 
    #reconnect then subscriptions will be renewed.
    #we are subscribed to two topics 
    client.subscribe("Ramps/jasna")
    client.subscribe("Ramps/ana")

#The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))#print the received topic name and topic data

    #if the topic is hello
    if(msg.payload == "Hello"):
        print("Received message #1, do something")
        #received some responses from Jasna
        #here you can now and the behaviour if jasna asks you to take a picture or not
        #then send the picture to Ana 
    #if the topic is hello
    if(msg.payload == "World"):
        print("Receieved message #2, do something")
        #received some responses from Ana
        #here you can first convert the data to a readable format then you can send the data
        #to jasna

#Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect=on_connect #everytime a client is connected the on_connect routine is called
client.on_message=on_message #everytime a client receives a message the on_message routine is called

client.connect("test.mosquitto.org", 1883,60)

#Process network traffic and dispatch callbacks. This with also handle reconnecting
#There are other loop*()functions made available. 
#Check the documentation at https://github.com/eclipse/paho.mqtt.python
client.loop_forever()