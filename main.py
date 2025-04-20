import  random
import time

class Hero:
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        other.health -= damage
        print(f"\n {self.name} нанёс игроку {other.name} {damage} урона")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}"

class Game:
    def __init__(self, user_name, computer = "Компьютер"):
        self.player = Hero(user_name)
        self.computer = Hero(computer)

    def start(self):
        print("Бой начинается")
        print(f"{self.player} против {self.computer}")
        print("=" * 40)

        time.sleep(1)
        round_num = 1

        while self.player.is_alive() and self.computer.is_alive():
            print("-" * 40)
            print(f"Раунд {round_num}")

            # Ход игрока
            self.player.attack(self.computer)
            print(f"У {self.computer} сталось {self.computer.health} здоровья")

            if not self.computer.is_alive():
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(f"У {self.player} осталось {self.player.health} здоровья")

            round_num += 1
            time.sleep(1)

        if self.player.is_alive():
            print(f"{self.player} побеждает!")

        else:
            print(f"{self.computer} побеждает!")

        print("Бой закончен")


# Запуск игры
user_name = input("Введите имя игрока: ")
game = Game(user_name)
game.start()