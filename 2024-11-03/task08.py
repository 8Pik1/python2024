# Задание 8: Калькулятор

a1 = float(input("Введите первое число: "))
operator = input("Выберите операцию: ")
a2 = float(input("Введите второе число: "))

if operator == "+":
    res = a1 + a2
elif operator == "-":
    res = a1 - a2
elif operator == "*":
    res = a1 * a2
elif operator == "/":
    if a2 == 0:
        print("Операция невозможна")
    else:
        res = a1 / a2
else:
    print("Неверная операция")

if "res" in globals():
    print(f"Ответ: {res:.2f}")
