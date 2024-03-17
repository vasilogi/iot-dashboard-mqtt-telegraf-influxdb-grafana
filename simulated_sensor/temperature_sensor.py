import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime
import random


# Read configuration from JSON file
def read_config(filename):
    with open(filename, "r") as f:
        config = json.load(f)
    return config


# Generate random temperature data
def generate_temperature():
    # Replace this with your logic to generate a more realistic temperature value
    return round(20 + (5 * random.random()), 2)


# MQTT callback function
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


# Main function
if __name__ == "__main__":
    # Read configuration
    broker_config = read_config("broker_config.json")  # Replace with your filename

    sensor_id = f'{random.randint(0, 1000)}'

    # Initialize MQTT client
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.on_connect = on_connect

    # Connect to MQTT broker
    mqtt_client.connect(broker_config["broker"], broker_config["ports"]["tcp"], 60)
    mqtt_client.loop_start()

    try:
        while True:
            # Generate temperature data
            temperature = generate_temperature()
            timestamp = datetime.now().isoformat()

            # Prepare message payload
            payload = {
                "id": sensor_id,
                "value": temperature,
                "timestamp": timestamp
            }

            # Convert payload to JSON string
            message = json.dumps(payload)

            # Publish message to MQTT topic
            mqtt_client.publish(topic="hivemq/free/public/mqtt/temperature", payload=message)

            # Simulate sensor reading interval
            time.sleep(5)  # Adjust sleep time as needed

    except KeyboardInterrupt:
        pass

    finally:
        mqtt_client.loop_stop()
        mqtt_client.disconnect()
