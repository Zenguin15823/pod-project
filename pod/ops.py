import RPi.GPIO as GPIO
from gpiozero import MotionSensor
from pygame import mixer
import time
import random

lights = [32, 22, 18, 16, 12]

sounds = [
    "pod/static/sounds/card-payment.mp3",
    "pod/static/sounds/charging-machine.mp3",
    "pod/static/sounds/coffee-machine.mp3",
    "pod/static/sounds/drone-pulse.mp3",
    "pod/static/sounds/electric-door.mp3",
    "pod/static/sounds/heavy-machine-click.mp3",
    "pod/static/sounds/industrial-machine-cycle.mp3",
    "pod/static/sounds/large-steampunk-factory.mp3",
    "pod/static/sounds/machine-powering-down.mp3",
    "pod/static/sounds/mechanicalclamp.mp3",
    "pod/static/sounds/mecha-sound-effects.mp3",
    "pod/static/sounds/old-machine.mp3",
    "pod/static/sounds/slot-machine-payout.mp3",
    "pod/static/sounds/turbine.mp3",
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

    while True:
        pir.wait_for_motion()
        play_sound()
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
