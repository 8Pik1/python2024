# Задание 4: время загрузки файла

i = int(input("Введите размер файла в мегабайтах: "))
s = int(input("Введите скорость интернета в мегабитах в секунду: "))
t = i   * 8
o = t / s

q = int(input("Выберете что показать (1 - минуты, 2 - секунды): "))
if q == 2:
    print("Время загрузки:", o, "секунд")
elif q == 1:
    print("Время загрузки:", o / 60, "минут")
else:
    print("Введена неверная команда")

# IEEE 1541/IEC 60027-2
# 1 байт = 8 бит
# 1 Кбайт = 1000 байт
# 1 Мбайт = 1000 Кбайт
# 1 Гбайт = 1000 Мбайт