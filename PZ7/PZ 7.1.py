# Дано целое число N и символ C. Вывести строку длины N, которая состоит из
# символов C.
a = input('Введите число больше 0 ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Введено неверное значение ')
        a = input('Введите число больше 0')

print('c' * a)
