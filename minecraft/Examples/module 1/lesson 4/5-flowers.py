import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 8)
    time.sleep(0.5)
