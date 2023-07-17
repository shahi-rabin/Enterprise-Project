mport time
import board
import adafruit_dht
import spidev
import paho.mqtt.client as mqtt

# ThingsBoard MQTT Broker details
THINGSBOARD_HOST = 'your-thingsboard-host'  # Replace with your ThingsBoard host
ACCESS_TOKEN = 'your-access-token'  # Replace with your device access token

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

# Main loop to read data from sensors and publish to ThingsBoard
while True:
    try:
        # Read data from the DHT11 sensor
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("DHT11 Sensor - Temp: {:.1f} F / {:.1f} C    Humidity: {}%".format(
            temperature_f, temperature_c, humidity
        ))

        # Publish DHT11 sensor data to ThingsBoard
        client.publish('v1/devices/me/telemetry', '{{"temperature": {:.2f}, "humidity": {:.2f}}}'.format(
            temperature_c, humidity))

        # Read data from the LDR sensor
        ldr_channel = 1  # Channel number for LDR in MCP3008
        ldr_raw_value = read_adc(ldr_channel)  # Read analog value from LDR channel

        # Logic for LDR sensor output
        if ldr_raw_value < 10:
            ldr_output = 1  # Output is 1 if raw value is less than 10
        else:
            ldr_output = 0  # Output is 0 if raw value is 10 or more

        print("LDR Sensor - Raw Value:", ldr_raw_value)
        print("LDR Sensor - Output:", ldr_output)

        # Publish LDR sensor data to ThingsBoard
        client.publish('v1/devices/me/telemetry', '{{"light": {:.2f}, "output": {}}}'.format(ldr_raw_value, ldr_output))

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])

    # Delay before taking the next sensor readings and publishing
    time.sleep(5)
``
