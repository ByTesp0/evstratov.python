a = float(input('Введите первое число'))
b = float(input('Введите второе число'))

c = a + b

d = c % 5

if d == 0:
    c = c + 1
elif d == 1:
    c = c - 2
print(c)

