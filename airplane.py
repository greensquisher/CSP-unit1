distance = float(input("How far are you traveling"))
speed = float(input("how fast does the plane go"))
wind = float(input("any wind (positive or negative)"))
print("it should take you about", ((distance/(speed*wind)," hours")))