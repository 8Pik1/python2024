# Задание 3: налог от дохода

i = int(input("Введите ваш доход: "))
if i < 10000:
    n1 =  i  * 5 / 100
    print("Вваш налог составляет:", n1)
elif i <= 50000:
    n2 = i  * 10 / 100
    print("Вваш налог составляет:", n2)
else:
    n3 = i * 15 / 100
    print("Вваш налог составляет:", n3)