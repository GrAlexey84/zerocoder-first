class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} ест")


class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f"{self.name} чирикает")


class Mammal(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f"{self.name} рычит")


class Reptile(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f"{self.name} шипит")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo():
    def __init__(self):
        self.workers = []
        self.animals = []

    def add_workers(self, worker):
        self.workers.append(worker)
        print(f"Сотрудник {worker.name} добавлен в зоопарк")

    def add_animals(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")



class ZooKeeper():
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"Сотрудник {self.name} кормит {animal.name}")


class Veterinarian():
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"Сотрудник {self.name} лечит {animal.name}")



bird_1 = Bird("Попугай Гоша", 5, "Белый")
mammal_1 = Mammal("Собака Бим", 7, "Чёрный")
reptile_1 = Reptile("Ящерица Жанна", 3, "Зелёная")

zoo = Zoo()
worker_1 = ZooKeeper("Иван")
worker_2 = Veterinarian("Анна")

zoo.add_workers(worker_1)
zoo.add_workers(worker_2)

zoo.add_animals(bird_1)
zoo.add_animals(mammal_1)
zoo.add_animals(reptile_1)

animal_sound(zoo.animals)

worker_1.feed_animal(mammal_1)
worker_2.heal_animal(reptile_1)

