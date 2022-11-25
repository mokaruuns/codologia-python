from mcpi.minecraft import Minecraft

mc = Minecraft.create()

import random


def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    return random.choice(brokenBlocks)


# 1) ввести переменные m,n - длина и ширина списка
# 2) заполнить двумерный список s рандомными элементами из
#    списка brokenBlocks
# 3) построить стену, выглядящую как двумерный список s

n = int(input())
m = int(input())
s = []

for i in range(n):
    s.append([])
    for j in range(m):
        s[i].append(brokenBlock())

pos = mc.player.getPos()
x, y, z = pos.x, mc.getHeight(pos.x, pos.z), pos.z

y = y + 5

for i in range(n):
    for k in range(m):
        mc.setBlock(x + k, y + i, z, s[i][k])
