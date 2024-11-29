sizex = 40
sizey = 25

for y in range(sizey):
    for x in range(sizex):
       # if x >= 7:
           # print("0  ",end="")
        if ((x + y == 5 or y - x == 5 or x == 5) and y <= 10  and x <= 5) or (x >= 7 and x - y <= 7 and y + x <= 17 ) or ( x/2 - 13 ) ** 2 + ( y - 10 ) ** 2 <= 25:
            print("X  ",end="")
        else:
            print("-  ", end="")
    print()

