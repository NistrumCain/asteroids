import pygame
from constants import *
def main():
    print("Starting asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        loop(screen)
def loop(screen: pygame.Surface):
    pygame.Surface.fill(screen, pygame.Color("black"))
if __name__ == "__main__":
    main()