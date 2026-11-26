
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newnode = Node(data)

        if self.root is None:
            self.root = newnode
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = newnode
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = newnode
                    return
                current = current.right

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


n = int(input())
tree = BST()

nums = list(map(int, input().split()))

for i in range(n):
    tree.insert(nums[i])

print("Inorder Traversal:")
tree.inorder(tree.root)
print()

print("Preorder Traversal:")
tree.preorder(tree.root)
print()

print("Postorder Traversal:")
tree.postorder(tree.root)
print()
