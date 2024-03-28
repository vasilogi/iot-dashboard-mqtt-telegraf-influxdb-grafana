import ntptime


class CustomTime:
    def __init__(self):
        pass

    @staticmethod
    def sync_with_ntp():
        try:
            ntptime.settime()
            print("Time synchronized with NTP server")
        except Exception as e:
            print(f"Error while syncing time with NTP server: {e}")
