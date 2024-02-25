from influxdb_client_3 import InfluxDBClient3


# token = os.environ.get("INFLUXDB_TOKEN")
TOKEN = "MrRgAwHoCrffzIGzh9Dy9tvVRlpFncT9jngEppglb24tLNWUXT0WpZhMHAc4INgmXgANIXbhes0d3j49__Fk5Q=="
ORG = "homeauto"
URL = "http://localhost:8086"

client = InfluxDBClient3(url=URL, token=TOKEN, org=ORG)

BUCKET="default"

# table = client.query("SELECT * FROM measurement1")

# print(table)