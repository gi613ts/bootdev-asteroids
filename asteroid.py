import pygame
import circleshape
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            blue_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(blue_angle)
            vector2 = self.velocity.rotate(-blue_angle)
            rock1 = Asteroid(self.position[0], self.position[1], new_radius)
            rock1.velocity = vector1 * 1.2
            rock2 = Asteroid(self.position[0], self.position[1], new_radius)
            rock2.velocity = vector2
