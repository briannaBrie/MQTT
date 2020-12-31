import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected to a broker")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subcribed to a topic")

def on_message(client, userdata, msg):
    print("Topic{}, message(={}".format(msg.topic, msg.payload))

def on_disconnect(client, userdata, rc):
    print("Disconnected from a broker")

client = mqtt.Client()
client.on_connect=on_connect
client.on_subscribe=on_subscribe
client.on_message=on_message
client.on_disconnect = on_disconnect
client.on_connect("127.0.0.1")
client.subscribe("ramps_test")
client.loop_forever()