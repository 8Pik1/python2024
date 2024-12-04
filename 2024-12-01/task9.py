# Задание 9: подсчет цифр

n = int(input("Введите число: "))
w = 1
n = n // 10
while n > 0:
    n = n // 10
    w = w + 1
print(w)
