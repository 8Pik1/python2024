# Задача 2: Генерация списка сочетаний

import random

num_count = 5
max_num = 10
numbers = random.sample(range(max_num),num_count)
print(numbers)
k = 3
result = []
group = []
for i in range(0,len(numbers)):
    for j in range(i + 1,len(numbers)):
        for k in range(j + 1, len(numbers)):
            result.append((numbers[i],numbers[j],numbers[k]))
print(result)
