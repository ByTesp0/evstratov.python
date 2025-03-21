# Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно удалив букву «с» из
# текста.

f1 = open('text18-8.txt', encoding='utf-16')
l = f1.readlines()
f1.close()
print(l)

lst = ('а', 'б', 'в', 'г')
schet = 0
for i in open('text18-8.txt', encoding='utf-16'):
    for n in i:
        if n == lst[0] or n == lst[1] or n == lst[2] or n == lst[3]:
            schet += 1
print(schet)

str = 'с'

f1 = open('text18-8.txt', encoding='utf-16')
l = f1.readlines()
for i in l:
    if i == str:
        i.replace('с', '_')
        f2 = open('exceptc.txt', 'w')
        f2.writelines(i)
        f2.close()

