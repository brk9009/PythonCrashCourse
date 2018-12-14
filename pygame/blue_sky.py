#12.1 Python Crash Course
import sys
import pygame

from controller import Controller

def blue_screen():
    """Creates a screen with a background color of blue"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Screen")

    controller = Controller(screen)

    while True:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0,0,255))
        controller.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

blue_screen()
