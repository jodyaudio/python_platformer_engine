# The setup module does the games initial setup right when the main file is executed.
# Sets up display, clock, and sets up game states/scenes into a dictionary

import pygame
import constants as c
import splash_screen


# Initialize pygame and all of its modules.
pygame.init()


# Method to create the games display with the given resolution.
def display_setup(resolution):
    return pygame.display.set_mode(resolution)


# Method that creates a pygame clock object to manage the games FPS.
def clock_setup():
    return pygame.time.Clock()


# Method that creates a dictionary of games states. Key = string name : Value = State object
def state_dict_setup():
    state_dict = {c.SPLASH_SCREEN: splash_screen.SplashScreen()}
    return state_dict
