# import paho mqtt client
import paho.mqtt.client as mqtt

# define a on_message callback
def on_message(client, userdata, message):
    print(f"Topic : {message.topic}. Received msg : {message.payload}")

# create an instance of Client
subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# register on_message callback for created client
subscriber.on_message = on_message

# connect with broker
#subscriber.connect("localhost")
subscriber.connect("mqtt.eclipseprojects.io");

# subscribe for the topic
subscriber.subscribe("home/test")

# wait for the messages
subscriber.loop_forever()