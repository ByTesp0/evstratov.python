# Дан размер файла в байтах. Используя операцию деления нацело,
# найти количество полных килобайтов, которые занимает данный файл (1 килобайт = 1024 байта)

from tkinter import *

def find_kb(x):
    try:
        n = int(num.get())
    except ValueError:
        result['text'] = ('Ошибка!')
        return
    check_num = n // 1024
    result['text'] = f"{check_num} КБ"

root = Tk()
root.title('байты в килобайты')
root.geometry('350x200')

Label(text="количество байт").grid(row=1, column=0)
num = Entry()
num.grid(row=1, column=1)

button = Button(text="вычислить")
button.grid(row=1, column=3)

result = Label()
result.grid(row=2, column=1)

button.bind('<Button-1>',find_kb)

def close():
    root.destroy()
    root.quit()

root.mainloop()

