# controller.py - Provides stuff to get input from 
# gamepads, using pygame
# Licensed under the MIT license. More information
# in the main LICENSE file at the root of this 
# repository.

import pygame

pygame.joystick.init()

all_devs = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

print(all_devs)

if not all_devs:
    print("No devs found!")
else:
    for dev in all_devs:
        print(dev.get_power_level())