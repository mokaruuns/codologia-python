from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

s = [[[1, 1, 1], [1, 0, 1], [1, 1, 1]],
     [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
     [[1, 1, 1], [1, 0, 1], [1, 1, 1]]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            mc.setBlock(x + i, y + j, z + k, s[i][j][k])
