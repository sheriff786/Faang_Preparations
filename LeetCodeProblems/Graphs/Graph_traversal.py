    #   1 ----- 3
    #  /        | \
    # 0         |  5 ---- 6
    #  \        | /
    #   2 ----- 4


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
    

def bfs(graph, visited, start):
    
    # visited = [False] * len(graph)

    q = deque()

    q.append(0)   # Source = 0
    
    while q:
        curr =q.popleft()
        if visited[curr] == False:
            print(curr, end=" ")
            visited[curr] = True

            for i in range(len(graph[curr])):
                edge = graph[curr][i]
                q.append(edge.dest)
    print()
    
def bfsDisconnected(graph):

    visited = [False] * len(graph)

    for i in range(len(graph)):

        if not visited[i]:

            bfs(graph, visited, i)
    


def dfs(graph, visited, start):
    if visited[start] == True:
        return
    
    print(start, end=" ")
    visited[start] = True

    for i in range(len(graph[start])):
        edge = graph[start][i]
        dfs(graph, visited, edge.dest)
    
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

print("\nBFS Traversal: ", end="")
bfsDisconnected(graph)



print("DFS Traversal: ", end="")
visited = [False] * V
for i in range(V):
    if not visited[i]:
        dfs(graph, visited, i)


print("\n")
print("=" * 60)
print("REVISION NOTES - BFS & DFS on Graph (Adjacency List)")
print("=" * 60)
print("""
=============================================
1. DATA STRUCTURE: ADJACENCY LIST
=============================================
- We use a list of lists: graph = [None] * V  -->  then each graph[i] = []
- Each graph[i] stores a list of Edge objects representing neighbors of node i.
- Edge has: src, dest, wt (source, destination, weight)

MEMORY ALLOCATION:
    graph = [None] * V
    |  graph is an array of V pointers (references)

    After createGraph:
    graph[0] = [ Edge(0,1,1), Edge(0,2,1) ]       # 2 edges
    graph[1] = [ Edge(1,0,1), Edge(1,3,1) ]       # 2 edges
    graph[2] = [ Edge(2,0,1), Edge(2,4,1) ]       # 2 edges
    graph[3] = [ Edge(3,1,1), Edge(3,4,1), Edge(3,5,1) ]  # 3 edges
    graph[4] = [ Edge(4,2,1), Edge(4,3,1), Edge(4,5,1) ]  # 3 edges
    graph[5] = [ Edge(5,3,1), Edge(5,4,1), Edge(5,6,1) ]  # 3 edges
    graph[6] = [ Edge(6,5,1) ]                    # 1 edge

    Total Space: O(V + E)  where V = vertices, E = edges
    For undirected graph: each edge stored twice (both directions)

=============================================
2. BFS (Breadth-First Search) - LEVEL ORDER
=============================================
APPROACH:
    - Uses a QUEUE (FIFO) - deque in Python
    - Visit level by level (all neighbors first, then their neighbors)
    - Like ripples in water - expands outward

PSEUDOCODE:
    BFS(graph, start):
        visited = [False] * V
        queue = empty deque
        queue.append(start)

        while queue is NOT empty:
            curr = queue.popleft()        # FIFO - remove from front
            if not visited[curr]:
                print(curr)
                visited[curr] = True
                for each neighbor of curr:
                    queue.append(neighbor)

    # For disconnected graph:
    BFS_Disconnected(graph):
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                BFS(graph, visited, i)

MEMORY ALLOCATION FOR BFS:
    - visited[] array: O(V) space
    - Queue: at worst O(V) elements
    - Total Space: O(V)
    - Time Complexity: O(V + E)

TRACE (starting from 0):
    Queue: [0]
    Visit 0 -> Queue: [1, 2]
    Visit 1 -> Queue: [2, 3]
    Visit 2 -> Queue: [3, 4]
    Visit 3 -> Queue: [4, 5]  (skip 1, already visited)
    Visit 4 -> Queue: [5]     (skip 2,3 already visited)
    Visit 5 -> Queue: [6]     (skip 3,4 already visited)
    Visit 6 -> Queue: []      (skip 5 already visited)
    Output: 0 1 2 3 4 5 6

=============================================
3. DFS (Depth-First Search) - GO DEEP FIRST
=============================================
APPROACH:
    - Uses RECURSION (implicit STACK - LIFO)
    - Go as deep as possible, then backtrack
    - Like exploring a maze - go one path fully then come back

PSEUDOCODE:
    DFS(graph, visited, start):
        print(start)
        visited[start] = True

        for each neighbor of start:
            if not visited[neighbor]:
                DFS(graph, visited, neighbor)    # recursive call

    # For disconnected graph:
    for i in range(V):
        if not visited[i]:
            DFS(graph, visited, i)

MEMORY ALLOCATION FOR DFS:
    - visited[] array: O(V) space
    - Recursion call stack: at worst O(V) deep (for a linear graph)
    - Total Space: O(V)
    - Time Complexity: O(V + E)

TRACE (starting from 0):
    DFS(0) -> print 0, go to neighbor 1
      DFS(1) -> print 1, go to neighbor 3 (0 visited)
        DFS(3) -> print 3, go to neighbor 4 (1 visited)
          DFS(4) -> print 4, go to neighbor 2 (3 visited)
            DFS(2) -> print 2, (0,4 visited) backtrack
          back to 4 -> go to neighbor 5 (3 visited)
            DFS(5) -> print 5, go to neighbor 6 (3,4 visited)
              DFS(6) -> print 6, (5 visited) backtrack
    Output: 0 1 3 4 2 5 6

=============================================
4. KEY DIFFERENCES - BFS vs DFS
=============================================
    | Feature        | BFS              | DFS              |
    |----------------|------------------|------------------|
    | Data Structure | Queue (FIFO)     | Stack/Recursion  |
    | Order          | Level by level   | Go deep first    |
    | Space          | O(V) - queue     | O(V) - stack     |
    | Time           | O(V+E)           | O(V+E)           |
    | Use Case       | Shortest path    | Cycle detection  |
    |                | (unweighted)     | Topological sort |
    |                | Level order      | Path finding     |

=============================================
5. WHEN TO USE WHAT?
=============================================
    BFS: Shortest path in unweighted graph, level-order traversal
    DFS: Cycle detection, topological sort, connected components,
         path existence, backtracking problems
""")