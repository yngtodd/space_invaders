import sys
import pygame

from space_invaders.sprites import Weapon, Alien


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


def update_ammo(alien_settings, screen_settings, screen, ship, aliens, ammo):
    """Update position of projectiles."""
    ammo.update()
    collisions = pygame.sprite.groupcollide(ammo, aliens, True, True)

    if len(aliens) == 0:
        ammo.empty()
        create_fleet(alien_settings, screen_settings, screen, ship, aliens)

    # Clear bullets that go off screen.
    for bullet in ammo.copy():
        if bullet.rect.bottom <= 0:
            ammo.remove(bullet)


def fire_weapon(weapon_settings, screen, ship, ammo):
    """Fire weapon if limit not yet reached"""
    if len(ammo) < weapon_settings.ammo_allowed:
        new_ammo = Weapon(weapon_settings, screen, ship)
        ammo.add(new_ammo)


def create_alien(alien_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place in in a row."""
    alien = Alien(alien_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(alien_settings, screen_settings, alien_width):
    """Determine the number of aliens that will fit in a row."""
    available_space_x = screen_settings.width - 2 * alien_width
    num_aliens_x = int(available_space_x / (2 * alien_width))
    return num_aliens_x


def get_num_alien_rows(screen_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (screen_settings.height - (4 * alien_height) - ship_height)
    num_rows = int(available_space_y / (2 * alien_height))
    return num_rows


def create_fleet(alien_settings, screen_settings, screen, ship, aliens):
    """Create a fleet of aliens."""
    alien = Alien(alien_settings, screen)
    num_aliens_x = get_number_aliens_x(alien_settings, screen_settings, alien.rect.width)
    num_alien_rows = get_num_alien_rows(screen_settings, ship.rect.height, alien.rect.height)

    for row_number in range(num_alien_rows):
        for alien_number in range(num_aliens_x):
            create_alien(alien_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(alien_settings, aliens):
    """"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(alien_settings, aliens)
            break


def change_fleet_direction(alien_settings, aliens):
    """Drop the entire fleet and change fleet direction."""
    for alien in aliens.sprites():
        alien.rect.y += alien_settings.fleet_drop_speed
    alien_settings.fleet_direction *= -1


def update_aliens(alien_settings, aliens):
    """Update the positions of alien fleet."""
    check_fleet_edges(alien_settings, aliens)
    aliens.update()


def update_screen(screen_settings, screen, ship, ammo, aliens):
    """Update images on the screen and flip to the new screen."""
    screen.fill(screen_settings.bg_color)
    for projectile in ammo.sprites():
        projectile.draw_weapon()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()
