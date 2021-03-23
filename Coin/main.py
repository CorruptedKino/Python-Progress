#### Modules ####
import ctypes
from os import system
import random
import time


#### Title ####
ctypes.windll.kernel32.SetConsoleTitleW("Coin Flip")
system("title " + "Coin Flip")

#### Variables ####
face = ['Heads', 'Tails']
flip_again = "yes"

#### Function ####
while flip_again == "yes" or flip_again == "y":
    print ("Flipping the coin...")
    time.sleep(1)
    print (random.choice(face))
    flip_again = input("Flip the coin again?")