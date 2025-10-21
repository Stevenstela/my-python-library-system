# demo.py - Demonstration of the Mini Library Management System

from library_system import (
    add_book, add_member, search_books,
    update_book, update_member,
    delete_book, delete_member,
    borrow_book, return_book,
    books, members
)

def print_books():
    print("\n📚 Current Books:")
    for isbn, info in books.items():
        print(f"  ISBN: {isbn} | Title: {info['title']} | Copies: {info['total_copies']}")

def print_members():
    print("\n👥 Current Members:")
    for m in members:
        borrowed = ', '.join(m['borrowed_books']) if m['borrowed_books'] else "None"
        print(f"  ID: {m['member_id']} | Name: {m['name']} | Borrowed: [{borrowed}]")

# Initialize genres (already defined in library_system)
print("✅ Starting Mini Library Management System Demo...\n")

# Add books
add_book("978-0-123456-78-9", "Dune", "Frank Herbert", "Sci-Fi", 3)
add_book("978-0-987654-32-1", "1984", "George Orwell", "Fiction", 2)
add_book("978-1-111111-11-1", "Sapiens", "Yuval Noah Harari", "Non-Fiction", 1)
# Add members
add_member("M001", "Alice", "alice@example.com")
add_member("M002", "Bob", "bob@example.com")

print_books()
print_members()

# Search books
print("\n🔍 Search for 'Dune':")
results = search_books("Dune")
for r in results:
    print(f"  Found: {r['title']} by {r['author']}")

# Borrow books
print("\n📥 Borrowing 'Dune' for Alice...")
borrow_book("M001", "978-0-123456-78-9")
borrow_book("M001", "978-0-987654-32-1")  # Second book

print_books()
print_members()

# Try to borrow third book (should work)
borrow_book("M001", "978-1-111111-11-1")

# Try to borrow fourth (should fail)
borrow_book("M001", "978-0-123456-78-9")  # Already borrowed, but also max limit
# Return a book
print("\n📤 Returning '1984'...")
return_book("M001", "978-0-987654-32-1")

print_books()
print_members()

# Update a book
update_book("978-0-123456-78-9", title="Dune: Part One")

# Delete a book (only if not borrowed)
delete_book("978-1-111111-11-1")  # Should fail (still borrowed)
return_book("M001", "978-1-111111-11-1")
delete_book("978-1-111111-11-1")  # Now should succeed

print("\n✅ Demo completed successfully!")