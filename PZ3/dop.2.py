#Вести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.
a = float(input('Введите число'))

b = a % 2

if b == 0:
    a = a * 4
elif b == 1:
    a = a * 5
print(a)