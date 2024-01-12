import RPi.GPIO as GPIO
import time
from gpiozero import MotionSensor
from pygame import mixer

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pir = MotionSensor(4)
lights = [32, 22, 18, 16, 12];
for i in lights:
  GPIO.setup(i, GPIO.OUT)
mixer.init()
mixer.music.load("/home/zac/src/pod-project/sounds/hello.mp3")

while True:
  pir.wait_for_motion()
  mixer.music.play()
  for i in range(10):
    for i in lights:
      GPIO.output(i, GPIO.HIGH)
      time.sleep(0.2)
      GPIO.output(i, GPIO.LOW)