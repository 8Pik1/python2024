# Задание 4: конвертер валют

rub_to_usd = 96.64   # курс доллара
rub_to_eur = 104.38  # курс евро

rub = int(input("Введите сумму в рублях: "))
vibor = int(input("Выберете команду (1 - в доллары, иное число - в евро): "))
if vibor == 1:
    doll = rub / rub_to_usd
    print(doll, "долларов")
else:
    evro = rub / rub_to_eur
    print(evro, "евро")

