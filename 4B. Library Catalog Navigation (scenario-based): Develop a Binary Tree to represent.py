class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.book, end=" ")
        inorder(root.right)


def preorder(root):
    if root is not None:
        print(root.book, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.book, end=" ")


# Creating Library Catalog Binary Tree

root = Node("DSA")

root.left = Node("C Programming")
root.right = Node("Python")

root.left.left = Node("Computer Networks")
root.left.right = Node("DBMS")

root.right.left = Node("Java")
root.right.right = Node("Artificial Intelligence")


print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)