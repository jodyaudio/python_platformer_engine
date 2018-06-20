import pygame
import constants as c
import state
import screen_fader


class SplashScreen(state.State):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.fader = screen_fader.ScreenFader()

        # STATE SETUP
        self.states = {"FADE_IN": "FADE_IN",
                       "PAUSE": "PAUSE",
                       "FADE_OUT": "FADE_OUT"}
        self.starting_state = self.states["FADE_IN"]
        self.current_state = self.starting_state

    def update(self, dt):
        if self.current_state == "FADE_IN":
            self.fade_in()
        if self.current_state == "PAUSE":
            self.pause()
        if self.current_state == "FADE_OUT":
            self.fade_out()

    # STATE METHODS BELOW
    def fade_in(self):
        pass

    def pause(self):
        pass

    def fade_out(self):
        pass
