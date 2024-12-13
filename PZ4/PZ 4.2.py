s = 1000

p = input('Введите желаемый процент: ')
while type(p) != float:
    try:
        p = float(p)
    except ValueError:
        print('Введено неверное значение ')
        p = input('Введите желаемый процент: ')

while p >= 25 or p <= 0:
    print('Введено неверное значение ')
    p = input('Введите желаемый процент: ')
    while type(p) != float:
        try:
            p = float(p)
        except ValueError:
            print('Введено неверное значение ')
            p = input('Введите желаемый процент: ')

k = 0
while s <= 1100:
    s += s * (p / 100)
    k += 1
print(f'конечная сумма', s)
print(f'колличество месяцев ', k)
