import ubinascii
from umqtt.simple import MQTTClient
import dht
from machine import Pin, unique_id
import json
import time


class Sensor:
    """Class to interact with a DHT11 temperature and humidity sensor and publish readings to an MQTT broker."""

    def __init__(self, reading_pin, broker_ip, broker_port):
        """Initialize the Sensor object.

            Args:
                reading_pin (int): The pin to which the DHT11 sensor is connected.
                broker_ip (str): The IP address of the MQTT broker.
                broker_port (int): The port of the MQTT broker.
        """
        # the ESP unique ID
        self.client_id = ubinascii.hexlify(unique_id())
        # define a dht object on the specified data pin
        self.sensor = dht.DHT11(Pin(reading_pin))
        self.broker_ip = broker_ip
        self.broker_port = broker_port
        self.mqtt_client = MQTTClient(self.client_id, self.broker_ip, self.broker_port)
        pass

    def mqtt_connect(self):
        """Connect to the MQTT broker."""
        # connect to the MQTT broker
        try:
            self.mqtt_client.connect()
        except Exception as e:
            print(f"An unexpected error occurred while trying to connect to the MQTT broker: {e}")

    def construct_payload(self, variable_name, value, timestamp):
        """Construct a JSON payload for publishing sensor readings.

            Args:
                variable_name (str): The name of the variable being published (e.g., "temperature" or "humidity").
                value (float): The value of the sensor reading.
                timestamp (float): The timestamp of the reading.

            Returns:
                str: A JSON-encoded payload.
        """
        if variable_name == "temperature":
            payload = {
                "id": self.client_id,
                "temperature": value,
                "timestamp": timestamp
            }
            return json.dumps(payload)
        elif variable_name == "humidity":
            payload = {
                "id": self.client_id,
                "humidity": value,
                "timestamp": timestamp
            }
            return json.dumps(payload)
        else:
            print("Variable name is not correct.")

    def publish_payload(self, topic, payload):
        """Publish a payload to the MQTT broker.

            Args:
                topic (str): The MQTT topic to which the payload will be published.
                payload (str): The payload to publish.
        """
        self.mqtt_client.publish(topic, payload)
        return None

    def instant_reading(self):
        """Read sensor data instantly.

            Returns:
                tuple: A tuple containing the temperature (float), humidity (float), and timestamp (float).
        """
        # Start measuring
        self.sensor.measure()
        # Save readings
        temperature = self.sensor.temperature()
        humidity = self.sensor.humidity()
        timestamp = time.time()
        return temperature, humidity, timestamp

    def continuous_measurement(self, reading_frequency, temperature_topic, humidity_topic):
        """Perform continuous sensor measurements and publish readings to MQTT.

            Args:
                reading_frequency (int): The frequency (in seconds) at which readings are taken.
                temperature_topic (str): The MQTT topic for publishing temperature readings.
                humidity_topic (str): The MQTT topic for publishing humidity readings.
        """

        # connect to the MQTT broker
        self.mqtt_connect()

        print("Starting continuous measurement...")
        print(f"Connect to the MQTT broker at mqtt://{self.broker_ip}/{self.broker_port}")
        print(f"Temperature Topic: {temperature_topic}")
        print(f"Humidity Topic: {humidity_topic}")

        while True:
            try:
                # Get sensor readings
                temperature, humidity, timestamp = self.instant_reading()

                # Publish temperature
                self.publish_payload(topic=temperature_topic,
                                     payload=self.construct_payload(variable_name="temperature",
                                                                    value=temperature,
                                                                    timestamp=timestamp))
                # Publish humidity
                self.publish_payload(topic=humidity_topic,
                                     payload=self.construct_payload(variable_name="humidity",
                                                                    value=humidity,
                                                                    timestamp=timestamp))

                # Delay next reading
                time.sleep(reading_frequency)
            except OSError as e:
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
