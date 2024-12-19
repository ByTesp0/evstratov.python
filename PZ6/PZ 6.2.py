# Дан список размера N. Найти минимальный из его локальных максимумов
# (локальный минимум — это элемент, который меньше любого из своих соседей).

import random

N = input('Введите количество элементов: ')

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введено неверное значение')
        N = input("Введите количество строк: ")

user_list = []

prov = 1
while prov <= N:
    user_list.append(random.randint(0, 100))
    prov += 1
print(user_list)

flag = False
schet = 0

for i in range(1, len(user_list)):
    if user_list[i] > user_list[i - 1]:
        if not flag:
            flag = True
    else:
        schet += 1
        flag = False

if flag:
    schet += 1

print(schet)
