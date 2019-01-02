import pygame

class Ship():
    
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/pirate-ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start ship on the left side in the center.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        
        # Store a decimal value for the ship's position
        self.center = float(self.rect.centery)
        
        # Movement flag for continuous movement
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the ship's position."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed
            
        # Update rect object from self.center.
        self.rect.centery = self.center
        
    def blitme(self):
        """Draw the ship"""
        self.screen.blit(self.image, self.rect)