import pygame
import sys
import constants
import player
import asteroid
import asteroidfield
import shot

def main():

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (updatable, drawable, shots)

    field = asteroidfield.AsteroidField()

    player_ship = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(dt)

        for rock in asteroids:
            if player_ship.collide(rock):
                print("Game Over!")
                sys.exit()
        
        for rock in asteroids:
            for bullet in shots:
                if bullet.collide(rock):
                    bullet.kill()
                    rock.split()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

