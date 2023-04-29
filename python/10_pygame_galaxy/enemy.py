from shuttle import Shuttle


class Enemy(Shuttle):
    def auto_moving(self):
        for i in range(10):
            self.right()
        for i in range(10):
            self.left()
