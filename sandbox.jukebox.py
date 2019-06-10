
# Violin jukebox
# Requires Python3
import board, os, random, subprocess, time
import RPI.GPIO as GPIO
from digitalio import DigitalInOut, Direction
from mocks import MockDigitalInOut, Human

# CONSTANTS
DOUBLE_TAP = 2
SONGS_DIR = '/home/pi/violin-jukebox/songs'
SAMPLE_RATE = 0.1
TIMEOUT = 2
OMXPLAYER_QUIT = 'q'.encode('utf-8')
PLAY_DURATION = 20

string_names = ['E', 'A', 'D', 'G']
strings = [0, 0, 0, 0]

playlist = os.listdir(SONGS_DIR)

# Uncomment for real production code
GPIO.setmode(GPIO.BOARD)


pad_pin = board.D23
pad = DigitalInOut(pad_pin)
pad.direction = Direction.INPUT

# For testing
# human = Human()
# pad = MockDigitalInOut()

# Print playlist
for index in range(len(playlist)):
  print("{song_num}: {song_name}".format(song_num=index+1, song_name=playlist[index]))

def play(song_id):
  # Construct command
  filename = "{songs_dir}/{song}".format(songs_dir=SONGS_DIR, song=playlist[song_id])
  command = "omxplayer --vol 500 -o local '{filename}'".format(filename=filename)
  print("Command: {command}".format(command=command))

  # execute the command
  p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
  time.sleep(PLAY_DURATION)
  p.communicate(input=OMXPLAYER_QUIT)


while True:
  # Randomly touch the pad
  # if random.random() < .2:
  #   print("Touching the pad")
  #   human.touch(pad)
  # else:
  #   print("Not touching the pad")
  #   human.stop_touching(pad)


  # CHOOSE A SONG
  # The playlist printed a 1-based index
  #   so we need to subtract 1 to get the 0-based index of the song
  # song_id = int(input("Which song? ")) - 1

  # SIMULATE DOUBLE TAPPING
  # if eval_time is not None and time.time() > eval_time:
  #   # user is done touching strings
  #   if any(string == DOUBLE_TAP for string in strings):
  #     # A string was double tapped
  #     song_id = random.choice(range(len(playlist)))
  #     play(song_id)

  # PLAY SONG
  # if pad.value:
    # song_id = random.choice(range(len(playlist)))
    # play(song_id)

  print(pad.value)

  time.sleep(SAMPLE_RATE)