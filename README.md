# violin-jukebox
Violin Jukebox project

# Visual Studio Code
_Installation_

https://pimylifeup.com/raspberry-pi-visual-studio-code/

## Install this version
```sh
sudo apt-get install code-oss=1.29.0-1539702286
```

## Lock the version
```sh
sudo apt-mark hold code-oss
```

## Unlock the version
```sh
sudo apt-mark unhold code-oss
```

# Vim
```sh
sudo apt-get install vim
```

# Neovim
_Has display problems. Use Vim instead._
https://wilkins.tech/posts/neovim-raspberry-pi/

# Adafruit Touchsensor library
1. https://learn.adafruit.com/circuitpython-on-raspberrypi-linux
1. https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi/programming

# Adafruit circuitpython library
```sh
sudo pip3 install adafruit-blinka
```

# Install Adafruit libraries
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

# Requirements
- Python3


# Usage
## To run via command-line
```sh
python3 jukebox.py
```

## To run at startup.

### Open `rc.local`
```sh
sudo vim /etc/rc.local
```

### Add this line
```sh
  sudo python3 /path/to/violin-jukebox/jukebox.py &
```

# Raspberry PIN Setup
```
# All pings are on the right side of GPIO board
    0  0 <- Red (Power v5.5). However any power pin will work
    0  0
    0  0 <- Black (Ground). However any ground pin will work
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0
    0  0 <- Green (GPIO 40). Output must go in pin 40 or change in codebase.

  [ Ethernet ]  [ USB Bank ] [ USB Bank ]
```


# Directly using GPIO library
```py
import RPi.GPIO as GPIO

# GPIO Pin. Not Broadcom pin
GPIO_INPUT_PIN = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_INPUT_PIN, GPIO.IN)

value = GPIO.input(GPIO_INPUT_PIN)
if value == 1:
  # Do something
```