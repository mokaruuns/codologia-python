n = int(input("Введите кол-во чисел, пожалуйста: "))
maxn = int(input())
minn = maxn
for i in range(n - 1):
    number = int(input())
    if number > maxn:
        maxn = number
    if number < minn:
        minn = number
print(maxn - minn)
