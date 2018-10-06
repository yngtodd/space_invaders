import pygame
from pygame.sprite import Sprite


class Weapon(Sprite):
    """
    Weapons fired by the ship.
    """
    def __init__(self, weapon_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, weapon_settings.width, weapon_settings.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.color = weapon_settings.color
        self.speed_factor = weapon_settings.speed_factor
        self.y = float(self.rect.y)

    def update(self):
        """Move the weapon up the screen."""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_weapon(self):
        """Draw the weapon to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
