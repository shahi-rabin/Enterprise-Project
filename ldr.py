import time
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

# Exponential Moving Average (EMA) filter parameters
ALPHA = 0.2  # Smoothing factor (0 < ALPHA < 1)
ema_value = None

# Main loop to read data from the LDR sensor and publish to ThingsBoard
while True:
    try:
        # Read data from the LDR sensor
        ldr_channel = 0  # Channel number for LDR in MCP3008
        ldr_raw_value = read_adc(ldr_channel)  # Read analog value from LDR channel
        
        # Apply EMA filter to smooth the LDR raw value
        if ema_value is None:
            ema_value = ldr_raw_value
        else:
            ema_value = ALPHA * ldr_raw_value + (1 - ALPHA) * ema_value

        # Perform any necessary calibration or processing on ema_value
        print("LDR Sensor - EMA Value:", ema_value)

        # Determine bulb state based on EMA filtered value
        if ema_value < 500:
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
        client.publish('v1/devices/me/telemetry', '{{"light": {:.2f}, "bulb_state": "{}"}}'.format(ema_value, bulb_state))

    except KeyboardInterrupt:
        break

    # Delay before taking the next sensor reading and publishing
    time.sleep(5)

# Cleanup GPIO on program exit
GPIO.cleanup()
