n = int(input("Введите N: "))

num = []
i = 0
while i < n:
    a = int(input())
    num.append(a)
    i += 1
print(num)

res = []
i = 0
while i < n:
    a = num[i]
    if a % 3 == 0 and a % 7 != 0:
        res.append(a)
    i += 1
print(res)
