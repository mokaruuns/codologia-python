class Shuttle:
    def __init__(self, hp, speed):
        self.hp = hp
        self.speed = speed
        self.armor = 0
        self.patrons = 100
        self.gun = None
        self.shuttle_view = None

    def left(self):
        self.shuttle_view.left()

    def right(self):
        self.shuttle_view.right()

    def up(self):
        self.shuttle_view.up()

    def down(self):
        self.shuttle_view.down()

