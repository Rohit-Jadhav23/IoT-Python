# import paho mqtt client
import paho.mqtt.client as mqtt

# define a on_publish callback
def on_publish(client, userdata, mid, reason_code, properties):
    print("Message is published\n")

# create an instance of mqtt Client
publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# register on_publish callback with this client
publisher.on_publish = on_publish

# connect with mqtt broker
# publisher.connect("localhost")
publisher.connect("mqtt.eclipseprojects.io")

# publish message on topic
publisher.publish("home/test", "Hello DESD")

# disconnect with broker
publisher.disconnect()