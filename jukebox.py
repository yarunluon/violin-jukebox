"""
Violin jukebox

Plays a random song when the violin is touched. Songs do not repeat until they've been all
cycled through. Touching the violin again stops the song.
yarun.luon@gmail.com
"""

import board, time, os, random, subprocess
from digitalio import DigitalInOut, Direction
from threading import Timer

# Constants
SONGS_DIR = "/home/pi/repos/violin-jukebox/songs"
OMXPLAYER_QUIT = "q".encode("utf-8")
MASTER_PLAYLIST = tuple(os.listdir(SONGS_DIR))

# Modes
MODE_PLAYING = "playing"
MODE_WAITING = "waiting"

# Volume controls
VOLUME_MAX = 200
VOLUME_NORMAL = 0

# Measured in seconds
SONG_BUFFER = 2
SONG_DURATION = 20
TOTAL_SONG_DURATION = SONG_DURATION + SONG_BUFFER
TOUCH_TIMEOUT = 2

# Uses Adafruit method. Alternative is directly use GPIO inputs
pad_pin = board.D21
pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT

# Setup global variables
playlist = []
mode = MODE_WAITING

def set_mode(next_mode):
  print("Setting mode from '{mode}' to '{next_mode}'".format(mode=mode, next_mode=next_mode))
  global mode
  mode = next_mode

def stop_playing(song_process, next_mode):
  if song_process.poll() is None:
    print("stopping process now")
    song_process.communicate(input=OMXPLAYER_QUIT)
  else:
    print("process is already stopped. Doing nothing")

  set_mode(next_mode)

def print_playlist(playlist):
  print("[ PLAYLIST ] [ PLAYLIST ] [ PLAYLIST ] [ PLAYLIST ]")
  for index in range(len(playlist)):
    print("{song_num}: {song_name}".format(song_num=index+1, song_name=playlist[index]))
  print("♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪")

print_playlist(MASTER_PLAYLIST)

while True:
  if pad.value:
    if mode == MODE_WAITING:
      if not playlist:
        # Playlist is empty. Repopulate and shuffle it from the master playlist
        playlist = list(MASTER_PLAYLIST[:])
        random.shuffle(playlist)

      # Take the next song from the playlist. Sample without replacement.
      song_name = playlist.pop()
      print("{remaining} songs left".format(remaining=len(playlist)))

      # Create command to execute
      filename = "{songs_dir}/{song}".format(songs_dir=SONGS_DIR, song=song_name)
      command = "omxplayer --vol {volume} -o local '{filename}'".format(volume=VOLUME_NORMAL, filename=filename)
      print("Command: {command}".format(command=command))

      # Create subprocess to play song
      song_process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)

      # Start timer to kill the song
      stop_timer = Timer(TOTAL_SONG_DURATION, stop_playing, kwargs= { "song_process": song_process, "next_mode": MODE_WAITING })
      stop_timer.start()

      set_mode(MODE_PLAYING)
    elif mode == MODE_PLAYING:
      stop_timer.cancel()
      stop_playing(song_process, MODE_WAITING)

    time.sleep(TOUCH_TIMEOUT)
