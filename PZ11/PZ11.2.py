# Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно удалив букву «с» из
# текста.

f1 = open('text18-8.txt', encoding='utf-16')
for i in f1:
    print(i, end='')
f1.close()

lst = ('а', 'б', 'в', 'г')
schet = 0
for i in open('text18-8.txt', encoding='utf-16'):
    for n in i:
        if n == lst[0] or n == lst[1] or n == lst[2] or n == lst[3]:
            schet += 1
print('\n', schet)

f1 = open('text18-8.txt', 'r', encoding='utf-16')
text = f1.read()
new_text = text.replace('с', '_')
f1.close()
f2 = open('except.txt', 'w', encoding='utf-16')
f2.write(new_text)
f2.close()
