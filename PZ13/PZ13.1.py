# В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два
# раза.

import random

lst = [[random.randint(0, 10) for i in range(3)] for i in range(3)]

print("Исходная матрица: ")
for i in lst:
    print(i)

n = int(input('Введите номер столбца: '))

print(list(map(lambda x: x[n - 1] * 2, lst)))

