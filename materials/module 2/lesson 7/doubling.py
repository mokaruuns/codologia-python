def doubling(number):
    # функция принимает число и возвращает удвоенное число
    return number * 2


# читаем с экрана информацию, превращаем в число
# и записываем это в переменную
c = int(input())
# записываем в переменную d результат выполнения функции
# с аргументом с
d = doubling(c)
# печатаем на экран результат
print(d)