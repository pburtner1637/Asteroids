import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        # 1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update game state (currently empty)

        # 3. Draw the game
        screen.fill('black')
        pygame.display.flip()

    pygame.quit()
    return

if __name__ == '__main__':
    main()
