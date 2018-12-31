#12.1 Python Crash Course
import sys
import pygame

from controller import Controller

def nintendo():
    """Creates a screen with a nintendo controller in the center"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Nintendo")

    controller = Controller(screen)

    while True:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255,255,255))
        controller.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

nintendo()
