import pygame

pygame.init()

pygame.display.set_caption("Наша игра")

screen = pygame.display.set_mode((800, 600))

play = True

clock = pygame.time.Clock()

r1 = pygame.Rect(0, 0, 100, 100)  # Создаем прямоугольник
BLUE = (0, 0, 255)  # Задаем синий цвет в формате RGB
pygame.draw.rect(screen, BLUE, r1)  # Рисуем прямоугольник методом `py

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    clock.tick(60)
    pygame.display.update()
