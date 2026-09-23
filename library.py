books = []


def show_menu():
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. View Available Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Borrowed Books")
    print("6. Exit")


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if title == "" or author == "":
        print("Error: Title and author cannot be empty.")
        return

    for book in books:
        if book["title"].lower() == title.lower():
            print("Error: This book already exists.")
            return

    book = {
        "title": title,
        "author": author,
        "status": "available"
    }

    books.append(book)
    print(f"Book '{title}' added successfully.")


def view_available_books():
    available_books = []

    for book in books:
        if book["status"] == "available":
            available_books.append(book)

    if len(available_books) == 0:
        print("No books are currently available.")
        return

    print("\n===== AVAILABLE BOOKS =====")

    for number, book in enumerate(available_books, 1):
        print(f"{number}. {book['title']} - {book['author']}")


def borrow_book():
    title = input("Enter book title to borrow: ").strip()

    if title == "":
        print("Error: Book title cannot be empty.")
        return

    for book in books:
        if book["title"].lower() == title.lower():

            if book["status"] == "borrowed":
                print("This book is already borrowed.")
                return

            book["status"] = "borrowed"
            print(f"You have borrowed '{book['title']}'.")
            return

    print("Book not found in the library.")


def return_book():
    title = input("Enter book title to return: ").strip()

    if title == "":
        print("Error: Book title cannot be empty.")
        return

    for book in books:
        if book["title"].lower() == title.lower():

            if book["status"] == "available":
                print("This book was not borrowed.")
                return

            book["status"] = "available"
            print(f"You have returned '{book['title']}'.")
            return

    print("Book not found in the library.")


def view_borrowed_books():
    borrowed_books = []

    for book in books:
        if book["status"] == "borrowed":
            borrowed_books.append(book)

    if len(borrowed_books) == 0:
        print("No books are currently borrowed.")
        return

    print("\n===== BORROWED BOOKS =====")

    for number, book in enumerate(borrowed_books, 1):
        print(f"{number}. {book['title']} - {book['author']}")


while True:

    show_menu()

    choice = input("Enter your choice (1-6): ").strip()

    try:
        if choice == "1":
            add_book()

        elif choice == "2":
            view_available_books()

        elif choice == "3":
            borrow_book()

        elif choice == "4":
            return_book()

        elif choice == "5":
            view_borrowed_books()

        elif choice == "6":
            print("Thank you for using the library system!")
            break

        else:
            print("Invalid choice. Please select 1-6.")

    except Exception as error:
        print("An unexpected error occurred:", error)
