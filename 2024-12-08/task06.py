sizex = 15
sizey = 15

for y in range(sizey):
    for x in range(sizex):
       # if x >= 7:
           # print("0  ",end="")
        if y - x == 0 or x - y <= 0:
            print("X  ",end="")
        else:
            print("   ", end="")
    print()
