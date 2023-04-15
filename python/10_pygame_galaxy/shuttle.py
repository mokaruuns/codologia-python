from shuttle_view import ShuttleView
from bullet import Bullet

class Shuttle:
    def __init__(self, hp, speed):
        self.hp = hp
        self.speed = speed
        self.armor = 0
        self.patrons = 100
        self.bullets = [Bullet()]
        self.shuttle_view = ShuttleView()

    def draw(self, screen):
        self.shuttle_view.draw(screen)

    def up(self):
        self.shuttle_view.up(self.speed)

    def down(self):
        self.shuttle_view.down(self.speed)

    def left(self):
        self.shuttle_view.left(self.speed)

    def right(self):
        self.shuttle_view.right(self.speed)