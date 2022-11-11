from mcpi.minecraft import Minecraft

mc = Minecraft.create()

s = [1, 2, 3, 4, 5, 6, 7]

pos = mc.player.getPos()
x, z = pos.x, pos.z
y = mc.getHeight(x, z) + 5

for i in range(len(s)):
    mc.setBlock(x, y, z + i, s[i])
