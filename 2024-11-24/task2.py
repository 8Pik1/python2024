# Задание 2: счастливый билет

n = int(input("Введите шестизначное число: "))
x = []
for _ in [1,2,3,4,5,6]:
    x.append(n%10)
    n = n // 10
d = (x[5]+x[4]+x[3])-(x[2]+x[1]+x[0])

if d == 0:
    print("Счастливый билет")
else:
    print("Несчастливый билет")
