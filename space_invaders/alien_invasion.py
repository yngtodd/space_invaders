import sys
import pygame
from pygame.sprite import Group

from space_invaders.menu import Button
from space_invaders.stats import GameStats
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
    play_button = Button(screen_settings, screen, "Play")
    stats = GameStats(ship_settings)

    ammo = Group()
    aliens = Group()
    ship = Ship(ship_settings, screen)
    gf.create_fleet(alien_settings, screen_settings, screen, ship, aliens)

    while True:
        gf.check_events(screen_settings, alien_settings, screen, stats, weapon_settings, ship, aliens, ammo, play_button)
        if stats.game_active:
            ship.update()
            gf.update_ammo(alien_settings, screen_settings, screen, ship, aliens, ammo)
            gf.update_aliens(alien_settings, ship_settings, screen_settings, stats, screen, ship, aliens, ammo)
        gf.update_screen(screen_settings, screen, stats, ship, ammo, aliens, play_button)


def main():
    run_game()


if __name__=='__main__':
    main()
