# В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов.

import re
#s = '<a href="#10">10: CamelCase -> under_score</a>;'
#p = re.compile(r"<a.*>(.*?)</a>", re.S)
#print(p.findall(s))

f1 = open('Dostoevsky.txt', encoding='UTF-8')
lst = f1.readlines()
st = "".join(lst)
f1.close()
p = re.compile(r"(«.+?»)", re.S)
print(p.findall(st), len(p.findall(st)))