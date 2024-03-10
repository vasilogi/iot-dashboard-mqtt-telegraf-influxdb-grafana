# Read temperature and humidity data with an ESP32

from machine import Pin, unique_id
from time import sleep, time
import dht
from umqtt.simple import MQTTClient
import network
import ubinascii

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # Create a WLAN object
    wlan.active(True)  # Activate the WLAN interface

    if not wlan.isconnected():  # Check if already connected
        print("Connecting to WiFi...")
        wlan.connect(ssid, password)  # Connect to the WiFi network

        while not wlan.isconnected():  # Wait until connection is established
            time.sleep(1)

    print("Connected to WiFi:", ssid)
    print("IP Address:", wlan.ifconfig()[0])


# Network credentials
ssid = 'Vodafone-83EB_2.4GEXT'
password = 'tbReNTRaJPE4JD6b'

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

while True:
    try:
        # measure
        sensor.measure()
        # save readings
        T = sensor.temperature()
        h = sensor.humidity()
        # print readings
        print('temperature:', T)
        print('humidity:', h)
        print('timestamp:', time())
        # delay
        sleep(rate)
    except OSError as e:
        # System-related error
        print('Failed to read sensor...')

