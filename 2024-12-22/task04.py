# Задача 4 - удаление дубликатов

numbers = []
for _ in range(5):
    a = int(input("Введите число: "))
    numbers.append(a)

print(f"original: {numbers}")

numbers_uniq = []
for i in numbers:
    found = False
    for j in numbers_uniq:
        if i == j:
            found = True
            break
    if not found:
        numbers_uniq.append(i)

print(f"uniq: {numbers_uniq}")

