#### Modules ####
import random
import time
import ctypes
from os import system
min = 1
max = 6

#### Titles ####
ctypes.windll.kernel32.SetConsoleTitleW("Dice")
system("title " + "Dice")

#### State ####
roll_again = "yes"

#### Function ####
while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dice...")
    time.sleep(1)
    print ("The value is....")
    print (random.randint(min, max))
    roll_again = input("Roll the dice again?")