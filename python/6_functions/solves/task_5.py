def has_even(numbers):
    a = 0
    for s in numbers:
        if s % 2 == 0:
            a += 1
    if a > 0:
        return True
    else:
        return False


print(has_even([1, 3, 5]))  # False
print(has_even([1, 2, 3]))  # True
# print(has_even(['a', 'b']))  # Ошибка
print(has_even([]))  # False
