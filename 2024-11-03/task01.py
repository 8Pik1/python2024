# задание 1: четность и кратность числа

w = int(input("Введите число: "))
ost = w % 2
if ost == 0:
    print("Четное")
else:
    print("Не четное")
t = w % 5
if t == 0:
    print("Кратное пяти")
else:
    print("Не кратное пяти")