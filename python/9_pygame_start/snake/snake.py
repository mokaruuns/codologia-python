import pygame
import queue
from head import Head
from food import Food
from body import Body


class Snake:
    def __init__(self, speed, start, radius):
        self.direction = (0, 0)
        self.speed = speed
        self.tail = []
        self.head = Head(start)
        self.color = (255, 0, 0)
        self.radius = radius

    def turn_left(self):
        self.direction = (-1, 0)
        self.head.left()

    def turn_right(self):
        self.direction = (1, 0)
        self.head.right()

    def turn_up(self):
        self.direction = (0, -1)
        self.head.up()

    def turn_down(self):
        self.direction = (0, 1)
        self.head.down()

    def move(self):
        self.tail.pop(0)
        self.tail.append(Body(self.head.position))

        self.head.move(self.direction, self.speed)

        print(self.head)

    def draw(self, screen):
        self.head.draw(screen)
        for b in self.tail:
            b.draw(screen)

    def eat(self, food):
        for product in food:
            if self.head.rect.colliderect(product.rect):
                print("Ам!")
                food.remove(product)
                del product
                food.append(Food())

    def add(self):
        self.tail.append(Body(self.head.position))
