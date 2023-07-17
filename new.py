import os
import time
import sys
import Adafruit_DHT as dht
import paho.mqtt.client as mqtt
import json
import board
import busio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

THINGSBOARD_HOST = 'localhost'
ACCESS_TOKEN = 'ljL4Q58gBLcrS0VBKnLj'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL = 2

sensor_data = {'temperature': 0, 'humidity': 0, 'dust': 0}

next_reading = time.time()

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

# Create SPI bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# Create MCP3008 ADC object
mcp = MCP.MCP3008(spi)

# Create analog input channels
channel_dust = AnalogIn(mcp, MCP.P0)  # Use the corresponding MCP3008 channel for the Vo pin

try:
    while True:
        humidity, temperature = dht.read_retry(dht.DHT11, 2)
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
        sensor_data
