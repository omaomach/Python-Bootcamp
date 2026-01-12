class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.title.__len__()

book = Book("The Holy Bible", "God")
print(book)

book2 = Book("Vanity", "Life")
print(book2)
print(len(book))