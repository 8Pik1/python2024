# Задание 8: Слияние двух отсартированных списков

import random

numbers1 = random.sample(range(20),10)
numbers1.sort()
print(numbers1)
numbers2 = random.sample(range(20),10)
numbers2.sort()
print(numbers2)

e1 = 0
e2 = 0
numbers3 = []

while len(numbers3) < len(numbers1) + len(numbers2):
    if e1 == len(numbers1):
        numbers3.append(numbers2[e2])
        e2 += 1
    elif e2 == len(numbers2) or numbers1[e1] < numbers2[e2]:
        numbers3.append(numbers1[e1])
        e1 += 1
    else:
        numbers3.append(numbers2[e2])
        e2 += 1
print(numbers3)

