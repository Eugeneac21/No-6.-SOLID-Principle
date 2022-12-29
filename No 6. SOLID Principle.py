class Books():
    def __init__(self):
        self.books = {}
        self.number = 0

    def add_book(self, book):
        self.number += 1
        self.books[self.number] = book

    def __str__(self):
        return str(self.books)

b = Books()
b.add_book("Buku Komik")
b.add_book("Buku Novel")
print(f"Buku yang sudah dibaca: {b}")