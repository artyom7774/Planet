import pygame
import math


class Particles:
    def __init__(self, game):
        self.game = game

        self.particles = []

    def create(self, x, y, color, angle, speed, radius, minus):
        dx = speed * math.cos(angle)
        dy = speed * math.sin(angle)

        self.particles.append([[x, y], [dx, dy], color, radius, minus])

    def update(self):
        for i, particle in enumerate(self.particles):
            self.particles[i][0][0] += particle[1][0]
            self.particles[i][0][1] += particle[1][1]

            self.particles[i][3] -= self.particles[i][4]

            if self.particles[i][3] <= 0:
                self.particles.pop(i)

    def draw(self):
        for particle in self.particles:
            pygame.draw.circle(self.game.screen, particle[2], particle[0], particle[3])
