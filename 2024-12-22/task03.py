# Задание 3 - найдите максимальный элемент

numbers = []
for _ in range(5):
    a = int(input("Введите число: "))
    numbers.append(a)

print(f"original: {numbers}")

max1 = numbers[0]
for i in range(1,len(numbers)):
    if numbers[i] > max1:
        max1 = numbers[i]
print(max1)
