a = []  # заводим пустой список
n = int(input())  # считываем количество элементов в списке
count = 1
while count <= n:
    new_element = int(input())  # считываем очередной элемент
    a.append(new_element)  # добавляем его в список
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
    count += 1
print(a)
