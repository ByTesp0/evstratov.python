# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Сумма элементов больших 10 во второй половине:

lst = ['100 14 -20 33 11 82']

f1 = open('digits1.txt', 'w')
f1.writelines(lst)
f1.close()

f2 = open('digits2.txt', 'w')
f2.write('Исходные данные: ')
f2.writelines(lst)
f2.write('\n')
f2.write('Количество элементов: ')
f2.close()

f1 = open('digits1.txt')
a = f1.read()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])
f1.close()
f2 = open('digits2.txt', 'a')
f2.write(str(len(a)))
f2.write('\n')
f2.write('Индекс последнего минимального элемента: ')
f2.close()

min_val = min(a)
min_ind = a.index(min_val)
f2 = open('digits2.txt', 'a')
f2.write(str(min_ind))
f2.close()

f1 = open('digits1.txt')

