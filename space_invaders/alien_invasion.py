import sys
import pygame

from space_invaders.sprites import Ship
from space_invaders.settings import ScreenSettings


def run_game():
    pygame.init()
    screen_settings = ScreenSettings()
    screen = pygame.display.set_mode((screen_settings.width, screen_settings.height))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #screen.fill(screen_settings.bg_color)
        ship.blitme()
        pygame.display.flip()


def main():
    run_game()


if __name__=='__main__':
    main()
