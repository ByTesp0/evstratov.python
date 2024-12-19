# Дан список размера N. Возвести в квадрат все его локальные минимумы (то есть
# числа, меньшие своих соседей).

import random

N = input('введите длинну списка: ')

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('введено неверное значение')
        N = input('введите длинну списка: ')

user_list = []
changed_user_list = []

x = 0
while x <= N:
    user_list.append(random.randint(0, 100))
    x += 1
print(user_list)

for i in range(N):
    if i > 0:
        left = user_list[i - 1]
    else:
        left = 0
    if i < N - 1:
        right = user_list[i + 1]
    else:
        right = 0
    if i == 0 or i == N - 1:
        m = 2
    else:
        m = 3

    sred_znach = (left + right + user_list[i]) / m
    changed_user_list.append(sred_znach)

print(changed_user_list)
