class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree():
    value = int(input("Enter data (-1 for no node): "))

    if value == -1:
        return None

    new_node = Node(value)

    print("Enter left child of", value)
    new_node.left = create_tree()

    print("Enter right child of", value)
    new_node.right = create_tree()

    return new_node


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


print("Create Binary Tree")
root = create_tree()

print("\nInorder Traversal:", end=" ")
inorder(root)

print("\nPreorder Traversal:", end=" ")
preorder(root)

print("\nPostorder Traversal:", end=" ")
postorder(root)