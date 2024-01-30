import pygame
import constants


class EndScreen:
    def __init__(self):
        self.image = pygame.image.load(constants.END_GAME)

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
