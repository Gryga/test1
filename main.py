import pygame,sys

import game_function as g_f

from settings import Settings

from element import Element

from pygame.sprite import Group

from background import Background
from alien import Alien

def init_game():
    pygame.init()

    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))

    element = Element(screen)


    bullets = Group()

    aliens = Group()
    alien = Alien(game_settings, screen)

    pygame.display.set_caption('Game')

    background = Background(screen)

    g_f.create_fleet(game_settings, screen, aliens)
    while True:

        g_f.check_events(game_settings, screen, element, bullets, alien)

        g_f.update_screen(element, bullets, background, aliens, screen)

        element.update()

        g_f.update_bullets(bullets)




init_game()