attack = [
    "Атаковать мечем (0)",
    "Атаковать магией (1)",
]
descriptions = [
    "Нанесли урон мечем: ",
    "Нанесли урон магией: ",
]

hp1 = 100
hp2 = 110
damage = 10


print("Идя по тропинке вы видите дракона:")
print("Он атакует вас первым")
game_over = False
while not game_over:
    print("---------------------------------------------")
    print("Ваше здоровье:",hp1)
    print("Здоровье дракона:", hp2)

    action = int(input("Как будем атакавать? - (0 - 1): "))
    if action == 0:
        hp2 = hp2 - damage
        print(descriptions[0], damage)
        if hp1 >= 50:
            hp2 = hp2 - damage
            print(descriptions[0], damage)
    if action == 1:
        hp2 = hp2 - damage
        print(descriptions[1], damage)
        if hp1 >= 30 and hp1 < 50:
            hp2 = hp2 - damage
            print(descriptions[1], damage)

    if hp2 <= 0:
        game_over = True
        print("> Игра окончина, вы победили")
    else:
        hp1 = hp1 - damage
    if hp1 <= 0:
        game_over = True
        print("> Игра окончина, вы проиграли")
