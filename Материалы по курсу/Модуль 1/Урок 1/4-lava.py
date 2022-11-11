# подключаемся к Майнкрафту
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# присваиваем переменным x,y,z значения координат игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# 10 - идентификатор лавы
blockType = 10

# изменяем координату у на -1
y = y - 1
# теперь блок с координатами (x,y,z) должен стать блоком лавы

# ставим блок лавы
mc.setBlock(x, y, z, blockType)
