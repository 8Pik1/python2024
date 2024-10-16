# Обратный порядок цифр

print("Введите число:")
n = int(input())
r = 0
while n > 0:
    ostatok = n % 10
    r = r * 10 + ostatok
    n = n // 10
print(r)
