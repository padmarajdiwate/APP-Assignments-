class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.issued_books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "has been added.")

    def register_member(self, member):
        self.members.append(member)
        print(member, "has been registered.")

    def borrow_book(self, member, book):
        if member in self.members and book in self.books:
            self.books.remove(book)
            self.issued_books.append([member, book])
            print(member, "borrowed", book)
        else:
            print("Book or member not available.")

    def return_book(self, member, book):
        if [member, book] in self.issued_books:
            self.issued_books.remove([member, book])
            self.books.append(book)
            print(member, "returned", book)
        else:
            print("Borrowing record not found.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books are currently available.")
        else:
            print("\nBooks Available:")
            for book in self.books:
                print(book)


def library_demo():
    library = Library()

    library.add_book("Python Programming")
    library.add_book("Java Basics")
    library.add_book("C Programming")

    library.register_member("Padmaraj")
    library.register_member("Machhi")

    library.display_books()

    library.borrow_book("Padmaraj", "Python Programming")
    library.borrow_book("Machhi", "Python Programming")

    library.display_books()

    library.return_book("Padmaraj", "Python Programming")
    library.display_books()


library_demo()
