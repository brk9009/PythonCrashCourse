import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
        
def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Get rid of bullets
    for bullet in bullets.copy():
        if bullet.rect.left > 1200:
            bullets.remove(bullet)
            
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
            
def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    
    # Redraw all the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
        
    # Make recent screen visible
    pygame.display.flip()
    