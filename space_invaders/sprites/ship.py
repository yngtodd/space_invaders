import os
import pygame


class Ship:
    """
    Friendly ship.
    """
    basedir = os.path.dirname(__file__)
    sprite_path = os.path.join(basedir, 'img/ship.png')

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.img = pygame.image.load(self.sprite_path)
        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False

    def blitme(self):
        """
        Draw the ship at the current location.
        """
        self.screen.blit(self.img, self.rect)

    def update(self):
        """
        Update the ship's position based on movement flag.
        """
        if self.moving_right:
            self.rect.centerx += 1
