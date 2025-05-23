# Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.

str = 'asdadasdasdsadsads'


def upper(a):
    b = a.split()
    yield from [i.upper() for i in b]


a = upper(str)

for i in a:
    print(i)
