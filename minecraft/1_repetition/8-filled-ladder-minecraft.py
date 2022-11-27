from mcpi.minecraft import Minecraft

mc = Minecraft.create()

n = int(input())
pos = mc.player.getPos()
x, y, z = pos.x, mc.getHeight(pos.x, pos.z), pos.z
for i in range(n + 1):  # i = 1, 2, 3, ..., n
    mc.setBlocks(x + i, y, z, x + i, y + i, z, 53)
