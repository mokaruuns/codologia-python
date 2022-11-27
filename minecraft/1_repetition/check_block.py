import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()  # получаем список блоков, на которые игрок нажал (правая кнопка мыши+меч)
    for hit in hits:
        mc.postToChat("You hit block ({},{},{})".format(hit.pos.x, hit.pos.y, hit.pos.z))
    time.sleep(0.1)
