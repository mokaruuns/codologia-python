# импортируем команды для изменения мира майнкрафта
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# ищем позицию игрока
pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z

l = []  # создаём пустой список
# заполняем список идентификаторами блоков, которые находятся под персонажем
count = 1
while count < y:
    l.append(mc.getBlock(x, count, z))
    count += 1

# удаляем все ненужные блоки из списка (0 - воздух, 1 - камень, 3 - земля)
count = 0
while count < len(l):
    if (l[count] == 0) or (l[count] == 1) or (l[count] == 3):
        del l[count]
    else:
        count += 1

# ставим под персонажем блоки, оставшиеся в списке
y = mc.getHeight(x, z)
count = 0
while count < len(l):
    mc.setBlock(x, y + count, z, l[count])
    count += 1
