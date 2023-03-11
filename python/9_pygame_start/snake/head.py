import pygame
import random


class Head(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.radius = 40
        self.set_image('head_down.png')

    def set_image(self, file):
        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect(center=self.fixed_position())

    def fixed_position(self):
        return self.position[0] + self.radius // 2, self.position[1] + self.radius // 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, direction, speed):
        self.rect.x = (self.rect.x + direction[0] * speed) % 800
        self.rect.y = (self.rect.y + direction[1] * speed) % 600
        self.position = (self.rect.x, self.rect.y)

    def right(self):
        self.set_image("head_right.png")

    def up(self):
        self.set_image("head_up.png")

    def down(self):
        self.set_image("head_down.png")

    def left(self):
        self.set_image("head_left.png")

    def set_position(self, position):
        self.position = position
