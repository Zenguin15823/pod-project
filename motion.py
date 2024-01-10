import RPi.GPIO as GPIO
import time
from gpiozero import MotionSensor

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pir = MotionSensor(4)
lights = [32, 22, 18, 16, 12];
for i in lights:
  GPIO.setup(i, GPIO.OUT)

while True:
  pir.wait_for_motion()
  for i in lights:
    GPIO.output(i, GPIO.HIGH)
  pir.wait_for_no_motion()
  for i in lights:
    GPIO.output(i, GPIO.LOW)
