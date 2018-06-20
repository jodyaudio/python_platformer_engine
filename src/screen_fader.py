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
        self.rect = self.image.get_rect()
        self.color = color.BLACK

        self.states = {"FADE_IN": "FADE_IN",
                       "PAUSE": "PAUSE",
                       "FADE_OUT": "FADE_OUT"}
        self.starting_state = self.states["FADE_IN"]
        self.current_state = self.starting_state

        self.min_alpha = 0
        self.max_alpha = 255
        self.current_alpha = 255
        self.increment_alpha = 6
        self.counter_max = 3
        self.counter_alpha = self.counter_max

    def update(self):
        if self.current_state == "FADE_IN":
            self.fade_in()
        elif self.current_state == "PAUSE":
            self.pause()
        elif self.current_state == "FADE_OUT":
            self.fade_out()

    # STATE METHODS BELOW
    def fade_in(self):
        if self.counter_alpha > 0:
            self.counter_alpha -= 1
        else:
            if self.current_alpha <= self.min_alpha:
                self.current_alpha = self.min_alpha
                self.set_state("PAUSE")
            else:
                self.current_alpha -= self.increment_alpha
                self.image.set_alpha(self.current_alpha)
                self.counter_alpha = self.counter_max

    def pause(self):
        pass

    def fade_out(self):
        if self.counter_alpha > 0:
            self.counter_alpha -= 1
        else:
            if self.current_alpha >= self.max_alpha:
                self.current_alpha = self.max_alpha
                self.set_state("PAUSE")
            else:
                self.current_alpha += self.increment_alpha
                self.image.set_alpha(self.current_alpha)
                self.counter_alpha = self.counter_max

    # SETTERS
    def set_increment(self, incremental_value):
        self.increment_alpha = incremental_value

    def set_counter(self, counter_value):
        self.counter_max = counter_value

    def set_min_alpha(self, min_value):
        self.min_alpha = min_value

    def set_max_alpha(self, max_value):
        self.max_alpha = max_value

    def set_current_alpha(self, alpha_value):
        self.current_alpha = alpha_value

    def set_state(self, state):
        self.current_state = self.states[state]
