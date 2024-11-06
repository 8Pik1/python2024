rooms = [
    "Главная комната (0)",
    "Зал (1)",
    "Кухня (2)",
    "Подземелье (3)"
]
descriptions = [
    "Тут нет ничего интересного",
    "Тут есть ключ, но его сторожит охранник",
    "Тут есть еда, которая востановит силы",
    "Тут есть дверь, но она заперта"
]
position = 0
has_food = False
has_key = False

game_over = False
while not game_over:
    print("---------------------------------------------")
    print("Игрок находится в: ", rooms[position])
    if position == 0:
        print(descriptions[0])
    elif position == 1:
        if has_key:
            print(descriptions[0])
        else:
            print(descriptions[1])
    elif position == 2:
        if has_food:
            print(descriptions[0])
        else:
            print(descriptions[2])
    elif position == 3:
        print(descriptions[3])
    print("  0-3 - переход в комнаты\n"
          "  e - действие")
    action = input("Что дальше? ")
    if action == "e":
        if position == 2:
            has_food = True
            print("> Вы взяли еду")
        elif position == 1:
            if has_food:
                has_key = True
                print("> Вы успешно взяли ключ")
            else:
                print("> Вам не хватит сил, что бы забрать ключ у охранника")
        elif position == 3:
            if has_key:
                game_over = True
                print("> Вы успешно вышли из замка")
            else:
                print("> Дверь не открывается")
        else:
            print("> Ничего не произошло")
    elif action == "0" or action == "1" or action == "2" or action == "3":
        position = int(action)
        print("> Переход в другую комнату")
