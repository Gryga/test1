import pygame, sys

from bullet import Bullet

from alien import Alien
def check_events(game_settings, screen, element, bullets, alien):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
            check_keydown_events(game_settings, screen, element, bullets, i)


        elif i.type == pygame.KEYUP:
            check_keyup_events(i, element)

    if element.rect.top == alien.rect.bottom:
        element.grow = True





def check_keydown_events(game_settings, screen, element, bullets, i):
    if i.key == pygame.K_RIGHT:
        element.moving_right = True

    elif i.key == pygame.K_LEFT:
        element.moving_left = True

    elif i.key == pygame.K_UP:
        element.moving_top = True

    elif i.key == pygame.K_DOWN:
        element.moving_bottom = True

    elif i.key == pygame.K_SPACE:
        if len(bullets) < game_settings.bullets_allowed:
            new_bullet = Bullet(game_settings, screen, element)
            bullets.add(new_bullet)


def create_fleet(game_settings, screen, aliens):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    for alien_number in range(number_aliens_x):
        alien = Alien(game_settings, screen)
        alien.rect.x = alien_width + 2 * alien_width * alien_number
        aliens.add(alien)


'''
def get_number_aliens_x(game_settings, alien_width):
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return (number_aliens_x)

def get_number_rows(game_settings, element_height, alien_height):
    available_space_y = game_settings.screen_width - (3 * alien_height) - element_height
    number_rows = int(available_space_y /available_space_y / (2 * alien_height))
    return (number_rows)

def create_alien(game_settings, aliens, alien_number, row_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * row_number
    aliens.add(alien)

def create_fleet(game_settings, screen, aliens, element):
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, element.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, aliens, alien_number, row_number)

'''





def check_keyup_events(i, element):
    if i.key == pygame.K_RIGHT:
        element.moving_right = False

    elif i.key == pygame.K_LEFT:
        element.moving_left = False

    elif i.key == pygame.K_UP:
        element.moving_top = False

    elif i.key == pygame.K_DOWN:
        element.moving_bottom = False




def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)





def update_screen(element, bullets, background, aliens, screen):
    aliens.update()
    background.update()
    element.blitme()
    #alien.blitme()
    aliens.draw(screen)



    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()