# IMPORTS
import paho.mqtt.subscribe as subscribe
from gpiozero import LED

# VARIABLES AND OBJECTS
red = LED(17)

# FUNCTIONS
def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    status = message.payload.decode()

    if status == "taend":
        red.on()
    if status == "sluk":
        red.off()

# SCRIPT
print('Subscribe MQTT script running...')
subscribe.callback(on_message_print, "LED", hostname="20.13.128.184", userdata={"message_count": 0})