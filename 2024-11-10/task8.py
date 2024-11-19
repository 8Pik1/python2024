# Обратный порядок цифр

print("Введите число:")
n = int(input())
i = n
r = 0
while i > 0:
    ostatok = i % 10
    r = r * 10 + ostatok
    i = i // 10
print("x =",n,"=> x =",r)
