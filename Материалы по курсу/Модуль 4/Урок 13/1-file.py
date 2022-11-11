file = open("file.txt", "w")  # "r", "a" (write, read, add)
# write, r == read, a == add - добавить
# write полностью стирает файл, файл открывается пустым
# r не стирает файл, ты просто можешь его прочитать
# a означает дописать что-то в конец файла - файл не стирается

file.write("бла-бла")
file.close()

file = open("file.txt", "r")
print(file.read())
file.close()
