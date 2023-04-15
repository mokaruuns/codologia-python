import pygame


class BulletView(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 5
        self.set_image('images/bullets/bullet.png')

    def set_image(self, file):
        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, direction, speed):
        next_x = (self.rect.x + direction[0] * speed)
        if 0 <= next_x <= 800 - self.radius:
            self.rect.x = next_x
        next_y = (self.rect.y + direction[1] * speed)
        if 0 <= next_y <= 600 - self.radius:
            self.rect.y = next_y

    def up(self, speed):
        self.move((0, -1), speed)

    def down(self, speed):
        self.move((0, 1), speed)

    def left(self, speed):
        self.move((-1, 0), speed)

    def right(self, speed):
        self.move((1, 0), speed)
