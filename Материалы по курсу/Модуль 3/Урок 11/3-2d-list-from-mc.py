from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x = int(input("Введите х-координату: "))
y = int(input("Введите у-координату: "))
z = int(input("Введите z-координату: "))
n = int(input("Введите высоту: "))
m = int(input("Введите ширину: "))
# создаём пустой список
s = []

# вложенный цикл - залог успеха при работе с двумерными списками
for i in range(n):
    # добавляем новую строчку
    s.append([])
    # добавляем в новую строчку m элементов -
    # идентификаторов соответствующих блоков
    for j in range(m):
        s[i].append(mc.getBlock(x + j, y + i, z))
print(s)
