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
    if num[i] % 3 == 0 and num[i] % 7 != 0:
        res.append(num[i])
    i += 1
print(res)
