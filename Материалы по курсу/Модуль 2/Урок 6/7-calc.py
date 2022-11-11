a = ''
z = 0
while a != 'выход':
    a = input(
        'введите арифметическое выражение вида "первое_число"+"арифметический_знак"+"второе_число" или "выход" для прекращения работы программы: ')
    if a.lower() != 'выход':
        if '+' in a:
            z = a.index('+')
        elif '-' in a:
            z = a.index('-')
        elif '*' in a:
            z = a.index('*')
        elif '/' in a:
            z = a.index('/')
        number1 = a[:z]
        number2 = a[z + 1:]
        try:
            number1 = int(number1)
            number2 = int(number2)
            if a[z] == '/' and number2 == 0:
                print('делить на ноль нельзя')
            else:
                if a[z] == '+':
                    print('ответ:', number1 + number2)
                elif a[z] == '-':
                    print('ответ:', number1 - number2)
                elif a[z] == '*':
                    print('ответ:', number1 * number2)
                elif a[z] == '/':
                    print('ответ:', number1 / number2)
        except ValueError:
            print('повторите ввод')
        z = 0
