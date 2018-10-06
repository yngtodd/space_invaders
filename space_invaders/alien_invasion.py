import sys
import pygame

from space_invaders.sprites import Ship
from space_invaders.settings import ScreenSettings, ShipSettings
import space_invaders.mechanics.game_functions as gf


def run_game():
    pygame.init()
    ship_settings = ShipSettings()
    screen_settings = ScreenSettings()
    screen = pygame.display.set_mode((screen_settings.width, screen_settings.height))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(ship_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen_settings, screen, ship)


def main():
    run_game()


if __name__=='__main__':
    main()
