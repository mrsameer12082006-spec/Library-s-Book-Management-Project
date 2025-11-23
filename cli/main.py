'''NAME - SAMEER MISHRA
   DATE - 24-11-2025
   TITLE - A LIBRARY MANAGEMENT SYSTEM 
'''
# ----------------------------------------------------

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import logging
from library_manager.inventory import LibraryInventory
from library_manager.book import Book




# -------------------- TASK 4: MENU-DRIVEN CLI --------------------
def menu():
    inventory = LibraryInventory()

    while True:
        print("\n========== Library Menu ==========")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")
        print("==================================")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Enter numbers only.\n")
            continue

        # -------------------- ADD BOOK --------------------
        if choice == 1:
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")

            book = Book(title, author, isbn)
            inventory.add_book(book)
            inventory.save_books()

        # -------------------- ISSUE BOOK --------------------
        elif choice == 2:
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)

            if book:
                if book.issue():
                    print("Book issued successfully.")
                    logging.info(f"Issued: {book.title}")
                else:
                    print("Book already issued.")
            else:
                print("Book not found.")

            inventory.save_books()

        # -------------------- RETURN BOOK --------------------
        elif choice == 3:
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)

            if book:
                if book.return_book():
                    print("Book returned successfully.")
                    logging.info(f"Returned: {book.title}")
                else:
                    print("Book was not issued.")
            else:
                print("Book not found.")

            inventory.save_books()

        # -------------------- VIEW ALL --------------------
        elif choice == 4:
            print("\n--- All Books ---")
            inventory.display_all()

        # -------------------- SEARCH BOOK --------------------
        elif choice == 5:
            keyword = input("Enter title or ISBN: ")

            book = inventory.search_by_isbn(keyword)
            if book:
                print("\nBook Found:")
                print(book)
                continue

            results = inventory.search_by_title(keyword)
            if results:
                print("\nSearch Results:")
                for b in results:
                    print(b)
            else:
                print("No books found.")

        # -------------------- EXIT --------------------
        elif choice == 6:
            print("Saving and exiting... Goodbye!")
            inventory.save_books()
            break

        else:
            print("Invalid choice. Try again.")


# -------------------- RUN THE PROGRAM --------------------
if __name__ == "__main__":
    menu()

