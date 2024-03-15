import json

class ConfigReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config_data = self._read_config()

    def _read_config(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def get_wifi_config(self):
        return self.config_data['wifi']

    def get_mqtt_config(self):
        return self.config_data['mqtt']

    def get_microcontroller_config(self):
        return self.config_data['microcontroller']