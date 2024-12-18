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

for i in range(1, N):
    if user_list[i] > user_list[i - 1]:
        flag = True
    else:
        schet += 1
        flag = False

print(schet)
