'''
q = int(input("Введите первый знак числа: "))
w = int(input("Введите второй знак числа: "))
e = int(input("Введите третий знак числа: "))
r = int(input("Введите четвертый знак числа: "))
t = int(input("Введите пятый знак числа: "))
s = 0
s = q + w + e + r + t
o = 0
if o < 1:
    o = q % 5
    if o < 1:
        o = w % 5
        if o < 1:
            o = e % 5
            if o < 1:
                o = r % 5
                if o < 1:
                    o = t % 5
                    print(s)
                    '''

'''
q = int(input("Введите первый знак числа: "))
w = int(input("Введите второй знак числа: "))
e = int(input("Введите третий знак числа: "))
r = int(input("Введите четвертый знак числа: "))
t = int(input("Введите пятый знак числа: "))

s = q + w + e + r + t
o = s % 5
if o <= 0:
    print(s)
'''










