import pygame
import constants as c
import ultracolors as color
import bounding_box


class Player(pygame.sprite.Sprite):
    """The player object will receive user input and be controllable.
    The player can run, jump and attack."""
    def __init__(self):
        super(Player, self).__init__()

        # Setup image properties
        self.width = c.LARGE_TILE_WIDTH
        self.height = c.LARGE_TILE_HEIGHT * 2
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.image.fill(color.BLUE)
        self.rect = self.image.get_rect()

        # Setup bounding box (hurt box/collision box)
        self.bbox_size = (self.size)
        self.bbox = bounding_box.BoundingBox(self.bbox_size)

        # Setup velocity properties
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 20
        self.jump_vel = -50

        # Setup states
        self.is_controllable = True
        self.is_alive = True
        self.in_air = False
        self.is_invincible = False
        self.states = {"IDLE": "IDLE",
                       "RUN": "RUN",
                       "JUMPING": "JUMPING",
                       "FALLING": "FALLING"}
        self.starting_state = self.states["IDLE"]
        self.current_state = self.starting_state

    def update(self):
        if self.current_state == "IDLE":
            self.idle_state()
        elif self.current_state == "RUN":
            self.run_state()
        elif self.current_state == "JUMPING":
            self.jumping_state()
        elif self.current_state == "FALLING":
            self.falling_state()

    # STATE METHODS BELOW
    def idle_state(self):
        pass

    def run_state(self):
        pass

    def jumping_state(self):
        pass

    def falling_state(self):
        pass