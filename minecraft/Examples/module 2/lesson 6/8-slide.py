from mcpi.minecraft import Minecraft

mc = Minecraft.create()

import time

import random

pos = mc.player.getPos()
x, y, z = pos.x, pos.y - 1, pos.z
while mc.getHeight(x, z) != y:
    mc.setBlock(x, y, z, 79)
    a = random.randint(1, 4)
    y -= 1
    if a == 1:
        x -= 1
    elif a == 2:
        x += 1
    elif a == 3:
        z -= 1
    elif a == 4:
        z += 1
    time.sleep(1)
