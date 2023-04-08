import pygame


class ShuttleView(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.set_image('images/shuttles/shuttle_easy.png')

    def set_image(self, param):
        pass