
class graph:
    def __init__(self, n):
        self.vertices = n
        self.adjlist = [[] for i in range(n)]

    def addEdge(self):
        e = int(input("Enter number of edges: "))

        for i in range(e):
            u, v = map(int, input("Enter edge (u v): ").split())
            self.adjlist[u].append(v)
            self.adjlist[v].append(u)

    def bfs(self, start):
        visited = [False] * self.vertices
        q = queue(self.vertices)

        q.insert(start)
        visited[start] = True

        print("BFS Traversal:")

        while q.f != -1:
            current = q.delete()
            print(current, end=" ")

            for v in self.adjlist[current]:
                if visited[v] == False:
                    visited[v] = True
                    q.insert(v)


class queue:
    def __init__(self, size):
        self.f = -1
        self.r = -1
        self.q = [0] * size

    def insert(self, x):
        if self.f == -1:
            self.f = 0
            self.r = 0
        else:
            self.r += 1

        self.q[self.r] = x

    def delete(self):
        x = self.q[self.f]

        if self.f == self.r:
            self.f = -1
            self.r = -1
        else:
            self.f += 1

        return x


n = int(input())
g = graph(n)
g.addEdge()
start = int(input())
g.bfs(start)
