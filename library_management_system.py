def display_books(books):
    print("\nAvailable Books:")
    for book in books:
        print("-", book)


def issue_book(books):
    name = input("Enter book name to issue: ")
    
    if name in books:
        books.remove(name)
        print("Book issued successfully")
    else:
        print("Book not available")


def return_book(books):
    name = input("Enter book name to return: ")
    
    if name in books:
        print("Book already exists in library")
    else:
        books.append(name)
        print("Book returned successfully")


def library_menu():
    books = ["Python", "C Programming", "Data Science", "AI Basics"]

    while True:
        print("\n--- Library Menu ---")
        print("1. View Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_books(books)

        elif choice == 2:
            issue_book(books)

        elif choice == 3:
            return_book(books)

        elif choice == 4:
            print("Exiting Library System")
            break

        else:
            print("Invalid choice")


library_menu()