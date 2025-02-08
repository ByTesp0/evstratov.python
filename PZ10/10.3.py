# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
# мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. в каких магазинах нельзя приобрести сыр.
# 2. в каких магазинах можно приобрести одновременно молоко и сахар.
# 3. в каких магазинах можно приобрести соль

magnit = {'молоко', 'соль', 'сахар'}
pyat = {'мясо', 'молоко', 'сыр'}
krest = {'молоко', 'творог', 'сыр', 'сахар'}
s = {'соль'}

naz = ['магнит', 'пятёрочка', 'перекрёсток']
lst = []


def sir(a, i):
    b = a & s
    if b == s:
        lst.append(naz[i])


sir(magnit, 0)
sir(pyat, 1)
sir(krest, 2)

print(lst)