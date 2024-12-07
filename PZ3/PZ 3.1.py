# Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел
# A и B нечетное».
a = input('Введите первое целое число ')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Введено неверное значение ')
        print('Введите первое целое число ')

b = input('Введите второе целое число ')
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Введено неверное значение ')
        print('Введите второе целое число ')

print(a % 2 != 0 and b % 2 != 0)
