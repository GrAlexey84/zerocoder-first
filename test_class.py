class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лёг спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} кого-то бьёт")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"Имя воина - {self.name}")
        print(f"Цвет волос - {self.hair_color}")
        print(f"Сила воина - {self.power}")
        print(f"Выносливость воина - {self.endurance}")

war_1 = Warrior("Степан", 76, 54, "Коричневый")
war_2 = Warrior("Егор", 50, 23, "Блонд")
print(war_1.info())