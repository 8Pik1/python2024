# Задание 6: Расчет оценки

ob = int(input("Введите общее количество вопросов: "))
ot = int(input("Введите количество правильных ответов: "))
prosent = ot / ob * 100

if prosent < 50:
    print("Неудовлетворительно")
elif prosent <= 70:
    print("Удовлетворительно")
elif prosent <= 85:
    print("Хорошо")
else:
    print("Отлично")

print(prosent)
