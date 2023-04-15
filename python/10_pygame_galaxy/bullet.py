import pygame
from bullet_view import BulletView

class Bullet:
    def __init__(self, speed=1, damage=1):
        self.speed = speed
        self.damage = damage
        self.bullet_view = BulletView()
