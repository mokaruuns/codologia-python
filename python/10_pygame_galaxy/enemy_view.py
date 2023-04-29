from shuttle_view import ShuttleView


class EnemyView(ShuttleView):
    def __init__(self):
        super().__init__()
        self.direction = (1, 0)

    def set_direction(self):
        if self.rect.x < 100:
            self.direction = (1, 0)
        if self.rect.x > 700:
            self.direction = (-1, 0)
