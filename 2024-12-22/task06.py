import random

numbers1 = random.sample(range(20),10)
print(numbers1)

numbers2 = []
for i in numbers1:
    numbers2.insert(0,i)
print(numbers2)
