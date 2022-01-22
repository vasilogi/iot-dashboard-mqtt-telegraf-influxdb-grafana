# Read temperature and humidity data with an ESP32

from machine import Pin
from time import sleep
import dht

# define the sampling rate
rate = 2  # get data every 2 seconds

# define a dht object on the specified data pin
sensor = dht.DHT11(Pin(4))

# infinite loop

while True:
    try:
        # delay
        sleep(rate)
        # measure
        sensor.measure()
        # save readings
        T = sensor.temperature()
        h = sensor.humidity()
        # print readings
        print('temperature: %3.1f' % T)
        print('humidity: %3.1f' % h)
    except OSError as e:
        # System-related error
        print('Failed to read sensor...')
