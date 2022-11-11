from mcpi.minecraft import Minecraft

mc = Minecraft.create()
import time

# импортировали нужные команды

# счётчик бегает от 30 до 0
for i in range(30, -1, -1):
    # печатаем в чат, сколько секунд до конца игры
    mc.postToChat(i)
    # ждём 1 секунду
    time.sleep(1)
    # находим позицию игрока
    pos = mc.player.getPos()
    # если под игроком железная руда, то печатаем "ты победил" и break
    if mc.getBlock(pos.x, pos.y - 1, pos.z) == 15:
        mc.postToChat("You won!")
        break
else:
    # если break не сработал, печатаем "ты проиграл"
    mc.postToChat("You lose!")
