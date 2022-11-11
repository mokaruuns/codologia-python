soup = ["вода", "помидоры", "лук", "вермишель", "говядина"]
print(len(soup))  # печать длины списка на экран
print(soup)
soup.append("приправы")  # добавление элемента в конец списка
print(len(soup))  # печать длины списка на экран
print(soup)
soup.insert(3, "топор")  # вставка элемента на 3 место
print(len(soup))  # печать длины списка на экран
print(soup)
soup.insert(3642, "абв")  # номер слишком большой, поэтому элемент вставится в конец списка
print(len(soup))  # печать длины списка на экран
print(soup)
del soup[2]  # удаление второго элемента списка
print(len(soup))  # печать длины списка на экран
print(soup)
waterPosition = soup.index("вода")  # поиск номера элемента "вода" в списке
del soup[waterPosition]  # снова удаление элемента с номером waterPosition
print(len(soup))  # печать длины списка на экран
print(soup)
