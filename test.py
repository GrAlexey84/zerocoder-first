class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info_book(self):
        print(f"Книга {self.title}, автор - {self.author.}")

author = Author("Лев Толстой", "Русский")
book = Book("Война и мир", author)