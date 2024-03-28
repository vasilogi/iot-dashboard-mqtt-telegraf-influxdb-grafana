import json


class ConfigReader:
    """A class for reading configuration data from a JSON file."""
    def __init__(self, file_path):
        """
            Initialize ConfigReader object with the file path.

            Parameters:
            - file_path (str): The path to the JSON configuration file.
        """
        self.file_path = file_path
        self.data = self._read_config()

    def _read_config(self):
        """
            Read the configuration data from the JSON file.

            Returns:
            - dict: A dictionary containing the configuration data.
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)

    @property
    def wifi_password(self):
        """
            Retrieve the Wi-Fi password from the configuration.

            Returns:
            - str or None: The Wi-Fi password if available, None otherwise.
        """
        return self.data.get('wifi', {}).get('password', None)

    @property
    def wifi_ssid(self):
        """
            Retrieve the Wi-Fi SSID from the configuration.

            Returns:
            - str or None: The Wi-Fi SSID if available, None otherwise.
        """
        return self.data.get('wifi', {}).get('ssid', None)

    @property
    def mqtt_broker(self):
        """
            Retrieve the MQTT broker from the configuration.

            Returns:
            - str or None: The MQTT broker if available, None otherwise.
        """
        return self.data.get('mqtt', {}).get('broker', None)

    @property
    def mqtt_tcp_port(self):
        """
            Retrieve the MQTT TCP port from the configuration.

            Returns:
            - int or None: The MQTT TCP port if available, None otherwise.
        """
        return self.data.get('mqtt', {}).get('ports', {}).get('tcp', None)

    @property
    def temperature_topic(self):
        """
            Retrieve the MQTT temperature topic from the configuration.

            Returns:
            - str or None: The temperature topic if available, None otherwise.
        """
        base_topic = self.data.get('mqtt', {}).get('topics', {}).get('base_topic', None)
        temperature = self.data.get('mqtt', {}).get('topics', {}).get('temperature', None)
        return base_topic + temperature

    @property
    def humidity_topic(self):
        """
            Retrieve the MQTT humidity topic from the configuration.

            Returns:
            - str or None: The humidity topic if available, None otherwise.
        """
        base_topic = self.data.get('mqtt', {}).get('topics', {}).get('base_topic', None)
        temperature = self.data.get('mqtt', {}).get('topics', {}).get('humidity', None)
        return base_topic + temperature

    @property
    def reading_frequency(self):
        """
            Retrieve the reading frequency from the configuration.

            Returns:
            - int or None: The reading frequency if available, None otherwise.
        """
        return self.data.get('microcontroller', {}).get('reading_frequency', None)

    @property
    def reading_pin(self):
        """
            Retrieve the reading frequency from the configuration.

            Returns:
            - int or None: The reading frequency if available, None otherwise.
        """
        return self.data.get('microcontroller', {}).get('reading_pin', None)


