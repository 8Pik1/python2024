# Задание 10: Сумма цифр

n = int(input("Введите число: "))
sum = 0
while n > 0:
    w = n % 10
    sum = sum + w
    n = n // 10
print(sum, end=" ")
