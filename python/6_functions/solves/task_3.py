def count_a(word):
    k = 0
    for s in word:
        if s == 'a':
            k += 1
    return k


print(count_a("apple"))
print(count_a("apple a"))
print(count_a(""))
print(count_a("snjnj dsi"))
