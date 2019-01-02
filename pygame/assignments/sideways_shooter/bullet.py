import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage bullets fired from a ship."""
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        
        # Create a bullet at (0,0) then set the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        
        # Set bullet's center as same as ship
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right
        
        # Store the bullet's position as a decimal
        self.x = float(self.rect.x)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed
        
    def update(self):
        """Move the bullet across."""
        self.x += self.speed_factor
        # Update the rect position
        self.rect.x = self.x
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)