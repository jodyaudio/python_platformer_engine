import pygame


class EventHandler:
    def __init__(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()