alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
            'я']

code_alphabet = ['@', '#', '№', '$', '%', '^', '&', '~', '`', '|', '/', '>', '<', '[', ']',
                 '{', '}', '*', '=', 's', 'i', 'o', 'p', 'm', 'q', 'r', 'w', 'g', 'a', 'b',
                 'c', 'd', 'e']

file = open("in.txt", "r")
s = file.read()
file.close()

s = s.lower()
for i in range(33):
    s = s.replace(alphabet[i], code_alphabet[i])

file = open("out.txt", "w")
file.write(s)
file.close()
