stack = []

def return_book():
    book = input("Enter book name to return: ")
    stack.append(book)
    print("Book returned successfully.")

def issue_book():
    if len(stack) == 0:
        print("No books available in the stack.")
    else:
        book = stack.pop()
        print("Book removed from stack:", book)

def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Books in stack:")
        for book in reversed(stack):
            print(book)

while True:
    print("\n--- Library Book Return Management ---")
    print("1. Return Book")
    print("2. Remove Top Book")
    print("3. Display Books")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        return_book()

    elif choice == 2:
        issue_book()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")