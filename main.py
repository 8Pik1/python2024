'''
print("Введите число:")
n = int(input())
r = 0                   # в начале ответ пустой
while n > 0:            # пока в числе есть цифры:
    ostatok = n%10      # берем последную цифру
    r = r*10 + ostatok  # дописываем ее в конец ответа
    n = n // 10         # убераем последнюю цифру в числе
print(r)

print(input()[::-1])


print("Ввидите число:")
f = int(input())
w = f // 1
if w > 0:
    w=1
e = f // 10
if e > 0:
    e=1
else:
    e=0
r = f// 100
if r > 0:
    r=1
else:
    r=0

print(w+e+r)



print("Введите пароль:")
regPass = (input())
print("Введите логин:")
regLogin = (input())

 if len(regLogin) >= 5 and len(regPass) >= 8:
     print("Успешная регистрация!")
else:
    pass


from tkinter import Label


from tkinter import *
tk = Tk()

canvas = Canvas(tk, width=500, height=500)
canvas.pack()
'''









































