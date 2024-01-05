import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

lights = [32, 22, 18, 16, 12];
for i in lights:
  GPIO.setup(i, GPIO.OUT)

for i in lights:
  GPIO.output(i, GPIO.LOW)
