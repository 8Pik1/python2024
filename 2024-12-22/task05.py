# Задание 5 - слияние списков

import random

numbers1 = random.sample(range(20),10)
print(numbers1)
numbers2 = random.sample(range(20),10)
print(numbers2)

numbers3 = []
for i in numbers1:
    numbers3.append(i)
for i in numbers2:
    numbers3.append(i)
print(numbers3)

