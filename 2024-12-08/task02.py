sizex = 15
sizey = 15

for y in range(sizey):
    for x in range(sizex):
        if y > 0 and x < 14 and x > 0 and y < 14:
            print("X  ",end="")
        else:
            print("   ", end="")
    print()


