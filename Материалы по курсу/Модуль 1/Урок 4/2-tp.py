import random
import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

count = 1
while count < 10:
    # выбираем случайные координаты x,y,z
    x = random.randint(-127, 127)
    y = random.randint(0, 127)
    z = random.randint(-127, 127)
    count = count + 1
    mc.player.setTilePos(x, y, z)
    time.sleep(1)
