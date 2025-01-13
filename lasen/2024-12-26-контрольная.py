n = int(input("Введите N: "))

num = []
i = 0
while i < n:
    a = int(input())
    num.append(a)
    i += 1
print(num)

i = n - 1
while i >= 0:
    a = num[i]
    if not ( a % 3 == 0 and a % 7 != 0 ):
        num.pop(i)
    i -= 1
print(num)

