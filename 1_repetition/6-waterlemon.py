from mcpi.minecraft import Minecraft

mc = Minecraft.create()

import time

time.sleep(30)
blockHits = mc.events.pollBlockHits()

for i in range(len(blockHits)):  # (0, 1, 2, 3, .., len(bH) - 1)
    print(blockHits[i].pos.x, blockHits[i].pos.y, blockHits[i].pos.z, blockHits[i].type)
    mc.setBlock(blockHits[i].pos.x, blockHits[i].pos.y, blockHits[i].pos.z, 11)

# и ниже то же самое другим способом

time.sleep(5)

for elem in blockHits:
    mc.setBlock(elem.pos.x, elem.pos.y, elem.pos.z, 103)
