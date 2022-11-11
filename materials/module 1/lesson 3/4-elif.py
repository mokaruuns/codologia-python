from mcpi.minecraft import Minecraft

mc = Minecraft.create()

hasApple = False
hasChocolate = True
if hasApple:
    print("беру яблоко")
elif hasChocolate:
    print("не, хочу шоколадку")
else:
    print("ладно, потом поем")
