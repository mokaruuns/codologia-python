import pygame
import random
from snake import Snake
from food import Food


class Game:
    def __init__(self):
        self.score = 0


pygame.init()

pygame.display.set_caption("Змейка")

screen = pygame.display.set_mode((800, 600))

BLUE = (0, 0, 255)
YELLOW = (247, 242, 26)
BLACK = (0, 0, 0)

snake = Snake(10, (400, 250), 20)
# для теста
snake.add()
snake.add()
snake.add()
snake.add()
snake.add()


clock = pygame.time.Clock()

food = [Food(), Food()]

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
    for product in food:
        product.draw(screen)
    snake.eat(food)
    snake.move()
    snake.draw(screen)
    pygame.display.update()
