import pygame
import random


class Head(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.radius = 40

        self.image = pygame.image.load('head.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
