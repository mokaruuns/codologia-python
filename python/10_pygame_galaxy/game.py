import pygame
from shuttle import Shuttle
from enemy import Enemy
from random import randint

BLUE = (0, 0, 255)
YELLOW = (247, 242, 26)
BLACK = (0, 0, 0)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Galaxy battle")

        self.score = 0
        self.screen = pygame.display.set_mode((800, 600))
        self.shuttle = Shuttle(10, 10)
        self.clock = pygame.time.Clock()
        self.enemies = [Enemy(0, 0), Enemy(0, 0)]

    def draw(self):
        self.screen.fill(BLACK)
        self.shuttle.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)

    def play(self):
        while True:
            self.clock.tick(60)
            self.key_control()
            self.shuttle.move_bullets()
            for enemy in self.enemies:
                enemy.move_bullets()
                enemy.auto_moving()
                enemy.get_damage(self.shuttle.bullets)
                self.shuttle.get_damage(enemy.bullets)
                if enemy.hp <= 0:
                    self.enemies.remove(enemy)
                    self.enemies.append(Enemy(enemy.hp * 1.5, enemy.speed * 1.5))
            self.draw()
            pygame.display.update()

    def key_control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.shuttle.left()
        if keys[pygame.K_RIGHT]:
            self.shuttle.right()
        if keys[pygame.K_UP]:
            self.shuttle.up()
        if keys[pygame.K_DOWN]:
            self.shuttle.down()
        if keys[pygame.K_SPACE]:
            self.shuttle.fire()

        for enemy in self.enemies:
            if abs(enemy.shuttle_view.rect.x - self.shuttle.shuttle_view.rect.x) < 10:
                enemy.fire()


game = Game()
game.play()
