import pygame
import sys

def run_game():
    """ Game that prints the keys being pressed."""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Key Pressing")
    
    bg_color = (230, 230, 230)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

    screen.fill(bg_color)
    pygame.display.flip()       
    
run_game()