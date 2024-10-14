
'''
print("Введите число:")
n = int(input())
r = 0
while n > 0:
    ostatok = n%10
    r = r*10 + ostatok
    n = n // 10
print(r)



print("Ведите число:")
i = input()
g = int(i)
t = 0
sum = 0
while g > 0:
    h = g % 10
    g = g // 10
    t = t + 1

    sum = h * h * h + sum

print(t)
print(sum)
'''



f = int(input("Введите размер файла в мегабайтах : "))
i = int(input("Введите скорость интернета в мегабайтах в секунду: "))
m = f // i
s = f % 60
print("Время скачивания =",m,"минут",s,"секунд")










'''

'''