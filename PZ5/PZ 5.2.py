# Описать функцию AddLeftDigit(D, K), добавляющую к целому положительному
# числу K слева цифру D (D — входной параметр целого типа, лежащий в диапазоне
# 1-9, K — параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции последовательно добавить к данному числу K слева
# данные цифры D1 и D2, выводя результат каждого добавления.

import random

k = input('Введите число: ')

while type(k) != int:
    try:
        k = int(k)
    except ValueError:
        print('Введено неверное значение')
        k = input('Введите число: ')


def ald(b):
    a = random.randint(1, 9)
    kolvo0 = 0
    schet = b
    while schet != 0:
        schet = schet // 10
        kolvo0 += 1
    mnozh = '1' + kolvo0 * '0'
    while type(mnozh) != int:
        mnozh = int(mnozh)
    a = a * mnozh
    b = a + b
    print(b)

    return b


k = ald(k)
ald(k)
