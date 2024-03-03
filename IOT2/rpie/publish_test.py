import paho.mqtt.publish as publish
import json

while True:
    payload = input('Input message: \n')
    publish.single("paho/test/topic", payload, hostname="20.13.128.184")