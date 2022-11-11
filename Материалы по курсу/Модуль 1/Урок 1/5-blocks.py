# подключаемся к Майнкрафту
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# присваиваем переменным x,y,z значения координат первого угла параллелепипеда
x = -20
y = 100
z = 160
# присваиваем переменным ширина, высота и длина соответствующие параметры параллелепипеда
width = 20
height = 40
length = 20
# присваиваем переменной blockType идентификатор (номер) блока, из которого будем строить параллелепипед
blockType = 103

# ставим блоки
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
