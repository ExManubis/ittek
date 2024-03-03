import paho.mqtt.subscribe as subscribe

print('Subscribe MQTT script running...')

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    userdata["message_count"] += 1
    if userdata["message_count"] >= 5:
        # it's possible to stop the program by disconnecting
        client.disconnect()

subscribe.callback(on_message_print, "paho/test/topic", hostname="20.13.128.184", userdata={"message_count": 0})