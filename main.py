class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly (self):
        print(f"{self.name} летает")

    def eat (self):
        print(f"{self.name} кушает")

    def sing (self):
        print(f"{self.name} поёт - чирик")

    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - окрас")

class Pigeon(Bird):
    def __init__(self, name, voice, color, favorit_food):
        super().__init__(name, voice, color)
        self.favorit_food = favorit_food

    def walk(self):
        print(f"{self.name} гуляет")

    def sing (self):
        print(f"{self.name} поёт - курлык")

bird_1 = Pigeon("Гоша", "курлык", "серый", "хлебные крошки")
bird_2 = Bird("Маша", "чирик", "коричневый")

bird_1.fly()
bird_1.sing()
bird_1.info()

bird_1.walk()