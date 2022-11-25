from mcpi.minecraft import Minecraft

mc = Minecraft.create()


# функция, помогающая упорядочить 2 числа в порядке возрастания
def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2


# функция, позволяющая "ввести" трёхмерный список (кубоид) из майнкрафта в питон
def copyStructure(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)
    # находим ширину, высоту и длину кубоида
    width = x2 - x1
    height = y2 - y1
    length = z2 - z1
    # создаём трёхмерный список, заполняя его нулями
    structure = []
    for i in range(length):
        structure.append([])
        for j in range(height):
            structure[i].append([])
            for k in range(width):
                structure[i][j].append(0)
    print("Wait, please")
    # меняем значения в трёхмерном списке с нулей на идентификаторы соответствующих блоков
    for z in range(length):
        for y in range(height):
            for x in range(width):
                structure[z][y][x] = mc.getBlock(x1 + x, y1 + y, z1 + z)
    return structure


# функция, позволяющая "вывести" кубоид из питона в майнкрафт
def buildStructure(x, y, z, structure):
    xStart = x
    yStart = y
    zStart = z
    # здесь используем другой вариант обхода - по элементам трёхмерного списка
    # в этом случае приходится исхищряться с переменными x,y,z - довольно неудобно
    # попробуйте переписать этот цикл, чтобы он стал более читабельным
    for depth in structure:
        for width in depth:
            for block in width:
                mc.setBlock(x, y, z, block)
                x += 1
            y += 1
            x = xStart
        z += 1
        y = yStart


input("Пройдите к первому углу и нажмите Enter в этом окне. ")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z

input("Пройдите к противоположному углу и нажмите Enter в этом окне. ")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z

structure = copyStructure(x1, y1, z1, x2, y2, z2)

input("Перейдите туда, где вы хотите создать конструкцию, и нажмите Enter в этом окне. ")
pos = mc.player.getTilePos()
buildStructure(pos.x, pos.y, pos.z, structure)
