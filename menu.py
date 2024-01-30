import pygame
import constants


class Menu:
    def __init__(self):
        self.background_image = pygame.image.load(constants.FON_IMAGE)

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 150

        for line in constants.RULES:
            string_rendered = font.render(line, 1, pygame.Color(constants.TEXT_COLOR))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 400
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
