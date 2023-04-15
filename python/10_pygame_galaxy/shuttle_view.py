import pygame


class ShuttleView(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 40
        self.set_image('images/shuttles/shuttle_easy.png')

    def set_image(self, file):
        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
