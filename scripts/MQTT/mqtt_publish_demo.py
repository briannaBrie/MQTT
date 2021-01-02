#MQTT PUBLISH DEMO
#publish two messages, to two different topics.

import paho.mqtt.publish as publish

publish.single("Ramps/jasna", "Hello", hostname = "test.mosquitto.org")
publish.single("Ramps/ana", "World", hostname = "test.mosquitto.org")
print("Done")