import sys
import pygame


def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(screen_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    screen.fill(screen_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
