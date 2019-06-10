import time, os, random, subprocess
import RPi.GPIO as GPIO

SONGS_DIR = '/home/pi/violin-jukebox/songs'
GPIO_INPUT_PIN = 40
OMXPLAYER_QUIT = 'q'.encode('utf-8')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_INPUT_PIN, GPIO.IN)

playlist = os.listdir(SONGS_DIR)

# Print playlist
for index in range(len(playlist)):
  print("{song_num}: {song_name}".format(song_num=index+1, song_name=playlist[index]))


while True:
  # print(GPIO.input(GPIO_INPUT_PIN))

  value = GPIO.input(GPIO_INPUT_PIN)
  if value == 1:
    print("touched")
    time.sleep(0.1)
    song_id = random.choice(range(len(playlist)))
     # Construct command
    filename = "{songs_dir}/{song}".format(songs_dir=SONGS_DIR, song=playlist[song_id])
    command = "omxplayer --vol 300 -o local '{filename}'".format(filename=filename)
    print("Command: {command}".format(command=command))

    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
    time.sleep(20)
    p.communicate(input=OMXPLAYER_QUIT)
