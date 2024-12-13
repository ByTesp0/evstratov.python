#Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном
#случае увеличить его в 1.5 раза.
a = float(input('Введите первое число'))
b = float(input('Введите второе число'))

proizv = a * b

if proizv < 0:
    proizv = proizv * 8
else:
    proizv = proizv * 1.5

print(proizv)
