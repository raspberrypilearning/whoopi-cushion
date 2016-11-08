import os
import random
from time import sleep
from gpiozero import Button

button = Button(2)

trumps = [
    'ben-fart.wav',
    'ca-fart.wav',
    'marc-fart.wav']

while True:
    button.wait_for_press()
    parp = random.choice(trumps)
    os.system("aplay {0}".format(parp))
    sleep(2)
