# Read temperature and humidity data with an ESP32

from machine import Pin, unique_id
from time import sleep, time
import dht
from umqtt.simple import MQTTClient
import network
import ubinascii


# Network credentials
ssid = 'Vodafone-14FD'
password = '3p&uA_ZrUEXPcw489N%@'

# connect to network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

# check if the connection is successful
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

# MQTT Broker
broker_ip = 'broker.hivemq.com'
topic_publish = b'temperature'

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


