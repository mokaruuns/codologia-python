from mcpi.minecraft import Minecraft

mc = Minecraft.create()

import time

time.sleep(30)  # ждём 30 секунд
blockHits = mc.events.pollBlockHits()  # получаем список блоков, на которые игрок нажал (правая кнопка мыши+меч)
print(blockHits)  # печатаем список
for i in range(len(blockHits)):  # перебираем все элементы списка
    mc.setBlock(blockHits[i].pos.x, blockHits[i].pos.y, blockHits[i].pos.z, 11)  # заменяем блок на арбуз

# и ниже то же самое другим способом
time.sleep(5)
for elem in blockHits:  # перебираем все элементы списка
    mc.setBlock(elem.pos.x, elem.pos.y, elem.pos.z, 103)  # заменяем блок
