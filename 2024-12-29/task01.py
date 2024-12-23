# Задача 1: разбиения списка на группы

import random

max_sum = 10
numbers = random.sample(range(max_sum),10)
print(numbers)

i = 0
sum = 0
result = []
group = []
while i < len(numbers):
    if sum + numbers[i] > max_sum:
        sum = 0
        result.append(group)
        group = []
    sum += numbers[i]
    group.append(numbers[i])
    i += 1
result.append(group)
print(result)
