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
        self.tail.append(Body(self.head.position))
        self.tail.pop(0)

        self.head.move(self.direction, self.speed)

    def draw(self, screen):

        for b in self.tail:
            b.draw(screen)
        self.head.draw(screen)

    def eat(self, food):
        score = 0
        for product in food:
            if self.head.rect.colliderect(product.rect):
                if product.is_health:
                    score += 1
                else:
                    score -= 5
                food.remove(product)
                del product
                food.append(Food(True))
                self.add()

        return score

    def add(self):
        self.tail.append(Body(self.head.position))
