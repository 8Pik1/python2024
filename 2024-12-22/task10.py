# Задание 10: Перестановка элементов

import random

numbers1 = random.sample(range(20),10)
print(numbers1)


e = 0
while e < len(numbers1) // 2:
    tmp = numbers1[2 * e + 1]
    numbers1[2 * e + 1] = numbers1[2 * e]
    numbers1[2 * e] = tmp
    e += 1
print(numbers1)
