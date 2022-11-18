import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

blockHits = mc.events.pollBlockHits()


def teleport(x, y, z):
    mc.player.setTilePos(x, y, z)


def find_block(block_id, timeout):
    mc.postToChat("Game started!")
    start_time = time.time()
    pred = 0
    while time.time() - start_time < timeout:
        k = time.time() - start_time
        if int(k) != pred:
            mc.postToChat(int(timeout - k))
            pred = int(k)
        pos = mc.player.getTilePos()
        block = mc.getBlock(pos.x, pos.y - 1, pos.z)
        if block == block_id:
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
