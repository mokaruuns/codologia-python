import pygame
from shuttle import Shuttle

BLUE = (0, 0, 255)
YELLOW = (247, 242, 26)
BLACK = (0, 0, 0)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Galaxy battle")

        self.score = 0
        self.screen = pygame.display.set_mode((800, 600))
        self.shuttle = Shuttle(100, 100)
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill(BLACK)
        self.shuttle.draw(self.screen)

    def play(self):
        while True:
            self.clock.tick(60)
            # self.key_control()
            # self.shuttle.move()
            self.draw()
            pygame.display.update()


game = Game()
game.play()
