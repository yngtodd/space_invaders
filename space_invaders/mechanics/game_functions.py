import sys
import pygame

from space_invaders.sprites import Weapon


def check_events(screen_settings, weapon_settings, screen, ship, ammo):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen_settings, weapon_settings, screen, ship, ammo)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, screen_settings, weapon_settings, screen, ship, ammo):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_weapon(weapon_settings, screen, ship, ammo)
    if event.key == pygame.K_BACKSPACE:
        sys.exit()


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_ammo(ammo):
    """Update position of projectiles."""
    ammo.update()
    # Clear bullets that go off screen.
    for bullet in ammo.copy():
        if bullet.rect.bottom <= 0:
            ammo.remove(bullet)


def fire_weapon(weapon_settings, screen, ship, ammo):
    """Fire weapon if limit not yet reached"""
    if len(ammo) < weapon_settings.ammo_allowed:
        new_ammo = Weapon(weapon_settings, screen, ship)
        ammo.add(new_ammo)


def update_screen(screen_settings, screen, ship, ammo, alien):
    """Update images on the screen and flip to the new screen."""
    screen.fill(screen_settings.bg_color)
    for projectile in ammo.sprites():
        projectile.draw_weapon()
    ship.blitme()
    alien.blitme()
    pygame.display.flip()
