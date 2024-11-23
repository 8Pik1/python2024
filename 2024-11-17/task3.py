# Задание 3: Банк

balans = 1000
i = input("Вашь баланс 1000 (что бы снять введите 'снять'): ")
while balans > 0:
    if i == "снять":
        s = int(input("Напишите сколько вы хотите снять: "))
        balans = balans - s
        print("Ваш баланс: ",balans)
