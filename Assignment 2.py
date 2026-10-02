class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, value):
    new_node = Node(value)

    if root is None:
        return new_node

    current = root

    while True:
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left

        elif value > current.data:
            if current.right is None:
                current.right = new_node
                break
            current = current.right

        else:
            print("Duplicate value not inserted.")
            break

    return root


def inorder_non_recursive(root):
    stack = []
    current = root

    while current is not None or len(stack) > 0:

        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")

        current = current.right


def preorder_non_recursive(root):
    if root is None:
        return

    stack = []
    stack.append(root)

    while len(stack) > 0:

        current = stack.pop()
        print(current.data, end=" ")

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)


# Main Program

root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter value: "))
    root = insert(root, value)

print("\nNon-Recursive Inorder Traversal:")
inorder_non_recursive(root)

print("\nNon-Recursive Preorder Traversal:")
preorder_non_recursive(root)