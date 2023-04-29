from shuttle_view import ShuttleView
from bullet import Bullet

class Shuttle:
    def __init__(self, hp, speed):
        self.hp = hp
        self.speed = speed
        self.armor = 0
        self.bullets = []
        self.shuttle_view = ShuttleView()

    def draw(self, screen):
        self.shuttle_view.draw(screen)
        for bullet in self.bullets:
            bullet.bullet_view.draw(screen)

    def up(self):
        self.shuttle_view.up(self.speed)

    def down(self):
        self.shuttle_view.down(self.speed)

    def left(self):
        self.shuttle_view.left(self.speed)

    def right(self):
        self.shuttle_view.right(self.speed)

    def fire(self):
        self.bullets.append(Bullet(
            x=self.shuttle_view.rect.x + self.shuttle_view.radius // 2,
            y=self.shuttle_view.rect.y
        ))

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.bullet_view.up(bullet.speed)
            if bullet.bullet_view.rect.y < 5:
                self.bullets.remove(bullet)

