📚 Library Management System (Python CLI)

A simple menu-driven Library Management System built using Object-Oriented Programming, text-file storage, and logging.
The project is fully modular and packaged using a clean folder structure.

🚀 Features
✅ Book Class (OOP)

Title, Author, ISBN, Status

Issue / Return methods

Convert to/from text-file format

✅ Inventory Manager

Add books

Search by title or ISBN

Issue / Return

Display all

Stores all books in books.txt

Uses library_log.log for logging

✅ Persistence (Text File)

Books are stored as:

title|author|isbn|status


One book per line inside books.txt.

✅ Command Line Interface

Menu options include:

Add Book

Issue Book

Return Book

View All Books

Search Book

Exit

✅ Logging

Every operation (add, issue, return, errors) is logged in:

library_log.log

🎁 BONUS: Packaged Folder Structure

Clean, modular project layout:

Library_Manager/
│
├── library_manager/
│   ├── __init__.py
│   ├── book.py
│   ├── inventory.py
│
├── cli/
│   ├── main.py
│
├── books.txt
├── library_log.log
├── README.md
├── requirements.txt
└── .gitignore

📂 Folder Explanation
📁 library_manager/

Package containing:

book.py → Book class

inventory.py → Inventory manager + logging + file handling

__init__.py → Makes folder importable (from library_manager import ...)

📁 cli/

Entry-point for the menu-driven program

main.py

▶️ How to Run
🔹 Step 1: Open terminal inside project root:
cd Library_Manager

🔹 Step 2: Run the CLI program:
python cli/main.py

📷output
1.<img width="1920" height="1080" alt="Screenshot (48)" src="https://github.com/user-attachments/assets/9349a4d0-fcab-4b05-9b51-0ff06d11393f" />
2.<img width="1920" height="1080" alt="Screenshot (49)" src="https://github.com/user-attachments/assets/ca7cc9bf-8b40-4949-9bf8-55f7099afecd" />
3.<img width="1920" height="1080" alt="Screenshot (50)" src="https://github.com/user-attachments/assets/a9261d83-d304-41d6-94ba-6d34e214ffc9" />





📝 Author
Sameer Mishra
