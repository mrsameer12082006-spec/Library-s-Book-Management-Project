# -------------------- TASK 1: BOOK CLASS --------------------
class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"

    def to_line(self):
        """Convert book to a single text line for saving."""
        return f"{self.title}|{self.author}|{self.isbn}|{self.status}"

    @staticmethod
    def from_line(line):
        """Convert text line back into a Book object."""
        parts = line.strip().split("|")
        if len(parts) == 4:
            return Book(parts[0], parts[1], parts[2], parts[3])
        return None

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"
