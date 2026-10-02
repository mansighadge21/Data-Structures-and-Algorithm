class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert node into BST
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    else:
        print("Duplicate value not inserted.")

    return root


# Level Order Traversal
def level_order(root):
    if root is None:
        print("Tree is Empty")
        return

    queue = [root]

    while queue:
        current = queue.pop(0)

        print(current.data, end=" ")

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)


# Copy BST
def copy_tree(root):
    if root is None:
        return None

    new_node = Node(root.data)

    new_node.left = copy_tree(root.left)
    new_node.right = copy_tree(root.right)

    return new_node


# Find Height
def height(root):
    if root is None:
        return -1

    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1


# Print Leaf Nodes
def print_leaf_nodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return

    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)


# Main Program
root = None
copy_root = None

while True:
    print("\n====================================")
    print("       BINARY SEARCH TREE MENU")
    print("====================================")
    print("1. Insert Node")
    print("2. Display Original BST (Level Order)")
    print("3. Copy BST")
    print("4. Display Copied BST (Level Order)")
    print("5. Find Height of BST")
    print("6. Display Leaf Nodes")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            value = int(input("Enter value: "))
            root = insert(root, value)

    elif choice == 2:
        print("Original BST (Level Order):")
        level_order(root)
        print()

    elif choice == 3:
        copy_root = copy_tree(root)
        print("BST Copied Successfully")

    elif choice == 4:
        print("Copied BST (Level Order):")
        level_order(copy_root)
        print()

    elif choice == 5:
        h = height(root)
        print("Height of BST =", h)

    elif choice == 6:
        print("Leaf Nodes:")
        print_leaf_nodes(root)
        print()

    elif choice == 7:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")