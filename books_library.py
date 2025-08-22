class Book:
    def __init__(self, title, author, is_available = True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        availability = "Available" if self.is_available == True else "Unavailable"
        return f"Book: {self.title} by {self.author} ({availability})."

class Member():
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:                
            book.is_available = False         
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is already borrowed.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"You haven't borrowed {book.title}")

class Library:
    def __init__(self):
        self.list_of_books = []

    def add_book(self, book):
        self.list_of_books.append(book)
        print(f"{book.title} by {book.author} added to Library")
    
    def list_books(self):
        for book in self.list_of_books:
            print(book)


b = Book("rich dad poor dad", "robert kiyosaki")
l = Library()
l.add_book(b)
l.list_books()