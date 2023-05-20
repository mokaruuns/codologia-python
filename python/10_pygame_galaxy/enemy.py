import random

from shuttle import Shuttle
from enemy_view import EnemyView
from bullet import Bullet


class Enemy(Shuttle):
    def __init__(self, hp, speed):
        if hp == 0:
            hp = random.randint(50, 150)
        if speed == 0:
            speed = random.randint(1, 5)
        super().__init__(hp, speed)
        self.shuttle_view = EnemyView()

    def auto_moving(self):
        self.shuttle_view.set_direction()
        self.shuttle_view.move(self.shuttle_view.direction, self.speed)

    def get_damage(self, bullets):
        for bullet in bullets:
            if bullet.bullet_view.rect.colliderect(self.shuttle_view.rect):
                self.hp -= bullet.damage
                bullets.remove(bullet)

    def fire(self):
        self.bullets.append(Bullet(
            x=self.shuttle_view.rect.x + self.shuttle_view.radius // 2,
            y=self.shuttle_view.rect.y + self.shuttle_view.radius,
            speed=5,
            damage=10,
            enemy=True
        ))
    def move_bullets(self):
        for bullet in self.bullets:
            bullet.bullet_view.down(bullet.speed)
            # if bullet.bullet_view.rect.y < 5:
            #     self.bullets.remove(bullet)