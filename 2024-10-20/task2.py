# Задание 2: три числа

a = int(input("Введите первое число: "))
m0 = a
m1 = a
s = a

a = int(input("Введите второе число: "))
if a < m0:
    m0 = a
if a > m1:
    m1 = a
s = s + a

a = int(input("Введите третье число: "))
if a < m0:
    m0 = a
if a > m1:
    m1 = a
s = s + a

s = s / 3

k = int(input("Выберите что посчитать (1 - максимум, 2 - минимум, 3 - среднее арифметическое): "))
if k == 1:
    print("Наибольшее число:", m1)
elif k == 2:
    print("Наименьшее число:", m0)
elif k == 3:
    print("Среднее арифмитическое трех чисел:", s)
else:
    print("Введена неверная команда")
