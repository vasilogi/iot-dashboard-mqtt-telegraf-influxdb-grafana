# IoT Dashboard: MQTT, Telegraf, InfluxDB, Grafana

This project demonstrates how to monitor the temperature and humidity using an ESP32 microcontroller connected to
a DHT11 sensor. The integrated Wi-Fi of ESP32 is utilized and the data is then transmitted via MQTT to the backend which
is hosted on a Raspberry Pi. The backend system consists of a local MQTT broker, Telegraf, InfluxDB, and Grafana
for visualization.

## Table of Contents

<!-- TOC -->
* [IoT Dashboard: MQTT, Telegraf, InfluxDB, Grafana](#iot-dashboard-mqtt-telegraf-influxdb-grafana)
  * [Table of Contents](#table-of-contents)
  * [Hardware Requirements](#hardware-requirements)
  * [Linux Development Environment](#linux-development-environment)
    * [Pre-requisites](#pre-requisites)
    * [Installation](#installation)
  * [ESP32 - DHT11 wiring](#esp32---dht11-wiring)
  * [Connect to the ESP32](#connect-to-the-esp32)
<!-- TOC -->

## Hardware Requirements

- [ESP32 System-on-a-Chip (SoC)](https://www.espressif.com/en/products/socs/esp32)
- [DHT11 - Temperature and Humidity Sensor](https://components101.com/sensors/dht11-temperature-sensor)

## Linux Development Environment

> This project has been developed using Debian 12 (bookworm).

Here, the set-up procedure for Linux systems will be described. However, it wouldn't be that different for Mac
or Windows OS.

### Pre-requisites

- [Python 3.12.2](https://www.python.org/downloads/release/python-3122/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Docker](https://docs.docker.com/engine/install/)
- [Pyenv](https://github.com/pyenv/pyenv) (optional)

> We recommend to use `pyenv` for installing and managing various Python version in simple way.

### Installation

1. Clone this repository to your local machine.

```shell
git clone https://github.com/vasilogi/LocalWeather-Reader.git 
```

2. Navigate inside the directory, containing the repository and create a Python virtual environment.

```shell
python -m venv .venv
```

3. Activate the virtual environment:

```shell
source .vevn/bin/activate
```

4. Install the necessary requirements.

```shell
pip install -r requirements.txt
```

## Hardware wiring

Connect the DHT11 sensor to the ESP32 board. The connections typically include VCC, GND, and data pins. Advice the
current configuration below:

![wiring_illustration](./images/wiring_illustration.png)


## Getting connected with the ESP32

### Powering the board

Your board has a micro USB connector on it, and it is powered through this when connected to your development machine.
Therefore, simply connect a micro USB cable to it.

### Downloading the MicroPython firmware

You can download the most recent MicroPython firmware **.bin file** to load onto your ESP32 device from the
[MicroPython downloads page](https://micropython.org/download/ESP32_GENERIC/). In this project, we are going to use the
[v.1.22.2](./esp32_firmware/ESP32_GENERIC-20240222-v1.22.2.bin).

### Flashing the MicroPython firmware into the ESP32

In your Python virtual environment that you have installed, we have included the `esptool.py` package.
You will use this open-source and platform-agnostic utility to communicate with the ROM bootloader in your ESP32 chip.
Thus, first activate the virtual environment as explained above in the [installation instructions](#installation).

Then, erase the flash memory by running the following command:

```shell
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
```

Upon success, you should be expecting a message like this:

```shell
esptool.py v4.7.0
Serial port /dev/ttyUSB0
Connecting.......
Chip is ESP32-D0WDQ6 (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 7c:9e:bd:61:5f:48
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 5.8s
Hard resetting via RTS pin...
```

Now, you are ready to flash the MicroPython firmware onto the ESP32 by running:

```shell
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 ./esp32_firmware/ESP32_GENERIC-20240222-v1.22.2.bin
```

You should be seeing in your terminal a similar to this message:

```shell
esptool.py v4.7.0
Serial port /dev/ttyUSB0
Connecting....
Chip is ESP32-D0WDQ6 (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 7c:9e:bd:61:5f:48
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 460800
Changed.
Configuring flash size...
Flash will be erased from 0x00001000 to 0x001a9fff...
Compressed 1737776 bytes to 1143554...
Wrote 1737776 bytes (1143554 compressed) at 0x00001000 in 25.8 seconds (effective 539.4 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

Super! You have successfully flashed the MicroPython firmware onto your ESP32!





