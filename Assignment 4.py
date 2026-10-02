class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = []

        for i in range(vertices):
            row = []
            for j in range(vertices):
                row.append(0)
            self.adj.append(row)

        self.visited = [False] * vertices

    def create_graph(self):
        edges = int(input("Enter number of edges: "))

        for i in range(edges):
            source = int(input("Enter source vertex: "))
            destination = int(input("Enter destination vertex: "))

            self.adj[source][destination] = 1
            self.adj[destination][source] = 1

    def display_graph(self):
        print("\nAdjacency Matrix:")

        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.adj[i][j], end=" ")
            print()

    def dfs(self, vertex):
        self.visited[vertex] = True
        print(vertex, end=" ")

        for i in range(self.vertices):
            if self.adj[vertex][i] == 1 and self.visited[i] == False:
                self.dfs(i)


# Main Program

vertices = int(input("Enter number of vertices: "))

graph = Graph(vertices)

graph.create_graph()

graph.display_graph()

start = int(input("\nEnter starting vertex: "))

print("DFS Traversal:", end=" ")
graph.dfs(start)

print()