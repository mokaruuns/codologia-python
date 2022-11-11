from mcpi.minecraft import Minecraft

mc = Minecraft.create()
import random
import time

pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z + 5
for i in range(20):
    mc.setBlocks(x - 1, y, z, x + 1, y, z + 20, 10)

while True:
    mc.setBlocks(x, y, z, x, y + 1, z + 20, 0)
    for i in range(20):
        mc.setBlock(x, y + random.randint(0, 1), z + i, 1)
    time.sleep(1)
