## This is MCOM Test

import os;
import time;
import math;
import winsound

Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 150 # Set Duration To 1000 ms == 1 second

# stats
armed = False;

def disarm():
    for i in range(8):
        winsound.Beep(Freq, Dur);
        time.sleep(2/8);

    
    print("MCOM DISAMRED");

if (armed == True) and (player == "DIS"):
    disarm();
elif (armed == False
