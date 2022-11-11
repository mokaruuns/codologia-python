# подключаемся к Майнкрафту
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# присваиваем переменной position 3 координаты игрока
position = mc.player.getTilePos()

# присваиваем переменным x,y,z значения координат игрока
x = position.x
y = position.y
z = position.z

# изменяем переменную y (ось Y - вверх!)
y = y + 10
# теперь x,y,z - координаты игрока, где персонаж должен
# оказаться после суперпрыжка

# телепортируем персонажа
mc.player.setTilePos(x, y, z)
