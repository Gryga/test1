import pygame

from pygame.sprite import Sprite





class Bullet(Sprite):
    def __init__(self, game_settings, screen, element):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, game_settings.bullet_whith, game_settings.bullet_height)
        self.rect.centerx = element.rect.centerx
        self.rect.top = element.rect.top
        self.bullet_color = game_settings.bullet_color
        self.speed = game_settings.bullet_speed_factor

    def update(self):
        self.rect.y -= self.speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

