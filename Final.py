import time
import board
import adafruit_dht
import spidev
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

# ThingsBoard MQTT Broker details
THINGSBOARD_HOST = 'localhost'  # Replace with your ThingsBoard host
ACCESS_TOKEN = 'ljL4Q58gBLcrS0VBKnLj'  # Replace with your device access token

# Create an instance of the SPI device
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0
spi.max_speed_hz = 1000000  # Set SPI speed (optional)

# Create an instance of the DHT11 sensor
dhtDevice = adafruit_dht.DHT11(board.D2)

# Function to read ADC value from MCP3008
def read_adc(channel):
    # MCP3008 operates in single-ended mode, so use channel number from 0 to 7
    assert 0 <= channel <= 7, 'ADC channel must be 0-7'
    # Create SPI message
    msg = [1, (8 + channel) << 4, 0]
    # Transfer SPI message and receive response
    response = spi.xfer2(msg)
    # Extract ADC value from response
    value = ((response[1] & 3) << 8) + response[2]
    return value

# Create an instance of the MQTT client
client = mqtt.Client()

# Connect to ThingsBoard MQTT Broker
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)

# GPIO pin for controlling the output
GPIO_PIN = 16

# Configure GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

# Main loop to read data from sensors and publish to ThingsBoard
while True:
    try:
        # Read data from the DHT11 sensor
        temperature_c = None
        humidity = None
        try:
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
        except RuntimeError as error:
            print(error.args[0])

        if temperature_c is not None:
            temperature_f = temperature_c * (9 / 5) + 32
            print("DHT11 Sensor - Temp: {:.1f} F / {:.1f} C    Humidity: {}%".format(
                temperature_f, temperature_c, humidity
            ))
        else:
            print("Failed to retrieve temperature data from the DHT sensor.")

        # Read data from the dust sensor
        dust_channel = 1  # Channel number for dust sensor in MCP3008
        dust_raw_value = read_adc(dust_channel)  # Read analog value from dust sensor channel
        # Perform any necessary calibration or processing on dust_raw_value
        # Use the calibrated value to determine the dust readings
        print("Dust Sensor - Raw Value:", dust_raw_value)

        # Publish dust sensor data to ThingsBoard
        client.publish('v1/devices/me/telemetry', '{{"dust": {:.2f}}}'.format(dust_raw_value))

        # Read data from the LDR sensor
        ldr_channel = 0  # Channel number for LDR in MCP3008
        ldr_raw_value = read_adc(ldr_channel)  # Read analog value from LDR channel
        # Perform any necessary calibration or processing on ldr_raw_value
        # Use the calibrated value to determine the light level
        print("LDR Sensor - Raw Value:", ldr_raw_value)

        # Publish LDR sensor data to ThingsBoard
        client.publish('v1/devices/me/telemetry', '{{"light": {:.2f}}}'.format(ldr_raw_value))

        # Determine bulb state based on LDR output
        if ldr_raw_value < 500:
            bulb_state = "on"
        else:
            bulb_state = "off"

        # Print bulb state
        print("Bulb state:", bulb_state)

        # Control GPIO pin based on LDR output
        if bulb_state == "on":
            GPIO.output(GPIO_PIN, GPIO.HIGH)  # Set GPIO pin to HIGH
        else:
            GPIO.output(GPIO_PIN, GPIO.LOW)  # Set GPIO pin to LOW

        # Publish LDR sensor data and bulb state to ThingsBoard
        client.publish('v1/devices/me/telemetry', '{{"light": {:.2f}, "bulb_state": "{}"}}'.format(ldr_raw_value, bulb_state))

    except KeyboardInterrupt:
        break

    # Delay before taking the next sensor readings and publishing
    time.sleep(5)

# Cleanup GPIO on program exit
GPIO.cleanup()

