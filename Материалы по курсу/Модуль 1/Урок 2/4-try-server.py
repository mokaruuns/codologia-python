try:
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    pos = mc.player.getPos()
    print(pos.x, pos.y, pos.z)
    break
except ConnectionRefusedError:
    print("Пожалуйста, зайдите на сервер, и тогда я определю ваши координаты. ")
