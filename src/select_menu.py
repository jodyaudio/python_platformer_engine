import pygame
import constants as c
import ultracolors as color


class SelectMenu(pygame.sprite.Sprite):
    """Simple menu class for generating selection menus that have
    multiple options that can be highlighted and selected."""
    def __init__(self, options_list):
        super(SelectMenu, self).__init__()
        self.options_list = options_list
        self.min_selection = 0
        self.max_selection = len(options_list - 1)
        self.current_index = 0
        self.default_color = color.GREY
        self.highlight_color = color.PURPLE_2
        self.font_size = 12
        self.font = pygame.font.Font(None, self.font_size)

