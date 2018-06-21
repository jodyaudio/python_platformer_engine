import pygame
import constants as c
import state
import screen_fader
import ultracolors as color


class SplashScreen(state.State):
    def __init__(self):
        super(SplashScreen, self).__init__()

        # SCREEN FADE SETUP
        self.fader = screen_fader.ScreenFader()

        # BACKGROUND SETUP
        self.bg = None

        # LOGO IMAGE SETUP
        self.logo_width = 190
        self.logo_height = 50
        self.logo_size = (self.logo_width, self.logo_height)
        self.logo_image = pygame.Surface(self.logo_size)
        self.logo_color = color.ORANGE
        self.logo_image.fill(self.logo_color)
        self.logo_x_pos = c.DISPLAY_WIDTH_CENTER - self.logo_width // 2
        self.logo_y_pos = c.DISPLAY_HEIGHT_CENTER - self.logo_height // 2
        self.logo_pos = (self.logo_x_pos, self.logo_y_pos)

        # STATE SETUP
        self.states = {"FADE_IN": "FADE_IN",
                       "PAUSE": "PAUSE",
                       "FADE_OUT": "FADE_OUT"}
        self.starting_state = self.states["FADE_IN"]
        self.current_state = self.starting_state

        # TIMERS SETUP
        self.fade_pause_counter = 20

        # SPRITE GROUP SETUP
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.fader)

    def update(self, dt):
        # UPDATE SPRITE GROUP
        self.sprite_group.update()

        # RUN STATE MACHINE
        if self.current_state == "FADE_IN":
            self.fade_in()
        if self.current_state == "PAUSE":
            self.pause()
        if self.current_state == "FADE_OUT":
            self.fade_out()

    # STATE METHODS BELOW
    def fade_in(self):
        if self.fader.current_alpha == self.fader.min_alpha:
            self.set_state("PAUSE")

    def pause(self):
        if self.fade_pause_counter > 0:
            self.fade_pause_counter -= 1
        else:
            self.fader.set_state("FADE_OUT")
            self.set_state("FADE_OUT")

    def fade_out(self):
        if self.fader.current_alpha == self.fader.max_alpha:
            pass

    def render(self, display):
        display.fill(color.BLACK)
        display.blit(self.logo_image, self.logo_pos)
        self.sprite_group.draw(display)
        pygame.display.update()

    # SETTERS
    def set_state(self, new_state):
        self.current_state = self.states[new_state]
