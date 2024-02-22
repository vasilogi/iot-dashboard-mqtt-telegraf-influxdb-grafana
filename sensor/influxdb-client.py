import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# token = os.environ.get("INFLUXDB_TOKEN")
token = "MrRgAwHoCrffzIGzh9Dy9tvVRlpFncT9jngEppglb24tLNWUXT0WpZhMHAc4INgmXgANIXbhes0d3j49__Fk5Q=="
org = "homeauto"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="default"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(10):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="homeauto", record=point)
  time.sleep(1) # separate points by 1 second