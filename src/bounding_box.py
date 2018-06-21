import pygame
import constants as c
import ultracolors as color


class BoundingBox(pygame.sprite.Sprite):
    def __init__(self, size):
        super(BoundingBox, self).__init__()
        self.size = size
        self.image = pygame.Surface(self.size)
        self.color = color.AQUA
        self.rect = self.image.get_rect()

    def update(self):
        pass