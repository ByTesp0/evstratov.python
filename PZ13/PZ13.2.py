# В двумерном списке элементы последней строки заменить на 0.import random

import random

lst = [[random.randint(0, 10) for i in range(3)] for i in range(3)]

print("Исходная матрица: ")
for i in lst:
    print(i)

# map(lambda x: x * 0, lst[2])
a = [i * 0 for i in lst[2]]

new_lst = [lst[0], lst[1], a]

print("Изменённая матрица: ")
for i in new_lst:
    print(i)