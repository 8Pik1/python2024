# Задание 2: числовой ряд

a1 = 0
res = 0
while a1 <= 50:
    a1 = a1 + 1
    if a1 % 3 == 0 : continue
    elif a1 % 7 == 0 :
        break
    print(a1)
