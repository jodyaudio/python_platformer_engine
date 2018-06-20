import pygame
import state
import constants as c
import player


class Level(state.State):
    def __init__(self):
        self.player = player.Player()

    def update(self, dt):
        pass