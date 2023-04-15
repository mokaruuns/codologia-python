from shuttle_view import ShuttleView


class Shuttle:
    def __init__(self, hp, speed):
        self.hp = hp
        self.speed = speed
        self.armor = 0
        self.patrons = 100
        self.gun = None
        self.shuttle_view = ShuttleView()

    def draw(self, screen):
        self.shuttle_view.draw(screen)

    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass
