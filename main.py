# Read temperature and humidity data with an ESP32

from machine import Pin, unique_id
import time
import dht
from umqtt.simple import MQTTClient
import network
import ubinascii
import json

def connect_to_wifi(ssid, password):
    # Create a WLAN object
    wlan = network.WLAN(network.STA_IF)
    # Activate the WLAN interface
    wlan.active(True)
    
    try:
        # Check if already connected
        if not wlan.isconnected():  
            print("Connecting to WiFi...")
            # Connect to the WiFi network
            wlan.connect(ssid, password)
            # Wait until connection is established
            while not wlan.isconnected():
                print("Attempting to reconnect to WiFi...")
                time.sleep(1)

        print(f"Connected to WiFi: {ssid}")
        print(f"IP Address: {wlan.ifconfig()[0]}")
    except Exception as e:
        print(f"Error occured while connecting to WiFi: {e}")


# Network credentials
ssid = 'Vodafone-83EB_2.4GEXT'
password = 'tbReNTRaJPE4JD6b'

# Connect to WiFi
connect_to_wifi(ssid, password)

# # MQTT Broker
# broker_ip = 'broker.hivemq.com'
# topic_publish = b'temperature'

# the ESP unique ID needed to create an MQTT client
client_id = ubinascii.hexlify(unique_id())

# define the sampling rate
# the sampling period in DHT11 is 1 sec
# while in DHT12 is 2 sec
rate = 2  # get data every 2 seconds

# define a dht object on the specified data pin
sensor = dht.DHT11(Pin(4))

# infinite loop
print("Starting infinite loop... \n")
  
while True:
    try:
        # Start measuring
        sensor.measure()
        # Save readings
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        timestamp = time.time()
        
        payload = {
            "id": client_id,
            "temperature": temperature,
            "humidity": humidity,
            "timestamp": timestamp
            }
        
        message = json.dumps(payload)
        
        print(message)
        # delay
        time.sleep(rate)
    except OSError as e:
        # Handle specific errors
        # Handle specific errors
        if e.errno == dht.DHT_ERROR_TIMEOUT:
            print("DHT sensor timed out.")
        elif e.errno == dht.DHT_ERROR_CHECKSUM:
            print("DHT checksum error.")
        else:
            print(f"Failed to read sensor: {e}")
        # System-related error
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")

