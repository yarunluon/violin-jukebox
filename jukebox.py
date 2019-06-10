"""
Violin jukebox

Plays a random song when the violin is touched. Songs do not repeat until they've been all
cycled through.
yarun.luon@gmail.com
"""

import board, time, os, random, subprocess
from digitalio import DigitalInOut, Direction

# Constants
SONGS_DIR = '/home/pi/repos/violin-jukebox/songs'
OMXPLAYER_QUIT = 'q'.encode('utf-8')
SONG_DURATION = 22
PLAYLIST = tuple(os.listdir(SONGS_DIR))
VOLUME_MAX = 200
VOLUME_NORMAL = 0

# Uses Adafruit method. Alternative is directly use GPIO inputs
pad_pin = board.D21
pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT
playlist = []

def print_playlist(playlist):
  print("[ PLAYLIST ] [ PLAYLIST ] [ PLAYLIST ] [ PLAYLIST ]")
  for index in range(len(playlist)):
    print("{song_num}: {song_name}".format(song_num=index+1, song_name=playlist[index]))
  print("♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪")

def play(song_name):
  filename = "{songs_dir}/{song}".format(songs_dir=SONGS_DIR, song=song_name)
  command = "omxplayer --vol {volume} -o local '{filename}'".format(volume=VOLUME_NORMAL, filename=filename)
  print("Command: {command}".format(command=command))
  p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
  time.sleep(SONG_DURATION)
  p.communicate(input=OMXPLAYER_QUIT)

print_playlist(PLAYLIST)

while True:
  if pad.value:
    print("pad touched. playing song")

    if not playlist:
      playlist = list(PLAYLIST[:])
      random.shuffle(playlist)

    song_name = playlist.pop()
    play(song_name)

  # Not sure why I need to do this. Following sample code
  time.sleep(0.1)
