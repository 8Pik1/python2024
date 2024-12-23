sizex = 15
sizey = 15

for y in range(sizey):
    for x in range(sizex):
        if y == 0 or x == 14 or x == 0 or y == 14:
            print("X  ",end="")
        else:
            print("   ", end="")
    print()

