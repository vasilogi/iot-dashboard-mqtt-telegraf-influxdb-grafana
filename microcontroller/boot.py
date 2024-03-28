# Read temperature and humidity data with an ESP32

from src.config_reader import ConfigReader
from src.wifi import Wifi

# Instantiate ConfigReader
config = ConfigReader(file_path="config.json")

# Connect to the WiFi
Wifi.connect(config.wifi_ssid, config.wifi_password)

# Execute main.py every time the board is powered up or reset
exec(open('main.py').read())
