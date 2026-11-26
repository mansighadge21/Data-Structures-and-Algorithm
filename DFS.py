class Graph:

    def __init__(self, v):
        self.v = v
        self.adj = [[0 for i in range(v)] for j in range(v)]
        self.visited = [False] * v

    def add_edge(self, u, w):
        self.adj[u][w] = 1
        self.adj[w][u] = 1

    def display(self):
        for i in range(self.v):
            print(self.adj[i])

    def dfs(self, vertex):
        self.visited[vertex] = True
        print(vertex, end=" ")

        for i in range(self.v):
            if self.adj[vertex][i] == 1 and not self.visited[i]:
                self.dfs(i)


# Main program
v = int(input("Enter number of vertices: "))
g = Graph(v)

e = int(input("Enter number of edges: "))

for i in range(e):
    u, w = map(int, input("Enter edge: ").split())
    g.add_edge(u, w)

print("\nAdjacency Matrix:")
g.display()

start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
g.visited = [False] * v
g.dfs(start)