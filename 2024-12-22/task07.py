import random

numbers1 = random.sample(range(20),10)
print(numbers1)

numbers2 = []
while len(numbers1) > 0:
    i_min = 0
    for i in range(1,len(numbers1)):
        if numbers1[i] < numbers1[i_min]:
            i_min = i
    numbers2.append(numbers1[i_min])
    numbers1.pop(i_min)
print(numbers2)
