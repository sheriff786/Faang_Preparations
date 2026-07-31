#Adjacency list (array list of array)


class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        
class Graph:

    def __init__(self, vertices):
        self.vertices = vertices

        # Create empty adjacency list
        self.graph = {}

        for i in range(vertices):
            self.graph[i] = []
            
    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        
    def add_undirected_edge(self, src, dest):

        self.graph[src].append(Edge(src, dest))
        self.graph[dest].append(Edge(dest, src))
    
    
    def print_graph(self):

        for vertex in self.graph:
            print(f"{vertex} -> ", end="")

            for edge in self.graph[vertex]:
                print(edge.dest, end=" ")

            print()
            
'''
      0
     / \
    1   2
    |   |
    3---4
    
0 - 1
0 - 2
1 - 3
2 - 4
3 - 4
'''

g = Graph(5)

g.add_undirected_edge(0,1)
g.add_undirected_edge(0,2)
g.add_undirected_edge(1,3)
g.add_undirected_edge(2,4)
g.add_undirected_edge(3,4)

g.print_graph()

print("in new way\n")
g = Graph(5)

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,4)

print(g.graph)

print("\n \n")
print("--------weighted undirectional graph")
#--------------------------------------Weighted graph--------------------------------------------

class Edge:

    def __init__(self, src, dest, weight):

        self.src = src
        self.dest = dest
        self.weight = weight
class Graph:

    def __init__(self, vertices):

        self.vertices = vertices
        self.graph = {}

        for i in range(vertices):
            self.graph[i] = []

    def add_edge(self, src, dest, weight):

        self.graph[src].append(Edge(src, dest, weight))
        self.graph[dest].append(Edge(dest, src, weight))
        
    def print_graph(self):

        for vertex in self.graph:

            print(vertex, end=" -> ")

            for edge in self.graph[vertex]:
                print(f"({edge.dest},{edge.weight})", end=" ")

            print()
            
g = Graph(5)

g.add_edge(0,1,4)
g.add_edge(0,2,2)
g.add_edge(1,3,5)
g.add_edge(2,4,1)
g.add_edge(3,4,3)

g.print_graph()

print("\n \n \n")
print("----------directed weighted graphs-------\n")

#-------------------------------Directed weighted graphs----------------------------


class Graph:

    def __init__(self, vertices):

        self.vertices = vertices

        # Adjacency List
        self.graph = {}

        # Create an empty list for every vertex
        for i in range(vertices):
            self.graph[i] = []

    # Add a directed edge
    def add_edge(self, src, dest, weight):

        self.graph[src].append((dest, weight))

    # Print graph
    def print_graph(self):

        for vertex in self.graph:

            print(f"{vertex} -> ", end="")

            for dest, weight in self.graph[vertex]:
                print(f"({dest}, {weight})", end=" ")

            print()
            
g = Graph(4)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 1)

g.print_graph()

'''
A simple rule to remember
Undirected

self.graph[src].append((dest, weight))
self.graph[dest].append((src, weight))


Directed
self.graph[src].append((dest, weight))

Think:

One-way street.


'''



'''
Since you're learning from scratch, I recommend this sequence:
✅ Directed Unweighted Graph (graph[src].append(dest))
✅ Undirected Unweighted Graph
✅ Directed Weighted Graph (graph[src].append((dest, weight)))
✅ Undirected Weighted Graph
✅ BFS
✅ DFS
✅ Cycle Detection
✅ Topological Sort
✅ Shortest Path (Dijkstra, Bellman-Ford)
✅ MST (Prim's, Kruskal's)
'''

