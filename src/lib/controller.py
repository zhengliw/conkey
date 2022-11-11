# controller.py - Provides stuff to get input from 
# gamepads, using inputs
# Mainly messing around right now.
# Licensed under the MIT license. More information
# in the main LICENSE file at the root of this 
# repository.

import os
from time import sleep
import inputs

while True:
    events = inputs.get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)
    
    print("\n======\n")

    sleep(0.5)

    os.system("cls")
