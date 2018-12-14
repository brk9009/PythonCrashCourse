#12.2 Python Crash Course
import pygame

class Controller():

    def __init__(self,screen):
        self.screen = screen

        # Load the controller image and get its rect
        self.image = pygame.image.load('images/nintendo.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Draw the controller at the center of the screen
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        """Draw the controller at its current location"""
        self.screen.blit(self.image, self.rect)
