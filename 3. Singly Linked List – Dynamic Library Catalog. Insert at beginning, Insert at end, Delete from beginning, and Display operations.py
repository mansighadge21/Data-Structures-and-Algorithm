class Node:
    def __init__(self, book):
        self.book = book
        self.next = None


head = None


def insert_beginning():
    global head

    book = input("Enter book name: ")

    new_node = Node(book)
    new_node.next = head
    head = new_node

    print("Book inserted at beginning.")


def insert_end():
    global head

    book = input("Enter book name: ")

    new_node = Node(book)

    if head is None:
        head = new_node
    else:
        temp = head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    print("Book inserted at end.")


def delete_beginning():
    global head

    if head is None:
        print("Library catalog is empty.")
    else:
        book = head.book
        head = head.next
        print("Book deleted:", book)


def display():
    if head is None:
        print("Library catalog is empty.")
    else:
        temp = head

        print("Library Catalog:")
        while temp is not None:
            print(temp.book)
            temp = temp.next


while True:
    print("\n--- Library Catalog ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_beginning()

    elif choice == 2:
        insert_end()

    elif choice == 3:
        delete_beginning()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")