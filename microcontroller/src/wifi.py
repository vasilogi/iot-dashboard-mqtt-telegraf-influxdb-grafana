import network
import time


class Wifi:
    def __init__(self):
        pass

    @staticmethod
    def connect(ssid, password):
        # Create a WLAN object
        wlan = network.WLAN(network.STA_IF)
        # Activate the WLAN interface
        wlan.active(True)

        try:
            # Check if already connected
            if not wlan.isconnected():
                print("Connecting to the WiFi...")
                # Connect to the WiFi network
                wlan.connect(ssid, password)
                # Wait until connection is established
                while not wlan.isconnected():
                    print("Attempting to reconnect to the WiFi...")
                    time.sleep(1)

            print(f"Connected to: {ssid}")
            print(f"ESP32 IP Address: {wlan.ifconfig()[0]}")
        except Exception as e:
            print(f"Error occurred while connecting to WiFi: {e}")
