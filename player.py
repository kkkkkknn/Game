import pygame
import constants
from game_map import GameMap

mapa = GameMap(constants.MAP)


class Player(pygame.sprite.Sprite):
    def __init__(self, game_map):
        super().__init__()
        self.image = pygame.image.load(constants.PLAYER_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.game_map = game_map

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, direction):
        if direction == "up":
            self.rect.y -= constants.CELL_SIZE
        elif direction == "down":
            self.rect.y += constants.CELL_SIZE
        elif direction == "left":
            self.rect.x -= constants.CELL_SIZE
        elif direction == "right":
            self.rect.x += constants.CELL_SIZE