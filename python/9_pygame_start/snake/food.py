import pygame
import random


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position = (random.randint(0, 800), random.randint(0, 600))
        self.radius = 40

        self.image = pygame.image.load('images/apple.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
