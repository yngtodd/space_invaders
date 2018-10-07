import os
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Alien ship.
    """
    basedir = os.path.dirname(__file__)
    sprite_path = os.path.join(basedir, 'img/alien.png')

    def __init__(self, alien_settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = alien_settings
        # Initial positioning
        self.image = pygame.image.load(self.sprite_path)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Check if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the aliens right."""
        self.x += (self.settings.speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
