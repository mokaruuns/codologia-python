from flask import Flask
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

app = Flask(__name__)


@app.route("/")
def showName():
    return "My coordinates x: " + str(pos.x) + ", y: " + str(pos.y) + ", z: " + str(pos.z)


pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z

app.run()
