a = float(input('Введите число: '))

while a < 10:
    print('Введено неверное число: ')
    a = float(input('Введите число: '))

b, c = divmod(a, 10)

if (b + c) % 2 == 0:
    a = a + 2
elif (b + c) % 2 == 1:
    a = a - 2

print(a)
