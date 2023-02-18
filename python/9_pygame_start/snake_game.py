import pygame
import random

pygame.init()

pygame.display.set_caption("Змейка")

screen = pygame.display.set_mode((800, 600))



BLUE = (0, 0, 255)
YELLOW = (247, 242, 26)
BLACK = (0, 0, 0)

while True:
    # pygame.event.get() получает все события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


    screen.fill(BLACK)
    pygame.display.update()

