# LocalWeather-Reader

## Wiring

In the image below it is explained how exactly the DHT11 sensor connects to ESP32.

![wiring_illustration](/Documentation/images/wiring_illustration.png)

find the umqtt library here

https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/umqtt/simple.py

## telegraf

docker run --rm telegraf telegraf config > telegraf.conf


https://hub.docker.com/_/telegraf


Telegraf is an agent that is collecting, processing, aggregating and sending metrics of a machine
that we want to monitor to various outputs like influxdb, graphite, kafka, etc.

InfluxDB is an open-source time series database written in Go.

Grafana is an open-source data visualization and monitoring suite.