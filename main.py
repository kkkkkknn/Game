import pygame

import constants
from end_screen import EndScreen
from game_map import GameMap
from health_bar import HealthBar
from menu import Menu
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Минные поля")

    clock = pygame.time.Clock()
    is_running = True

    menu = Menu()
    game_map = GameMap(constants.MAP)
    player = Player(game_map)
    end_screen = EndScreen()
    health_bar = HealthBar()
    end_screen = EndScreen()

    current_screen = "menu"

    while is_running:
        x_now = 0
        y_now = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if current_screen == "menu":
                    if event.key == pygame.K_RETURN or event.button == 3:
                        current_screen = "game"
                elif current_screen == "game":
                    if event.key == pygame.K_ESCAPE:
                        current_screen = "menu"

                    elif event.key == pygame.K_w:
                        player.move("up")
                        y_now -= 1

                    elif event.key == pygame.K_s:
                        player.move("down")
                        y_now += 1

                    elif event.key == pygame.K_a:
                        player.move("left")
                        x_now -= 1

                    elif event.key == pygame.K_d:
                        player.move("right")
                        x_now += 1

        screen.fill(constants.BACKGROUND_COLOR)

        if current_screen == "menu":
            menu.draw(screen)
        elif current_screen == "game":
            game_map.draw(screen)
            health_bar.draw(screen)
            player.draw(screen)
        elif current_screen == "end_game":
            end_screen.draw(screen)

        pygame.display.flip()
        clock.tick(constants.FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
