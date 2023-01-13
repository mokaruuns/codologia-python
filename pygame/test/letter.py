import sys


def different_letter(cur, new):
    k = 0
    for i in range(len(cur)):
        if cur[i] != new[i]:
            k += 1

    return k

def similar(word, dictionary):
    for i in dictionary:
        if different_letter(word, i) == 1:
            d2 = dictionary.copy()
            d2.remove(i)
            print(word, i)
            similar(i, d2)

a = list(map(str.strip, sys.stdin.readlines()))

similar(a[0], a[1:])

'''
test 
cat
bat
hat
lat
'''