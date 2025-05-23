# В последовательности на n целых элементов найти количество пар, для которых
# произведение элементов делится на 3 (элементы пары в последовательности являются
# соседними).
import random

kolvo = int(input('количество симвлов: '))
prob = [random.randint(1,10) for i in range(0, kolvo)]
print(prob)

lst = [prob[i] * prob[i + 1] for i in range(len(prob) - 1)]
print(len(list(filter(lambda x: x % 3 == 0, lst))))
