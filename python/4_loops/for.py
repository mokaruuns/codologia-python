import random

number = random.randint(1, 100)

while True:
    user_number = int(input())
    if number > user_number:
        print("Загаданное число больше вашего")