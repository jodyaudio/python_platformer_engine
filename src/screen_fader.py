import pygame
import ultracolors as color
import constants as c


class ScreenFader(pygame.sprite.Sprite):
    def __init__(self):
        super(ScreenFader, self).__init__()
        self.width = c.DISPLAY_WIDTH
        self.height = c.DISPLAY_HEIGHT
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = color.BLACK
        self.states = {"FADE_IN": "FADE_IN",
                       "PAUSE": "PAUSE",
                       "FADE_OUT": "FADE_OUT"}
        self.starting_state = self.states["FADE_IN"]
        self.current_state = self.starting_state

        self.mix_alpha = 0
        self.max_alpha = 255
        self.current_alpha = 255
        self.increment_alpha = 3
        self.counter_alpha = 3

    def update(self):
        if self.current_state == "FADE_IN":
            self.fade_in()
        elif self.current_state == "PAUSE":
            self.pause()
        elif self.current_state == "FADE_OUT":
            self.fade_out()

    # STATE METHODS BELOW
    def fade_in(self):
        pass

    def pause(self):
        pass

    def fade_out(self):
        pass
