# Создание базового класса "Животное" и его наследование для создания классов
# "Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
# и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
# такие как "гавкать" и "мурлыкать".

class animal(object):
    def breath(self):
        print("Я умею дышать")
    def eat(self):
        print("Я умею питаться")


class dog(animal):
    def gav(self):
        print("гавкать")


class cat(animal):
    def meow(self):
        print("мурлыкать")


Milka = dog()
Milka.breath()
Milka.gav()

Barsik = cat()
Barsik.eat()
Barsik.meow()