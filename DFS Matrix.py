
class graph:
    def __init__(self, n):
        self.vertices = n
        self.adjmatrix = []

        for i in range(n):
            row = list(map(int, input(f"Enter row {i}: ").split()))
            self.adjmatrix.append(row)

    def dfs(self, start):
        visited = [False]*self.vertices
        s = stack(self.vertices)

        s.push(start)

        print("DFS Traversal:")

        while s.top != -1:
            current = s.pop()

            if visited[current] == False:
                print(current, end=" ")
                visited[current] = True

                for v in range(self.vertices-1, -1, -1):
                    if self.adjmatrix[current][v] == 1 and visited[v] == False:
                        s.push(v)


class stack:
    def __init__(self, size=5):
        self.top = -1
        self.s = [0]*size

    def push(self, x):
        if self.top == len(self.s)-1:
            return
        self.top += 1
        self.s[self.top] = x

    def pop(self):
        x = self.s[self.top]
        self.top -= 1
        return x


n = int(input("Enter number of vertices: "))
g = graph(n)
start = int(input("Enter start vertex: "))
g.dfs(start)
