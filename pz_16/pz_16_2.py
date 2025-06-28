# Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе.

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def display(self):
        print(f"Вид: {self.species}, Возраст: {self.age} лет")

class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__('Собака', age)
        self.breed = breed

    def display(self):
        print(f"Вид: {self.species}, Возраст: {self.age} лет, Порода: {self.breed}")


class Cat(Animal):
    def __init__(self, age, breed):
        super().__init__('Кошка', age)
        self.breed = breed

    def display(self):
        print(f"Вид: {self.species}, Возраст: {self.age} лет, Порода: {self.breed}")


dog = Dog(age=5, breed='Овчарка')
cat = Cat(age=3, breed='Сиамская')

dog.display()
cat.display()
