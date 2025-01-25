# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти среднее значение продаж по
# каждому виду продукции, результаты вывести на экран.

a = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
lst_a = a.split()

print(lst_a)

orgs = dict.fromkeys([lst_a[0]], lst_a[1:6])
apls = dict.fromkeys([lst_a[6]], lst_a[7:])

c = lst_a[0]
d = lst_a[6]
def funkc(a, b):
    nums = a.get(b)
    lst = []
    for i in range(len(nums)):
        lst.append(int(nums[i]))
        print(lst)
    b = 0
    for i in lst:
        b = (b + i)
    b = b/len(lst)
    print('среднее значение продукции за 5 дней:', b)

funkc(orgs, c)
funkc(apls, d)
