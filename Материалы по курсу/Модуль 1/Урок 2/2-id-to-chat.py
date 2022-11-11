from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# положим в переменную pos координаты игрока
pos = mc.player.getPos()
# загрузим в переменную message идентификатор
# (номер) блока, на котором стоит персонаж
message = mc.getBlock(pos.x, pos.y, pos.z)
# отправим в чат сообщение с идентификатором блока
mc.postToChat(message)
