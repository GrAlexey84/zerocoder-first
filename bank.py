class Accaunt():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Счёт успешно пополнен на {money}. На вашем счёте - {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Невозможно снять {money}. Недостаточно средств на счёте")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money}. На вашем счёте осталось - {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")

man = Accaunt(12345, 1000)
man.all_balance()
man.withdraw(700)
man.withdraw(500)
man.deposit(10000)
