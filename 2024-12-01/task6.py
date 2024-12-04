# Задание 6: сумма четных чисел

n = int(input("Введите число: "))
w = 1
sum = 0
while w <= n:
    if w % 2 == 0:
        sum = sum + w
    w = w + 1
print(sum)
