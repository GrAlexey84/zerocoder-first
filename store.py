class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    #Добавить товар:
    def adding_product (self, product_name, price):
        self.items[product_name] = price
        print(f"Товар {product_name} в ассортимент магазина {self.name} добавлен!")

    #Удалить товар:
    def delete_product (self, product_name):
        self.items.pop(product_name)
        print(f"Товар {product_name} из ассортимента магазина {self.name} удалён!")

    #Узнать цену товара:
    def price(self, product_name):
        if product_name in self.items:
            print(f"Продукт {product_name} стоит: {self.items[product_name]} руб")
        else:
            print(f"Продукт {product_name} отсутствует в магазине {self.name}:")


    #Изменить цену товара:
    def update_prise(self, product_name, price):
        self.items.update({product_name: price})
        print(f"Цена на товар {product_name} изменилась и стала равняться = {price} руб ")

#Примеры:
shop_1 = Store ("Атлас", "Центральная, 240")
shop_2 = Store ("Незабудка", "Центральная, 215")
shop_3 = Store ("Каприз", "Попова, 17")

shop_1.adding_product("Огурец", 180)
shop_1.adding_product("Банан", 150)
shop_1.adding_product("Яблоко", 120)

shop_2.adding_product("Зефир", 240)
shop_2.adding_product("Торт`Наполеон`", 1200)
shop_2.adding_product("Тульский пряник", 140)

shop_3.adding_product("Зубная паста`SPLAT`", 130)
shop_3.adding_product("Мыло`DOVE`", 160)
shop_3.adding_product("Туалетная бумага`ZEVA`", 450)

shop_1.adding_product("Лимон", 90)

shop_1.delete_product("Банан")

shop_1.price("Огурец")
shop_1.price("Банан")
shop_1.price("Яблоко")
shop_1.price("Лимон")

shop_1.update_prise("Огурец", 150)

shop_1.price("Огурец")
