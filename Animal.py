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

import json


def save_zoo(zoo, filename='zoo_save.json'):
    """Сохраняет зоопарк в файл"""
    data = {
        'animals': [
            {
                'type': animal.__class__.__name__,
                'name': animal.name,
                'age': animal.age,
                'color': animal.color if hasattr(animal, 'color') else None
            } for animal in zoo.animals
        ],
        'workers': [
            {
                'type': worker.__class__.__name__,
                'name': worker.name
            } for worker in zoo.workers
        ]
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Зоопарк сохранён в {filename}")


def load_zoo(filename='zoo_save.json'):
    """Загружает зоопарк из файла"""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

        zoo = Zoo()

        # Загружаем животных
        animal_classes = {'Bird': Bird, 'Mammal': Mammal, 'Reptile': Reptile}
        for animal_data in data['animals']:
            animal_class = animal_classes.get(animal_data['type'])
            if animal_class:
                animal = animal_class(animal_data['name'], animal_data['age'], animal_data['color'])
                zoo.add_animals(animal)

        # Загружаем сотрудников
        worker_classes = {'ZooKeeper': ZooKeeper, 'Veterinarian': Veterinarian}
        for worker_data in data['workers']:
            worker_class = worker_classes.get(worker_data['type'])
            if worker_class:
                worker = worker_class(worker_data['name'])
                zoo.add_workers(worker)

        print(f"Зоопарк загружен из {filename}")
        return zoo

    except FileNotFoundError:
        print("Файл сохранения не найден. Создан новый зоопарк.")
        return Zoo()
    except Exception as e:
        print(f"Ошибка при загрузке: {e}. Создан новый зоопарк.")
        return Zoo()


# Пример использования:
print("\nСохранение текущего зоопарка...")
save_zoo(zoo)

print("\nЗагрузка зоопарка...")
loaded_zoo = load_zoo()

print("\nПроверка загруженного зоопарка:")
animal_sound(loaded_zoo.animals)
for worker in loaded_zoo.workers:
    if isinstance(worker, ZooKeeper) and loaded_zoo.animals:
        worker.feed_animal(loaded_zoo.animals[0])
    elif isinstance(worker, Veterinarian) and loaded_zoo.animals:
        worker.heal_animal(loaded_zoo.animals[-1])