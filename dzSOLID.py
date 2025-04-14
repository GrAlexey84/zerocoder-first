from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")


class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука")


class MagicalWand(Weapon):
    def attack(self):
        print("Боец наносит выстрел волшебным посохом")


class Fighter:
    def __init__(self,title, weapon):
        self.title = title
        self.weapon = weapon


    def change_weapon(self):
        print(f"Боец выбирает {self.title}")

    def fight(self):
        self.weapon.attack(self)
        print("Монстр побеждён!")


class Monstr:
    pass


weapon_1 = Fighter("меч", Sword)
weapon_2 = Fighter("лук", Bow)
weapon_3 = Fighter("волшебный посох", MagicalWand)

weapon_1.change_weapon()
weapon_1.fight()

weapon_2.change_weapon()
weapon_2.fight()

weapon_3.change_weapon()
weapon_3.fight()