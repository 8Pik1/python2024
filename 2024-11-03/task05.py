# Задание 5: ИМТ

rost = int(input("Введите ваш рост (см): "))
ves = int(input("Введите ваш вес (кг): "))
index = ves / ((rost / 100) ** 2)
if index < 18.5:
    print("Недостаточная масса тела")
elif index < 25:
    print("Нормальная масса тела")
else:
    print("Ожирение")
print(index)
