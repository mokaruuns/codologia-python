from mcpi.minecraft import Minecraft

mc = Minecraft.create()

places = {'Дом': [76, 1, -61],
          'Площадь': [61, 9, -61],
          'Шахта': [24, 124, 34]}

place = input("Введите место, куда Вы хотите телепортироваться: ")

location = places[place]
x, y, z = location[0], location[1], location[2]
mc.player.setPos(x, y, z)
