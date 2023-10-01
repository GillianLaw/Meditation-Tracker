import os
import time
import datetime
import sys


"""This will be a non-GUI-based meditation timer, allowing me to choose the length of
 the meditation and add interval sounds"""

def countdown(minutes) -> int:


    total_seconds = minutes * 60

    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:

        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)

        # Prints the time left on the timer
        print(timer, end="\r")

        # Delays the program one second
        time.sleep(1)

        # Reduces total time by one second
        total_seconds -= 1

        if total_seconds == ((minutes * 60)/3) * 2:
            print("One third done")
            os.system('afplay /System/Library/Sounds/Ping.aiff')
        if total_seconds == (minutes * 60)/3:
            print("One third to go")
            os.system('afplay /System/Library/Sounds/Ping.aiff')



    print("Well done, I hope you feel calmer")
    os.system('afplay /System/Library/Sounds/Basso.aiff')
    os.system('afplay /System/Library/Sounds/Bottle.aiff')
    os.system('afplay /System/Library/Sounds/Ping.aiff')



minutes = input("How long do you plan to meditate today? ")
countdown(int(minutes))


