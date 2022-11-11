class Cat(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


fluff = Cat('Пушок', 4.5)
print(fluff.weight)

fluff.name = 'Барсик'
print(fluff.name)
