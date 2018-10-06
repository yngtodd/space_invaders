import sys
import pygame
from pygame.sprite import Group

from space_invaders.sprites import Ship
from space_invaders.settings import ScreenSettings, ShipSettings, WeaponSettings
import space_invaders.mechanics.game_functions as gf


def run_game():
    pygame.init()
    ship_settings = ShipSettings()
    weapon_settings = WeaponSettings()
    screen_settings = ScreenSettings()
    screen = pygame.display.set_mode((screen_settings.width, screen_settings.height))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(ship_settings, screen)
    ammo = Group()

    while True:
        gf.check_events(screen_settings, weapon_settings, screen, ship, ammo)
        ship.update()
        ammo.update()
        gf.update_screen(screen_settings, screen, ship, ammo)


def main():
    run_game()


if __name__=='__main__':
    main()
