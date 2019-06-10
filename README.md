# violin-jukebox
Violin Jukebox project

# Visual Studio Code
_Installation_

https://pimylifeup.com/raspberry-pi-visual-studio-code/

## Install this version
```
sudo apt-get install code-oss=1.29.0-1539702286
```

## Lock the version
```
sudo apt-mark hold code-oss
```

## Unlock the version
```
sudo apt-mark unhold code-oss
```

# Vim
sudo apt-get install vim

# Neovim
_Has display problems. Use Vim instead._
https://wilkins.tech/posts/neovim-raspberry-pi/

# Adafruit Touchsensor library
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux
https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi/programming

# Adafruit circuitpython library
sudo pip3 install adafruit-blinka

# Install Adafruit libraries
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

# Requirements
- Python3


# Usage
## To run via command-line
```py
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

# Raspbeery PIN Setup
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


