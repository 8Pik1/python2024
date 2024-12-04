# Задание 4: четные числа

n = int(input("Введите число: "))
w = 1
while w <= n:
    if w % 2 == 0:
        print(w, end=" ")
    w = w + 1

