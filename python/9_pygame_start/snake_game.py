import pygame
import random


class Game:
    def __init__(self):
        self.score = 0


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




pygame.init()

pygame.display.set_caption("Змейка")

screen = pygame.display.set_mode((800, 600))

BLUE = (0, 0, 255)
YELLOW = (247, 242, 26)
BLACK = (0, 0, 0)

snake = Snake(10, (400, 250), 20)
snake.draw(screen)

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    # pygame.event.get() получает все события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.turn_up()
            if event.key == pygame.K_a:
                snake.turn_left()
            if event.key == pygame.K_s:
                snake.turn_down()
            if event.key == pygame.K_d:
                snake.turn_right()
    screen.fill(BLACK)

    snake.move()
    snake.draw(screen)
    pygame.display.update()
