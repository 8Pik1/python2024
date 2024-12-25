sizex = 15
sizey = 15

for y in range(sizey):
    for x in range(sizex):
        if 2 * x - y == 0 or 2 * x + y == 28 or y == 0:
            print("X  ",end="")
        else:
            print("   ", end="")
    print()
