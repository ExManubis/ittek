import paho.mqtt.publish as publish

publish.single("paho/test/topic", "payload", hostname="20.13.128.184")