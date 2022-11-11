from mcpi.minecraft import Minecraft

mc = Minecraft.create()

showerX =
showerY =
showerZ =

width = 3
height = 3
length = 3

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if showerX <= x < showerX + width  # and ... and ... :
    mc.setBlocks(showerX, showerY, showerZ, showerX + width, showerY + height, showerZ + length, 8)
else:
    mc.setBlocks(showerX, showerY, showerZ, showerX + width, showerY + height, showerZ + length, 0)
