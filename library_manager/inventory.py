import logging
import os
from library_manager.book import Book



# -------------------- LOGGING SETUP --------------------
logging.basicConfig(
    filename="library_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -------------------- TASK 2: INVENTORY MANAGER --------------------
class LibraryInventory:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        logging.info(f"Book added: {book.title}")
        print("Book added successfully.\n")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        if not self.books:
            print("No books available.\n")
            return
        for b in self.books:
            print(b)

    # -------------------- TASK 3: TEXT FILE PERSISTENCE --------------------
    def save_books(self):
        try:
            with open(self.filename, "w") as f:
                for b in self.books:
                    f.write(b.to_line() + "\n")

            logging.info("Books saved to text file.")
        except Exception as e:
            logging.error(f"Error saving books: {str(e)}")

    def load_books(self):
        try:
            if not os.path.exists(self.filename):
                return

            with open(self.filename, "r") as f:
                for line in f:
                    book = Book.from_line(line)
                    if book:
                        self.books.append(book)

            logging.info("Books loaded from text file.")
        except Exception as e:
            logging.error(f"Error loading file: {str(e)}")
            print("Warning: Could not load book data. File may be corrupted.\n")