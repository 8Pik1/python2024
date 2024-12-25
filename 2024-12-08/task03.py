sizex = 15
sizey = 15

for y in range(sizey):
    for x in range(sizex):
        if 2 * x - y == 14 or 2 * x + y == 14 or y == 14:
            print("X  ",end="")
        else:
            print("   ", end="")
    print()
