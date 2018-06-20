# The setup module does the games initial setup right when the main file is executed.
# Sets up display, clock, and sets up game states/scenes into a dictionary.

import pygame
import constants as c
import splash_screen


# Initialize pygame and all of its modules. !!!mixer module must be set up specifically like this or it will have
# a really long delay (must be initialized before pygame itself). I could not find out why this is, but it is the only
# way it works for some reason.
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.mixer.init()
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
