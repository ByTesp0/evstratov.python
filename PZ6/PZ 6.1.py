# Дан целочисленный список размера 10. Вывести все содержащиеся в данном списе
# четные числа в порядке убывания их индексов, а также их количество K.

import random

user_list = []
chet = []

i = 0
while i <= 10:
    user_list.append(random.randint(0, 100))
    i += 1
print(user_list)

user_list.reverse()
for schet in user_list:
    if schet % 2 == 0:
        chet.append(schet)

print(chet)

kolvo = len(chet)
print(kolvo)
