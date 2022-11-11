# подключаемся к Майнкрафту
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# присваиваем переменным x,y,z значения координат
x = 100
y = 100
z = 100

# меняем позицию игрока
mc.player.setTilePos(x, y, z)
