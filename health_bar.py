import pygame
import constants


class HealthBar:
    def __init__(self):
        # self.full_health = 100
        # self.health = self.full_health
        # self.width_ = 100
        self.width_b = 200
        self.width_r = constants.HEALTH * 2
        self.height = 20

    # def update(self, damage):
    #     self.health -= damage

    def draw(self, screen):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1065, 680, self.width_b, self.height))
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(1065, 680, self.width_r, self.height))

