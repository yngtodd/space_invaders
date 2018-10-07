import os
import pygame


class Ship:
    """
    Friendly ship.
    """
    basedir = os.path.dirname(__file__)
    sprite_path = os.path.join(basedir, 'img/ship.png')

    def __init__(self, ship_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = ship_settings
        self.set_initial_position()
        # Movement flags
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """
        Draw the ship at the current location.
        """
        self.screen.blit(self.img, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom

    def set_initial_position(self):
        """Initial position of ship"""
        self.img = pygame.image.load(self.sprite_path)
        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        """
        Update the ship's position based on movement flag.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.ship_speed_factor

        if self.moving_up and self.screen_rect.top < self.rect.top:
            self.centery -= self.settings.ship_speed_factor

        if self.moving_down and self.screen_rect.bottom > self.rect.bottom:
            self.centery += self.settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
