attack = [
    "Атаковать мечем (0)",
    "Атаковать магией (1)",
]
descriptions = [
    "Нанесли урон мечем",
    "Нанесли урон магией",
]

hp1 = 100
attack1 = 0
hp2 = 150
attack2 = 20

print("Идя по тропинке вы видите дракона:")
print("Он атакует вас первым")
game_over = False
while not game_over:
    print("---------------------------------------------")
    print("Ваше здоровье:",hp1 - attack2)
    print("Здоровье дракона:", hp2)
    attack = input("Как будем атакавать? - (0 - 1): ")

    if attack == 0:
        print(descriptions[0])
        if hp1 < 50:
            print(descriptions[0])
    if attack == 1 and hp1 > 30:
        print(descriptions[1])
        if hp1 < 30:
            print(descriptions[1])

        if attack == 0:
            hp1 = hp1 - attack2
            hp2 = hp2 - 15
            print(descriptions[1])
            if hp1 < 50:
                hp1 = hp1 - attack2
                hp2 = hp2 - 10
                print(descriptions[1])
        if attack == 1 and hp1 > 30:
            hp1 = hp1 - attack2
            hp2 = hp2 - 20
            print(descriptions[1])
            if hp1 < 30:
                hp1 = hp1 - attack2
                hp2 = hp2 - 10
                print(descriptions[1])
        if hp1 == 0:
            game_over = True
        if hp2 == 0:
            game_over = True
