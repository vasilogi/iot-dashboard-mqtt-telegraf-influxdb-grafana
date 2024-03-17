# # Read temperature and humidity data with an ESP32
#
# from src.config_reader import ConfigReader
# from src.wifi import Wifi
# from src.sensor import Sensor
#
# if __name__ == "__main__":
#     # Instantiate ConfigReader
#     config = ConfigReader(file_path="config.json")
#
#     # Connect to the WiFi
#     Wifi.connect(config.wifi_ssid, config.wifi_password)
#
#     # Instantiate Sensor
#     sensor = Sensor(config.reading_pin, config.mqtt_broker, config.mqtt_tcp_port)
#
#     # Continuous Measurement
#     sensor.continuous_measurement(reading_frequency=config.reading_frequency,
#                                   temperature_topic=config.temperature_topic,
#                                   humidity_topic=config.humidity_topic)
#
