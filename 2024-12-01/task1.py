# Задание 1: сумма чисел

n = int(input("Введите число: "))
w = 1
sum = 0
while w <= n:
    sum = sum + w
    w = w + 1
print("Вывод: ",sum)
