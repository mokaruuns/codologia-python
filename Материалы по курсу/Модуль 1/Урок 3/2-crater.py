from mcpi.minecraft import Minecraft

mc = Minecraft.create()

answer = input("Создать кратер? Да/Нет ")
if answer == "Да":
    p = mc.player.getPos()
    mc.setBlocks(p.x + 1, p.y + 1, p.z + 1, p.x - 1, p.y - 1, p.z - 1, 0)
    # mc.postToChat("It is done!")
