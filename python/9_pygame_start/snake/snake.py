import pygame


class Snake:
    def __init__(self, speed, start, radius):
        self.direction = (0, 0)
        self.speed = speed
        self.tail = []
        self.head = start
        self.color = (255, 0, 0)
        self.radius = radius

    def turn_left(self):
        self.direction = (-1, 0)

    def turn_right(self):
        self.direction = (1, 0)

    def turn_up(self):
        self.direction = (0, -1)

    def turn_down(self):
        self.direction = (0, 1)

    def move(self):
        self.head = (self.head[0] + self.direction[0] * self.speed,
                     self.head[1] + self.direction[1] * self.speed)
        self.head = (self.head[0] % 800, self.head[1] % 600)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.head, self.radius)
