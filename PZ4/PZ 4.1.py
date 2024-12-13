A = (input('Введите первое число: '))
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print('Введено неверное значение ')
        print('Введите первое число ')

B = (input('Введите второе число: '))
while type(B) != int:
    try:
        A = int(B)
    except ValueError:
        print('Введено неверное значение ')
        print('Введите второе число ')

a = A
result = 0
while a <= B:
    result += a ** 2
    a += 1
print(result)
