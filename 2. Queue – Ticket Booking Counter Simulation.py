queue = []
MAX = 5

def enqueue():
    if len(queue) == MAX:
        print("Queue is full.")
    else:
        name = input("Enter customer name: ")
        queue.append(name)
        print("Customer added to queue.")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        name = queue.pop(0)
        print("Ticket booked for:", name)

def display():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Customers in queue:")
        for name in queue:
            print(name)

while True:
    print("\n--- Ticket Booking Counter ---")
    print("1. Add Customer")
    print("2. Book Ticket")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")