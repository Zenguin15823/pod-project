import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

lights = [32, 22, 18, 16, 12];
for i in lights:
  GPIO.setup(i, GPIO.OUT)

while True:
  for i in lights:
    GPIO.output(i, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(i, GPIO.LOW)
  for i in reversed(lights[1:4]):
    GPIO.output(i, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(i, GPIO.LOW)
