# Read temperature and humidity data with an ESP32

from src.config_reader import ConfigReader
from src.sensor import Sensor
from src.time import CustomTime
import time


def main():
    # Instantiate ConfigReader
    config = ConfigReader(file_path="config.json")

    # Instantiate Sensor
    sensor = Sensor(config.reading_pin, config.mqtt_broker, config.mqtt_tcp_port)

    # Synchronize with NTP
    CustomTime.sync_with_ntp()

    # Give some time to the sensor to stabilize
    time.sleep(2)

    # Continuous Measurement
    sensor.continuous_measurement(reading_frequency=config.reading_frequency,
                                  temperature_topic=config.temperature_topic,
                                  humidity_topic=config.humidity_topic)


if __name__ == "__main__":
    main()
