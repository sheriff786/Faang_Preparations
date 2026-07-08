from collections import deque


class Edge:
    def __init__(self, s, d, w):
        self.src = s
        self.dest = d
        self.wt = w
    
def createGraph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[0].append(Edge(0, 1, 1))
    graph[0].append(Edge(0, 2, 1))

    graph[1].append(Edge(1, 0, 1))
    graph[1].append(Edge(1, 3, 1))

    graph[2].append(Edge(2, 0, 1))
    graph[2].append(Edge(2, 4, 1))

    graph[3].append(Edge(3, 1, 1))
    graph[3].append(Edge(3, 4, 1))
    graph[3].append(Edge(3, 5, 1))

    graph[4].append(Edge(4, 2, 1))
    graph[4].append(Edge(4, 3, 1))
    graph[4].append(Edge(4, 5, 1))

    graph[5].append(Edge(5, 3, 1))
    graph[5].append(Edge(5, 4, 1))
    graph[5].append(Edge(5, 6, 1))

    graph[6].append(Edge(6, 5, 1))
    
def printAllPaths(graph, visited, curr, path, target):

    # Base case
    if curr == target:
        print(path)
        return

    visited[curr] = True

    for i in range(len(graph[curr])):
        edge = graph[curr][i]

        if not visited[edge.dest]:
            printAllPaths(
                graph,
                visited,
                edge.dest,
                path + "->" + str(edge.dest),
                target
            )

    visited[curr] = False  # Backtrack
        
        
    

    # Mark the current node as visited and add it to the path
    
    
# Create and populate the graph
V = 7  # number of vertices
graph = [None] * V
createGraph(graph)

# Print the complete Adjacency List representation
print("=" * 60)
print("ADJACENCY LIST REPRESENTATION OF THE GRAPH:")
print("=" * 60)
print("""
    Visual Graph:
       1 ----- 3
      /         | \\
     0          |  5 ---- 6
      \\         | /
       2 ----- 4

    Adjacency List:
    0 -> [1, 2]
    1 -> [0, 3]
    2 -> [0, 4]
    3 -> [1, 4, 5]
    4 -> [2, 3, 5]
    5 -> [3, 4, 6]
    6 -> [5]
""")
print("Adjacency List (from code):")
for i in range(V):
    neighbors = [edge.dest for edge in graph[i]]
    print(f"  {i} -> {neighbors}")
print()

print("Detailed Edge Info:")
for i in range(V):
    print(f"  Node {i} -> ", end="")
    for edge in graph[i]:
        print(f"(dest={edge.dest}, wt={edge.wt})", end=" ")
    print()
print("=" * 60)

print("all path from src to target")

src = 0;
tar = 5;
visited = [False] * V
visited[src] = True

print("All paths from", src, "to", tar, ":\n")
printAllPaths(graph, visited, src, str(src), tar)