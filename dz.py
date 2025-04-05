class User:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._access = "user"

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access(self):
        return self._access

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._access = "admin"
        self._list_user = []


    def add_user(self, name):
        self._list_user.append(name)
        print(f"Новый сотрудник {name.get_name()} добавлен")

    def remove_user(self, name):
        self._list_user.remove(name)
        print(f"Сотрудник {name.get_name()} удалён")

    def list_user(self):
        for i in self._list_user:
            print(f"id - {i.get_id()}, Имя - {i.get_name()}, Доступ - {i.get_access()}")



ad_1 = Admin("01", "Сергей")
us_1 = User("002", "Андрей")
us_2 = User("003", "Елена")

ad_1.add_user(us_1)
ad_1.add_user(us_2)

ad_1.list_user()

ad_1.remove_user(us_1)

ad_1.list_user()


