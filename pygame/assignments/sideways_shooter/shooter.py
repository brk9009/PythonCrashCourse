import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """Game that shoots bullets across the screen left-to-right."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Sideways Shooter")
    
    # Make a ship
    ship = Ship(screen, ai_settings)
    # Make a group to store bullets in.
    bullets = Group()
    
    while True:
        
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
    
    
run_game()