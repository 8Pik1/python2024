n = int(input("Введите N: "))

res = []
i = 0
while i < n:
    a = int(input())
    if a % 3 == 0 and a % 7 != 0:
        res.append(a)
    i += 1
print(res)
