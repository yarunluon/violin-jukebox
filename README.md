# Violin Jukebox project
The violin jukebox is a capacitive enabled instrument. When the electrical field around the violin is disturbed, it sends a signal to the microcontroller to play a song. The microcontroller outputs the song into a vibrating speaker attached to the back of the violin. The vibrarion of the speakers is amplified by the violin's natural acoustic body.The jukebox cycles through every song in random order before repeating songs.


# Requirements
1. Python3
1. Raspberry Pi
1. Violin
1. Capacitive touch sensor
1. Vibrating speaker
1. Violan stand

# Installation
## Visual Studio Code
Need to install a Raspberry Pi build of vs-code
https://pimylifeup.com/raspberry-pi-visual-studio-code/

### Install this version
Need to install the gpg keys before installing this specific version. Might be easier to first install the most recent version and then downgrade.
```sh
sudo apt-get install code-oss=1.29.0-1539702286
```

### Lock the version
```sh
sudo apt-mark hold code-oss
```

### Unlock the version
```sh
sudo apt-mark unhold code-oss
```

## Vim
```sh
sudo apt-get install vim
```

## Neovim
_Has display problems. Use Vim instead._
https://wilkins.tech/posts/neovim-raspberry-pi/

## Adafruit Touchsensor library
1. https://learn.adafruit.com/circuitpython-on-raspberrypi-linux
1. https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi/programming

## Adafruit circuitpython library
```sh
sudo pip3 install adafruit-blinka
```

## Install Adafruit libraries
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi


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

# Setup using either GPIO or Adafruit library

## Directly using GPIO library
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

## Directly using Adafruit library
```py
import board
from digitalio import DigitalInOut, Direction

# Uses DCOM pin. Not the GPIO pin
pad_pin = board.D21
pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT

while True:
  if pad.value:
    # Do something
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

