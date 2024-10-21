# Задание 5: количество часов и приветсвие

i = int(input("Введите количество часов: "))
i = i % 24
if i < 6:
    print("Good night")
elif i < 13:
    print("Good morning")
elif i < 17:
    print("Good day")
elif i < 24:
    print("Good evening")
