import time


# функция с 2 аргументами
def helloAndBye(personName, secsToWait):
    print("Привет, " + personName)
    time.sleep(secsToWait)
    print("Пока, " + personName)


helloAndBye("Филипп", 5)
# подаём в функцию в переменные
# personName Филипп, а в secsToWait 5
