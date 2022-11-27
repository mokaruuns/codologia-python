from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# положим в переменную message сообщение, которое хотим отправить
message = "Hello, Minecraft!"
# отправим в чат сообщение с идентификатором блока
mc.postToChat(message)
