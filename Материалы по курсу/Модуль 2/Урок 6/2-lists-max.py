from mcpi.minecraft import Minecraft

mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
heights = [pos.y, pos.y]
count = 0

while count < 10:
    pos = mc.player.getTilePos()
    if pos.y < heights[0]:
        heights[0] = pos.y
    if pos.y > heights[1]:
        heights[1] = pos.y
    count += 1
    time.sleep(1)

mc.postToChat("min height:")
mc.postToChat(heights[0])
mc.postToChat("max height:")
mc.postToChat(heights[1])
