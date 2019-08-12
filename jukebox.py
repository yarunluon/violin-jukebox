"""
Violin jukebox

Plays a random song when the violin is touched. Songs do not repeat until they've been all
cycled through.

There are two modes that can be set.
    1. `MODE_SONG_STOPPABLE` which lets the user stop the current song to play another song.
    2. `MODE_SONG_UNSTOPPABLE` which plays the song the entire way through without stopping.

yarun.luon@gmail.com
"""

import board, time, os, random, subprocess
from digitalio import DigitalInOut, Direction
from threading import Timer

# Modes
MODE_SONG_STOPPABLE = "stoppable"
MODE_SONG_UNSTOPPABLE = "unstoppable"

# Constants
STARTUP_SOUND = "startup.wav"
ROOT_DIR = "/home/pi/repos/violin-jukebox/"
SONGS_DIR = ROOT_DIR + "songs"
OMXPLAYER_QUIT = "q".encode("utf-8")
MASTER_PLAYLIST = tuple(os.listdir(SONGS_DIR))

# States
STATE_PLAYING = "playing"
STATE_WAITING = "waiting"

# Volume controls
VOLUME_MAX = 200
VOLUME_NORMAL = 0

# Measured in seconds
SONG_BUFFER = 2
SONG_DURATION = 20
STARTUP_DURATION = 4
TOTAL_SONG_DURATION = SONG_DURATION + SONG_BUFFER
TOUCH_TIMEOUT = 2

# Uses Adafruit method. Alternative is directly use GPIO inputs
pad_pin = board.D21
pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT

# Setup global variables
playlist = []
state = STATE_WAITING

# Helper functions
def set_state(next_state):
  print("Setting state from '{state}' to '{next_state}'".format(state=state, next_state=next_state))
  global state
  state = next_state

def stop_playing(song_process, next_state):
  if song_process.poll() is None:
    print("stopping process now")
    song_process.communicate(input=OMXPLAYER_QUIT)
  else:
    print("process is already stopped. Doing nothing")

  set_state(next_state)

def print_playlist(playlist):
  print("[ PLAYLIST ] [ PLAYLIST ] [ PLAYLIST ] [ PLAYLIST ]")
  for index in range(len(playlist)):
    print("{song_num}: {song_name}".format(song_num=index+1, song_name=playlist[index]))
  print("♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪")

# Start program
mode = MODE_SONG_UNSTOPPABLE
print_playlist(MASTER_PLAYLIST)

# Play the startup sound indicating the program is ready
filename = ROOT_DIR + STARTUP_SOUND
startup_command = "omxplayer --vol {volume} -o local '{filename}'".format(volume=VOLUME_NORMAL, filename=filename)
print("Command: {command}".format(command=startup_command))
startup_process = subprocess.Popen(startup_command, shell=True, stdin=subprocess.PIPE)
time.sleep(STARTUP_DURATION)

# Main program
while True:
  if pad.value:
    if state == STATE_WAITING:
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
      stop_timer = Timer(TOTAL_SONG_DURATION, stop_playing, kwargs= { "song_process": song_process, "next_state": STATE_WAITING })
      stop_timer.start()

      set_state(STATE_PLAYING)
    elif state == STATE_PLAYING:
      if mode == MODE_SONG_STOPPABLE:
        stop_timer.cancel()
        stop_playing(song_process, STATE_WAITING)

    time.sleep(TOUCH_TIMEOUT)
