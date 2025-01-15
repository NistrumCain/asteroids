import sys
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    dt = 0

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:

            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
            if asteroid.collision(player):
                print("Game Over")
                sys.exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()