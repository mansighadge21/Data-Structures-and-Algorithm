
# General Binary Tree (Scenario-Based)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        new = Node(x)

        if self.root is None:
            self.root = new
            return

        q = [self.root]

        while q:
            temp = q.pop(0)

            if temp.left is None:
                temp.left = new
                return
            else:
                q.append(temp.left)

            if temp.right is None:
                temp.right = new
                return
            else:
                q.append(temp.right)

    def inorder(self, temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            self.inorder(temp.right)

    def preorder(self, temp):
        if temp is not None:
            print(temp.data, end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)

    def postorder(self, temp):
        if temp is not None:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data, end=" ")

    def levelorder(self):
        if self.root is None:
            print("Tree is Empty")
            return

        q = [self.root]

        while q:
            temp = q.pop(0)
            print(temp.data, end=" ")

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)

        print()

    def search(self, x):
        if self.root is None:
            return False

        q = [self.root]

        while q:
            temp = q.pop(0)

            if temp.data == x:
                return True

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)

        return False


# Main Program

t = BinaryTree()

while True:
    print("\n1. Insert")
    print("2. Inorder")
    print("3. Preorder")
    print("4. Postorder")
    print("5. Level Order")
    print("6. Search")
    print("7. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        x = input("Enter data: ")
        t.insert(x)

    elif ch == 2:
        if t.root is None:
            print("Tree is Empty")
        else:
            t.inorder(t.root)
            print()

    elif ch == 3:
        if t.root is None:
            print("Tree is Empty")
        else:
            t.preorder(t.root)
            print()

    elif ch == 4:
        if t.root is None:
            print("Tree is Empty")
        else:
            t.postorder(t.root)
            print()

    elif ch == 5:
        t.levelorder()

    elif ch == 6:
        x = input("Enter data to search: ")

        if t.search(x):
            print("Element Found")
        else:
            print("Element Not Found")

    elif ch == 7:
        break

    else:
        print("Invalid Choice")
