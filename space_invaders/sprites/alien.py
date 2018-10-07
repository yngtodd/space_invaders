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
        self.img = pygame.image.load(self.sprite_path)
        self.rect = self.img.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.img, self.rect)
