# подключаемся к Майнкрафту
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# присваиваем переменным x,y,z значения координат
x = -10
y = 100
z = 173
blockType = 103

# ставим блок
mc.setBlock(x, y, z, blockType)

y = y + 1
mc.setBlock(x, y, z, blockType)
y = y + 1
mc.setBlock(x, y, z, blockType)
y = y + 1
mc.setBlock(x, y, z, blockType)
y = y + 1
mc.setBlock(x, y, z, blockType)
