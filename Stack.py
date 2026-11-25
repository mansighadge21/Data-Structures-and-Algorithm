stack = []

def push():
    element = int(input("Enter element to push: "))
    stack.append(element)
    print("Element pushed successfully.")

def pop():
    if len(stack) == 0:
        print("Stack Underflow! Stack is empty.")
    else:
        element = stack.pop()
        print("Popped element:", element)

def peek():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Top element:", stack[-1])

def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack elements:")
        for element in reversed(stack):
            print(element)

while True:
    print("\n--- Stack Operations ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")