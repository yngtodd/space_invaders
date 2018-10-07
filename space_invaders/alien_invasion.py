import sys
import pygame
from pygame.sprite import Group

from space_invaders.sprites import Ship, Alien
from space_invaders.settings import ScreenSettings
from space_invaders.settings import ShipSettings
from space_invaders.settings import WeaponSettings
from space_invaders.settings import AlienSettings
import space_invaders.mechanics.game_functions as gf


def run_game():
    pygame.init()

    ship_settings = ShipSettings()
    weapon_settings = WeaponSettings()
    alien_settings = AlienSettings()
    screen_settings = ScreenSettings()

    screen = pygame.display.set_mode((screen_settings.width, screen_settings.height))
    pygame.display.set_caption("Space Invaders")

    ship = Ship(ship_settings, screen)
    ammo = Group()
    aliens = Group()
    gf.create_fleet(alien_settings, screen_settings, screen, aliens)

    while True:
        gf.check_events(screen_settings, weapon_settings, screen, ship, ammo)
        ship.update()
        gf.update_ammo(ammo)
        gf.update_screen(screen_settings, screen, ship, ammo, aliens)


def main():
    run_game()


if __name__=='__main__':
    main()
