# controller.py - Provides stuff to get input from 
# gamepads, using inputs
# Mainly messing around right now.
# Licensed under the MIT license. More information
# in the main LICENSE file at the root of this 
# repository.

import inputs

gamepads = inputs.devices.gamepads

if gamepads:
    for gamepad in gamepads:
        print("Gamepad found:", gamepad)

    usedGamepadIndex = 0

    if len(gamepads) > 1:
        
        # If more than one gamepad connected, let user
        # decide with number input

        print("Which gamepad would you like to use?")

        for index, gamepad in enumerate(gamepads):
            print("{}: {}".format(index, gamepad))
        
        while True:
            try:
                usedGamepadIndex = int(input(">>> "))
                
                # Make sure the gamepad index is valid
                # by trying to access the indexed gamepad
                gamepads[usedGamepadIndex]

            except (ValueError, IndexError):
                continue
            else:
                break

else:
    print("No gamepads detected.")
    exit(1)

diri = [item for item in dir(gamepads[usedGamepadIndex]) if item[0] != '_']

print(diri)