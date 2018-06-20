# CREATED BY JODY BAILEY 5/20/2018

import game_setup
import controller
import constants as c
import pygame


# Create the games display
display = game_setup.display_setup(c.DISPLAY_SIZE)

# Create the games clock
clock = game_setup.clock_setup()

# Create a dictionary of the games states / scenes
state_dict = game_setup.state_dict_setup()

# Create a controller object that runs the games main loop
controller = controller.Controller(display, clock, state_dict)

# This is the controller objects run method that is essentially the main game loop.
controller.run()

# If the main loop ever breaks, this de-initializes pygame and quits the program.
pygame.quit()
quit()
