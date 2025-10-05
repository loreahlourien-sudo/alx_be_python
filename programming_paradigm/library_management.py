class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def _init_(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Adds a Book object to the library."""
        self._books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def check_out_book(self, title):
        """Checks out a book by its title, marking it as unavailable."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                print(f"Book '{title}' checked out successfully.")
                return
        print(f"Book '{title}' not found or already checked out.")

    def return_book(self, title):
        """Returns a book by its title, marking it as available."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                print(f"Book '{title}' returned successfully.")
                return
        print(f"Book '{title}' not found or not currently checked out.")

    def list_available_books(self):
        """Lists all books currently available in the library."""
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"- '{book.title}' by {book.author}")
        else:
            print("No books currently available in the library.")