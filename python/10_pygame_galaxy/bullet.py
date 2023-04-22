import pygame
from bullet_view import BulletView


class Bullet:
    def __init__(self, speed=5, damage=1, x=0, y=0):
        self.speed = speed
        self.damage = damage
        self.bullet_view = BulletView(x, y)
