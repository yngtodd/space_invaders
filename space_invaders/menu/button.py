import pygame.font


class Button:

    def __init__(self, screen_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = screen_settings.width / 4
        self.height = screen_settings.height / 4
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into rendered image centered on the button."""
        self.msg_img = self.font.render(msg, True, self.text_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        """Render button and text."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)


