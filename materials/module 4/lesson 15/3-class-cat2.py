class Cat(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, food):
        self.weight = self.weight + 0.05
        print(self.name + ' ест ' + food)

    def eatAndSleep(self, food):
        self.eat(food)
        print(self.name + ' теперь спит...')


fluff = Cat('Пушок', 4.5)
print(fluff.weight)

fluff.name = 'Барсик'
print(fluff.name)

fluff.eat('рыбу')
fluff.eatAndSleep('Ваню')
