from mcpi.minecraft import Minecraft

mc = Minecraft.create()
# импортируем библиотеку с командами
# для поиска рандомных чисел
import random


def randomPlaceBlock(blockType, repeats):
    count = 0
    while count < repeats:
        x = random.randint(-127, 127)
        z = random.randint(-127, 127)
        y = mc.getHeight(x, z)
        mc.setBlock(x, y, z, blockType)
        count += 1


randomPlaceBlock(8, 8000)
