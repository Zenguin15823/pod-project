import RPi.GPIO as GPIO
from gpiozero import MotionSensor
from pygame import mixer
import time
import random

lights = [32, 22, 18, 16, 12]

sounds = [
    "pod/static/sounds/charging-machine.mp3",
    "pod/static/sounds/heavy-machine-click.mp3",
    "pod/static/sounds/hello.mp3",
    "pod/static/sounds/mechanicalclamp.mp3",
    "pod/static/sounds/mecha-sound-effects.mp3",
    "pod/static/sounds/never-president.mp3",
    "pod/static/sounds/not-touching.mp3",
    "pod/static/sounds/slot-machine-payout.mp3",
    "pod/static/sounds/sorry.mp3",
    "pod/static/sounds/startup-sequence.mp3"
    ]

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
    setup()
    play_sound()

    while True:
        pir.wait_for_motion()
        for i in range(10):
            for i in lights:
                GPIO.output(i, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(i, GPIO.LOW)

def off():
    """Turns off everything."""
    for i in lights:
        GPIO.output(i, GPIO.LOW)
    GPIO.cleanup()

def play_sound():
    mixer.init()
    mixer.music.load(random.choice(sounds))
    mixer.music.play()
    while mixer.music.get_busy() == True:
        pass

def setup():
    """Sets up the GPIO pins for use."""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    for i in lights:
        GPIO.setup(i, GPIO.OUT)
    
def test():
    """Does a quick Cylon scan."""
    setup()

    for _ in range(10):
        for i in lights:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(i, GPIO.LOW)
    
    off()
