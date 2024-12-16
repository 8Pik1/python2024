# Задание 2 - сумма чисел в списке

numbers = []
for _ in range(5):
    a = int(input("Введите число: "))
    numbers.append(a)

print(f"original: {numbers}")
sum = 0
for i in numbers:
    sum += i
print(sum)

