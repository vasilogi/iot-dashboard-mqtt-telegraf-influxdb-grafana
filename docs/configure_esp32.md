https://docs.micropython.org/en/latest/esp32/tutorial/intro.html

(.venv) leohnard@euler:~/Documents/GitHub/LocalWeather-Reader$ sudo esptool.py --port /dev/ttyUSB0 erase_flash
[sudo] password for leohnard: 
sudo: esptool.py: command not found
(.venv) leohnard@euler:~/Documents/GitHub/LocalWeather-Reader$ sudo -s
(failed reverse-i-search)`': ^C
root@euler:/home/leohnard/Documents/GitHub/LocalWeather-Reader# source .venv/bin/activate
(.venv) root@euler:/home/leohnard/Documents/GitHub/LocalWeather-Reader# esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py v4.7.0
Serial port /dev/ttyUSB0
Connecting.........
Detecting chip type... Unsupported detection protocol, switching and trying again...
Connecting......
Detecting chip type... ESP32
Chip is ESP32-D0WDQ6 (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 7c:9e:bd:61:5f:48
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 4.0s
Hard resetting via RTS pin...
(.venv) root@euler:/home/leohnard/Documents/GitHub/LocalWeather-Reader#

https://micropython.org/download/ESP32_GENERIC/

(.venv) root@euler:/home/leohnard/Documents/GitHub/LocalWeather-Reader# esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 ./ESP32/firmware/ESP32_GENERIC-20240222-v1.22.2.bin 
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
Wrote 1737776 bytes (1143554 compressed) at 0x00001000 in 25.8 seconds (effective 539.8 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
(.venv) root@euler:/home/leohnard/Documents/GitHub/LocalWeather-Reader# 



communicate with the board

mpy --help
Usage: ampy [OPTIONS] COMMAND [ARGS]...

  ampy - Adafruit MicroPython Tool

  Ampy is a tool to control MicroPython boards over a serial connection.
  Using ampy you can manipulate files on the board's internal filesystem and
  even run scripts.

Options:
  -p, --port PORT    Name of serial port for connected board.  Can optionally
                     specify with AMPY_PORT environment variable.  [required]
  -b, --baud BAUD    Baud rate for the serial connection (default 115200).
                     Can optionally specify with AMPY_BAUD environment
                     variable.
  -d, --delay DELAY  Delay in seconds before entering RAW MODE (default 0).
                     Can optionally specify with AMPY_DELAY environment
                     variable.
  --version          Show the version and exit.
  --help             Show this message and exit.

Commands:
  get    Retrieve a file from the board.
  ls     List contents of a directory on the board.
  mkdir  Create a directory on the board.
  put    Put a file or folder and its contents on the board.
  reset  Perform soft reset/reboot of the board.
  rm     Remove a file from the board.
  rmdir  Forcefully remove a folder and all its children from the board.
  run    Run a script and print its output.

