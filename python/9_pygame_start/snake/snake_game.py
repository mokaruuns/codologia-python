import pygame
from snake import Snake
from food import Food

BLUE = (0, 0, 255)
YELLOW = (247, 242, 26)
BLACK = (0, 0, 0)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Змейка")

        self.score = 0
        self.screen = pygame.display.set_mode((800, 600))
        self.snake = Snake(10, (400, 250), 30)
        self.clock = pygame.time.Clock()
        self.food = [Food(), Food()]

    def key_control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.snake.turn_up()
                if event.key == pygame.K_a:
                    self.snake.turn_left()
                if event.key == pygame.K_s:
                    self.snake.turn_down()
                if event.key == pygame.K_d:
                    self.snake.turn_right()

    def draw(self):
        self.screen.fill(BLACK)
        for product in self.food:
            product.draw(self.screen)
        self.snake.draw(self.screen)

    def eat(self):
        self.score += self.snake.eat(self.food)
        print("Текущий счет:", self.score)

    def play(self):
        while True:
            self.clock.tick(60)
            self.key_control()
            self.eat()
            self.snake.move()
            self.draw()
            pygame.display.update()


game = Game()
game.play()
