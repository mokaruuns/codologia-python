from mcpi.minecraft import Minecraft

mc = Minecraft.create()

import time

time.sleep(10)
blockHits = mc.events.pollBlockHits()
mc.postToChat(len(blockHits))
print(len(blockHits))
