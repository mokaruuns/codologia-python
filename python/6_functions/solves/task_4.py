def count_symbol(word, symbol):
    k = 0
    for s in word:
        if s == symbol: # 'a' == ''
            k += 1
    return k


print(count_symbol("apple", 'p'))
print(count_symbol("apple", 'q'))
print(count_symbol("apple", '1'))
print(count_symbol("apple", 'pp'))
print(count_symbol("apple", ''))
print(count_symbol("", 'p'))
print(count_symbol("'sd'", "1"))

