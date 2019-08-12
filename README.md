# Violin Jukebox project
The violin jukebox is a capacitive enabled instrument. When the electrical field around the violin is disturbed, it sends a signal to the microcontroller to play a song. The microcontroller outputs the song into a vibrating speaker attached to the back of the violin. The vibrarion of the speakers is amplified by the violin's natural acoustic body.The jukebox cycles through every song in random order before repeating songs.


# Requirements
1. Python3
1. Raspberry Pi 3
1. Violin
1. [Capacitive touch sensor](https://www.adafruit.com/product/1374)
1. Vibrating speaker
1. Violan stand

# Driver installation
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

## To run at startup
1. Open `rc.local`
    ```sh
    sudo vim /etc/rc.local
    ```

1. Add this line to the end of the file
    ```sh
    sudo python3 /path/to/violin-jukebox/jukebox.py &
    ```

# Implement using either GPIO or Adafruit library

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
# All pins are on the right side of GPIO board
# Any power or ground pins will work
                                    0  0 <- Red (Power v5.5)
                                    0  0
                                    0  0 <- Black (Ground)
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
                                    0  0 <- Green (GPIO 40). Update the code if not using pin 40.

  [ Ethernet ]  [ USB Bank ] [ USB Bank ]
```
# Physical setup
## Input
1. Attach an antenna to the touch sensor by soldering a wire to the pinhole.
1. Attach the wire antenna to the string of the violin under the bridge.
1. Attach the pins of the touch sensor to the raspberry according to the pin diagram

## Output
1. Plug an 1/8" audio cord from the raspberry pi to the aux in of the vibration speaker
1. Attach the speaker to the flat portion on the back of the violin

# Tools
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