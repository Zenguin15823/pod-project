# from playsound import playsound
# playsound('/home/hello.mp3')

import time
from pygame import mixer

mixer.init()
mixer.music.load("/home/hello.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)