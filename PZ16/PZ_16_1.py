# Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
# который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
# Пол: пол".


class human:
    def __init__(self, name, age, pol):
        self.name = name
        self.age = age
        self.pol = pol
    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age},Пол: {self.pol}")


student = human("Владимир", 17, "М")
student.info()