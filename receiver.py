import json
import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "172.25.0.125"
broker_port = 1883
broker_username = "rabin"

# Define the callback function to handle incoming MQTT messages
def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode()
    print(f"Received message: {payload} on topic: {topic}")
    # Process the received data as needed
    # Example: Parse the JSON payload and perform actions based on the sensor data

# Create an MQTT client object and set the message callback
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)
client.username_pw_set(broker_username)

# Subscribe to the desired MQTT topic
client.subscribe("sensor/data")

# Start the MQTT loop in a separate thread
client.loop_start()

# Keep the script running
while True:
    pass

# Stop the MQTT loop and disconnect from the broker
client.loop_stop()
client.disconnect()
