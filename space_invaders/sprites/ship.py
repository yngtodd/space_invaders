import pygame


class Ship:
    """
    Friendly ship.
    """
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.img = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """
        Draw the ship at the current location.
        """
        self.screen.blit(self.img, self.rect)
