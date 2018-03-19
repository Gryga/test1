import pygame

class Element():
    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('ship.png')
        self.image = pygame.transform.scale(self.image, (280, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.moving_right = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_top = False
        self.grow = False

    def update(self):



        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 10
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 10
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 10
        elif self.moving_top and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 10

        elif self.grow:
            self.image = pygame.transform.scale(self.image, (280 + 10, 200 + 10))












    def blitme(self):
        self.screen.blit(self.image,self.rect)