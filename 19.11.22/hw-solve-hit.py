import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

blockHits = mc.events.pollBlockHits()

coins = 0


def teleport(x, y, z):
    mc.player.setTilePos(x, y, z)


def find_block(block_id, timeout):
    global coins

    mc.postToChat("Game started!")
    start_time = time.time()
    pred = 0
    while time.time() - start_time < timeout:
        k = time.time() - start_time

        # Вывод оставшегося времени
        if int(k) != pred:
            mc.postToChat(int(timeout - k))
            pred = int(k)

        # Проверка блока, на который нажал игрок
        for elem in mc.events.pollBlockHits():
            blockType = mc.getBlock(elem.pos.x, elem.pos.y, elem.pos.z)
            if blockType == block_id:
                coins += 10
                return True

    return False


def start_game():
    while find_block(15, 15) is False:
        mc.postToChat("You lose!")
        time.sleep(5)
        teleport(-120, 70, 250)
        time.sleep(5)
    mc.postToChat("You won!")


start_game()
