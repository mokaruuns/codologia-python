import random

from shuttle import Shuttle
from enemy_view import EnemyView


class Enemy(Shuttle):
    def __init__(self, hp, speed):
        super().__init__(hp, speed)
        self.shuttle_view = EnemyView()

    def auto_moving(self):
        self.shuttle_view.set_direction()
        self.shuttle_view.move(self.shuttle_view.direction, self.speed)
        print(self.shuttle_view.direction)
