# Задание 3: перевод из метров

metr = int(input("Введите количество метров: "))

vibor = int(input("Выберите команду во что переводить (1 - мили, 2 - ярды, 3 - дюймы): "))

mili = metr / 1609
duim = metr * 39.37
yard = metr * 1.094

if vibor == 1:
    print("Количество миль:", mili)
elif vibor == 2:
    print("Количество ярдов:", yard)
elif vibor == 3:
    print("Количество дюймов:", duim)
else:
    print("Неверно введенная команда")



