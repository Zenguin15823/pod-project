import RPi.GPIO as GPIO
from gpiozero import MotionSensor
from pygame import mixer
import time

lights = [32, 22, 18, 16, 12]

def activate():
    """Turns on everything."""
    setup()
    cylon()

def cylon():
    """Blinks the lights in a Cylon scan pattern."""
    while True:
        for i in lights:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(i, GPIO.LOW)

def motion():
    pir = MotionSensor(4)

def off():
    """Turns off everything."""
    for i in lights:
        GPIO.output(i, GPIO.LOW)
    GPIO.cleanup()

def sound():
    mixer.init()
    mixer.music.load("static/sounds/hello.mp3")

def setup():
    """Sets up the GPIO pins for use."""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    for i in lights:
        GPIO.setup(i, GPIO.OUT)
    
def test():
    """Does a quick Cylon scan."""
    setup()

    for i in range(10):
        for i in lights:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(i, GPIO.LOW)
    
    off()
