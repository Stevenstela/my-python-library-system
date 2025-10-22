[README.md](https://github.com/user-attachments/files/23057276/README.md)
Read.md
# 📚 Mini Library Management System

A simple console-based library management system built in Python. This project allows librarians or users to manage books, members, and track borrowing/returning of books — all using core Python data structures.

## ✨ Features

- Add, update, delete, and search for books
- Register and remove library members
- Borrow and return books with validation
- Enforce rules:
  - Maximum of 3 books per member
  - Cannot delete books that are currently borrowed
  - Only predefined genres are allowed

## 🗂️ Data Structures Used

| Data       | Structure        | Reason |
|------------|------------------|--------|
| **Books**  | Dictionary       | Fast access using ISBN as key |
| **Members**| List of dictionaries | Flexible for adding/removing users |
| **Genres** | Tuple            | Fixed list of valid genres (immutable) |

## 🧩 Core Functions

- `add_book(isbn, title, author, genre, total_copies)`
- `add_member(member_id, name, email)`
- `search_books(query)` – by title or author
- `update_book(isbn, **updates)`
- `delete_book(isbn)`
- `delete_member(member_id)`
- `borrow_book(member_id, isbn)`
- `return_book(member_id, isbn)`

## ▶️ How to Run

1. Save the code in a file named `library_system.py`
2. Open your terminal or command prompt
3. Navigate to the project folder
4. Run the program:

```bash
python library_system.py
