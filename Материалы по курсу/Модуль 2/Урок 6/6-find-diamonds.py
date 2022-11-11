from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 56 - идентификатор алмазной руды
pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z
blocks = []
с = 0
while c < y:
    blocks.append(mc.getBlock(x, c, z))
    с += 1
if 56 in blocks:
    mc.postToChat(x, blocks.index(56), z)
    print(x, blocks.index(56), z)
else:
    mc.postToChat("no diamonds here")
    print("no diamonds here")
