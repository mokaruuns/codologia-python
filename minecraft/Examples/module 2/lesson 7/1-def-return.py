def priceOfCookie(cost):
    price = cost + 2
    price = price * 10
    return price


# возвращаем в основную программу значение переменной price
# это то же самое, что и return (cost+2)*10

P = priceOfCookie(5)
print(P)
# это то же самое, что и print(priceOfCookie(5))
