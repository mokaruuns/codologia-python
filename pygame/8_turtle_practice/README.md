# Turtle. Практика

## Функция

Функция - это блок кода, который выполняет определенную задачу. Функция может принимать параметры, а так же возвращать результат.

```python
def my_function(param1, param2):
    # do something
    return result # функция может возвращать результат, а может и не возвращать
```

## Практика. Ёлка с помощью функций

Давайте напишем программу, которая будет рисовать ёлку с помощью функций.
От самых простых к более сложным.

Первоначально нам нужно понять, как рисовать треугольник
### Треугольник

```python
def triangle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.goto(x + 100, y)
    t.goto(x + 50, y + 100)
    t.goto(x, y)
```

Теперь нарисуем пенек(квадрат)
### Пенек

```python
def penek(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    for i in range(4):
        t.forward(100)
        t.left(90)
```

Теперь нарисуем ёлку
### Ёлка
```python
def tree(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    penek(x + 30, y)
    triangle(x, y + 100)
    triangle(x, y + 200)
    triangle(x, y + 300)
```

Давайте упростим код, выделим общие части в функции

Например, функцию для переноса карандаша в нужную точку
### Перемещение карандаша
```python
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
```

Теперь наша функция tree выглядит так
### Ёлка
```python
def tree(x, y):
    move(x, y)
    penek(x + 30, y)
    triangle(x, y + 100)
    triangle(x, y + 200)
    triangle(x, y + 300)
```