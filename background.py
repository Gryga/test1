import pygame

class Background():
    def __init__(self, screen):
        self.screen = screen
        self.bg_img = pygame.image.load('Parallax100.png')
        self.bg_img = pygame.transform.scale(self.bg_img,(1000, 800))
        self.rect_img = self.bg_img.get_rect()

        self.bg_speed = 2
        self.bg_y1 = 0
        self.bg_y2 = -self.rect_img.width

    def update(self):
        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed
        if self.bg_y1 >= self.rect_img.width:
            self.bg_y1 = -self.rect_img.width

        if self.bg_y2 >= self.rect_img.width:
            self.bg_y2 = -self.rect_img.width

        self.screen.blit(self.bg_img, (self.bg_y1, 0))
        self.screen.blit(self.bg_img, (self.bg_y2, 0))

        print(self.bg_y1)

