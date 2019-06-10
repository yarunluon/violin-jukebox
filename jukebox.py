import time, os, random, subprocess

import board
from digitalio import DigitalInOut, Direction

# Constants
SONGS_DIR = '/home/pi/repos/violin-jukebox/songs'

OMXPLAYER_QUIT = 'q'.encode('utf-8')
SONG_DURATION = 22
MODE_WAITING = "waiting"
MODE_PLAYING = "playing"

pad_pin = board.D21
pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT

playlist = os.listdir(SONGS_DIR)

# Print playlist
for index in range(len(playlist)):
  print("{song_num}: {song_name}".format(song_num=index+1, song_name=playlist[index]))

mode = MODE_WAITING

while True:
  if pad.value:
    print(pad.value)
    time.sleep(0.1)
    # if mode == MODE_WAITING:
    song_id = random.choice(range(len(playlist)))
    # Construct command
    filename = "{songs_dir}/{song}".format(songs_dir=SONGS_DIR, song=playlist[song_id])
    command = "omxplayer --vol 200 -o local '{filename}'".format(filename=filename)
    print("Command: {command}".format(command=command))

    mode = MODE_PLAYING
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
    time.sleep(SONG_DURATION)
    print("end of song has arrived")
    p.communicate(input=OMXPLAYER_QUIT)
    # time.sleep(5)
      # mode = MODE_WAITING
    # elif mode == MODE_PLAYING:
    #   print("stopping song per request")
    #   p.communicate(input=OMXPLAYER_QUIT)
    #   time.sleep(1)
    #   mode == MODE_WAITING
  else:
    time.sleep(0.1)
