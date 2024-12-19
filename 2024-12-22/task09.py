# Задание 9: Поиск минимального и максимального устройства

import random

numbers = random.sample(range(20),10)
print(numbers)

max1 = numbers[0]
min1 = numbers[0]

for i in range(1,len(numbers)):
    if numbers[i] > max1:
        max1 = numbers[i]
    if numbers[i] < min1:
        min1 = numbers[i]
print(min1,max1)
