# Количество цифр и сумма их кубов

print("Ведите число:")
i = input()
g = int(i)
t = 0
sum = 0
while g > 0:
    h = g % 10
    g = g // 10
    t = t + 1

    sum = h * h * h + sum

print("Количество цифр:", t)
print("Сумма их кубов:", sum)
