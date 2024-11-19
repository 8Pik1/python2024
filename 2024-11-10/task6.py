
i = int(input("Ведите число:"))
h = 0
sum = 0
while i > 0:
    h = i % 10
    i = i // 10
    sum = sum + h

print("Сумма цифр:", sum,h)
