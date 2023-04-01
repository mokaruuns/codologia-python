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
        self.food = [Food(True), Food(False)]
        self.bg = pygame.image.load("images/background.jpg").convert()
        self.bg = pygame.transform.scale(self.bg, (800, 600))

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
        # self.screen.fill(BLACK)
        self.screen.blit(self.bg, (0, 0))
        for product in self.food:
            product.draw(self.screen)
        self.snake.draw(self.screen)
        self.draw_score()

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(str(self.score), True, BLACK)
        self.screen.blit(text_surface, (0, 0))

    def eat(self):
        count_food = self.snake.eat(self.food)
        if count_food != 0:
            self.score += count_food
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
