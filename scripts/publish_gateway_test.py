#MQTT PUBLISH DEMO
#publish two messages, to two different topics.

import paho.mqtt.publish as publish

publish.single("Ramps/is_valid", "yes", hostname = "test.mosquitto.org")
publish.single("Ramps/jasna", "will check validity", hostname = "test.mosquitto.org")
publish.single("Ramps/ana", "will send picture", hostname = "test.mosquitto.org")
publish.single("Ramps/take_picture", "yes", hostname="test.mosquitto.org")
print("Done")
