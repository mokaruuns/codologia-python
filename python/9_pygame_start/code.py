import pygame
import random

pygame.init()

pygame.display.set_caption("Наша игра")

screen = pygame.display.set_mode((800, 600))

x_r1 = 400
y_r1 = 300
speed = 50

BLUE = (0, 0, 255)
YELLOW = (247, 242, 26)
BLACK = (0, 0, 0)

while True:
    # pygame.event.get() получает все события
    for event in pygame.event.get():
        # pygame.QUIT - тип события закрывающего программу
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.draw.circle(screen,
                                   YELLOW,
                                   (random.randint(0, 800),
                                    random.randint(0, 600)),
                                   random.randint(10, 50))
            if event.key == pygame.K_w:
                y_r1 -= speed
            if event.key == pygame.K_s:
                y_r1 += speed
            if event.key == pygame.K_a:
                x_r1 -= speed
            if event.key == pygame.K_d:
                x_r1 += speed

            # if event.key == pygame.K_r:
                
    r1 = pygame.Rect(x_r1, y_r1, 100, 100)
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, r1)  # Рисуем прямоугольник методом rect
    pygame.display.update()

#
# play = True
#
# clock = pygame.time.Clock()
#
# r1 = pygame.Rect(0, 0, 100, 100)  # Создаем прямоугольник
# BLUE = (0, 0, 255)  # Задаем синий цвет в формате RGB
# pygame.draw.rect(screen, BLUE, r1)  # Рисуем прямоугольник методом `py
#
# while play:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             play = False
#             quit()
#     clock.tick(60)
#     pygame.display.update()
