# Найти длину отрезка в метрах.

user_num = input('Введите число от 1 до 5: ')

while type(user_num) != int:
    try:
        user_num = int(user_num)
    except ValueError:
        print('Введено неверное значение: ')

user_measure = input('Введите длину отрезка: ')

while type(user_measure) != float:
    try:
        user_measure = float(user_measure)
    except ValueError:
        print('Введено неверное значение: ')

if user_num == 1:
    user_measure = user_measure / 10
elif user_num == 2:
    user_measure = user_measure * 1000
elif user_num == 3:
    print(user_measure)
elif user_num == 4:
    user_measure = user_measure / 1000
elif user_num == 5:
    user_measure = user_measure / 100
else:
    print('Введено неверное число')
print(user_measure)
