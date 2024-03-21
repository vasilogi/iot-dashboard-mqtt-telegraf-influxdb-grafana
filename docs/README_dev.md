# LocalWeather-Reader

## Wiring

In the image below it is explained how exactly the DHT11 sensor connects to ESP32.

![wiring_illustration](/Documentation/images/wiring_illustration.png)

find the umqtt library here

https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/umqtt/simple.py

## telegraf

generate a config file

docker run --rm telegraf telegraf config > telegraf.conf


https://hub.docker.com/_/telegraf

plugins

https://github.com/influxdata/telegraf/tree/master/plugins


Telegraf is an agent that is collecting, processing, aggregating and sending metrics of a machine
that we want to monitor to various outputs like influxdb, graphite, kafka, etc.

InfluxDB is an open-source time series database written in Go.

Grafana is an open-source data visualization and monitoring suite.

# MQTT

https://github.com/eclipse/paho.mqtt.python?tab=readme-ov-file#getting-started

## esp 32

sudo apt-get install picocom
https://www.youtube.com/watch?v=fmgQ8Dcg9uM
https://docs.micropython.org/en/latest/esp32/quickref.html#installing-micropython
https://micropython.org/download/ESP32_GENERIC/


the ESP32 can retrieve the exact time and date with just an Internet connection.
As soon as the ESP32 is completely turned off, it loses track of time. It is like an oven or microwave clock that
displays 00:00 when there was a power failure. The most classical way is then to use an external RTC with a battery permanently connected

Synchronizing the clock is very useful when the ESP32 wakes up from time to time to communicate with WEB services,
and wants to date its packets with the right date. It can also be useful to have an alarm clock that executes a task at a specific time.

