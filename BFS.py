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

        if self.root == None:
            self.root = newnode
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left == None:
                    current.left = newnode
                    return
                current = current.left
            else:
                if current.right == None:
                    current.right = newnode
                    return
                current = current.right

    def bfs(self):
        if self.root == None:
            return

        q = queue(100)
        q.insert(self.root)

        print("Level-wise Traversal:")

        while q.front <= q.rear:
            current = q.delete()
            print(current.data, end=" ")

            if current.left != None:
                q.insert(current.left)

            if current.right != None:
                q.insert(current.right)


class queue:
    def __init__(self, size):
        self.front = 0
        self.rear = -1
        self.q = [None] * size

    def insert(self, x):
        self.rear += 1
        self.q[self.rear] = x

    def delete(self):
        x = self.q[self.front]
        self.front += 1
        return x


n = int(input())
tree = BST()

values = list(map(int, input().split()))

for i in range(n):
    tree.insert(values[i])

tree.bfs()
