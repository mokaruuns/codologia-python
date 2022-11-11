from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# положил в переменную координаты игрока
pos = mc.player.getPos()
# нашел идентификатор блока, который находится под игроком
id = mc.getBlock(pos.x, pos.y, pos.z)
# отправил в чат значение выполнения операции ((ид равен 8) или (ид равен 9))
mc.postToChat((id == 8) or (id == 9))
