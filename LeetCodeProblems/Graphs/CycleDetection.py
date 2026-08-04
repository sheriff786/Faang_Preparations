# ==============================================================================
# =================== CYCLE DETECTION IN GRAPHS ================================
# ==============================================================================
#
# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                    UNDIRECTED GRAPH (Visual)                                ║
# ║                                                                             ║
# ║         0 ———————— 1                                                       ║
# ║        /|         / |                                                       ║
# ║       / |        /  |                                                       ║
# ║      /  |       /   |                                                       ║
# ║     3   |      /    |                                                       ║
# ║     |   |     /     |                                                       ║
# ║     |    \   /      |                                                       ║
# ║     4     \ /       |                                                       ║
# ║            2 ———————+  (0-1-2 forms a cycle)                                ║
# ║                                                                             ║
# ║  Edges: 0--1, 0--2, 0--3, 1--2, 3--4                                       ║
# ║  Cycle: 0 → 1 → 2 → 0 (ya koi bhi path jo wapas aaye)                     ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                    DIRECTED GRAPH (Visual)                                  ║
# ║                                                                             ║
# ║         0                                                                   ║
# ║        / \                                                                  ║
# ║       ↓   ↓                                                                ║
# ║      1     2                                                                ║
# ║      |     |                                                                ║
# ║      ↓     ↓                                                                ║
# ║      3 ←———+                                                               ║
# ║      |                                                                      ║
# ║      ↓                                                                      ║
# ║      4 ——→ 1  (BACK EDGE! Cycle: 1→3→4→1)                                  ║
# ║                                                                             ║
# ║  Edges: 0→1, 0→2, 1→3, 2→3, 3→4, 4→1                                      ║
# ║  Cycle: 1 → 3 → 4 → 1 (direction matters!)                                ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
#
# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║          FAANG INTERVIEW GUIDE — Kab Kaunsa Approach Use Karna Hai?        ║
# ╠══════════════════════════════════════════════════════════════════════════════╣
# ║                                                                             ║
# ║  🔑 STEP 1: Pehle identify karo — Graph DIRECTED hai ya UNDIRECTED?        ║
# ║                                                                             ║
# ║  ┌─────────────────────────────────────────────────────────────────┐        ║
# ║  │  UNDIRECTED GRAPH → "Parent Tracking" approach use karo         │        ║
# ║  │  DIRECTED GRAPH   → "Recursion Stack" approach use karo         │        ║
# ║  └─────────────────────────────────────────────────────────────────┘        ║
# ║                                                                             ║
# ║  ⚠️  GALTI JO LOG KARTE HAIN (Common Mistakes):                            ║
# ║  • Undirected mein recursion stack use karna — GALAT! Ye false positive     ║
# ║    nahi dega but unnecessary complexity hai                                  ║
# ║  • Directed mein parent tracking use karna — GALAT! Ye MISS karega cycles  ║
# ║    Example: A→B, A→C→B mein B visited hai but cycle nahi hai,              ║
# ║    parent check se galat answer aayega                                       ║
# ║                                                                             ║
# ╠══════════════════════════════════════════════════════════════════════════════╣
# ║                                                                             ║
# ║  🔑 STEP 2: Kaunsa scenario hai? (FAANG mein ye poochte hain)              ║
# ║                                                                             ║
# ║  ┌─────────────────────────────────────────────────────────────────┐        ║
# ║  │ SCENARIO                    │ APPROACH                          │        ║
# ║  ├─────────────────────────────┼───────────────────────────────────┤        ║
# ║  │ Undirected + DFS            │ Parent tracking (is_cyclic_util)  │        ║
# ║  │ Undirected + BFS            │ BFS + parent check (Kahn's nahi) │        ║
# ║  │ Undirected + Union-Find     │ Best for dynamic edge addition   │        ║
# ║  │ Directed + DFS              │ Recursion Stack (rec_stack[])     │        ║
# ║  │ Directed + BFS              │ Kahn's Algorithm (Topological)   │        ║
# ║  │ Directed + coloring         │ WHITE/GRAY/BLACK (same as rec)   │        ║
# ║  └─────────────────────────────┴───────────────────────────────────┘        ║
# ║                                                                             ║
# ╠══════════════════════════════════════════════════════════════════════════════╣
# ║                                                                             ║
# ║  🔑 STEP 3: Worst Case Scenarios                                           ║
# ║                                                                             ║
# ║  TIME:  O(V + E) — Dono approaches ka same hai                             ║
# ║  SPACE: O(V) — visited + rec_stack/parent                                  ║
# ║                                                                             ║
# ║  WORST CASE kab hota hai?                                                  ║
# ║  • Jab graph mein cycle LAST mein milta hai ya milta hi nahi                ║
# ║  • Tab poora graph traverse karna padta hai → O(V + E)                     ║
# ║  • Example: Linear chain 0→1→2→...→N with cycle only at end               ║
# ║                                                                             ║
# ║  SPACE worst case:                                                          ║
# ║  • Recursion depth = O(V) jab graph ek line jaisa ho (skewed)              ║
# ║  • Stack overflow ho sakta hai → Iterative DFS ya BFS consider karo        ║
# ║                                                                             ║
# ╠══════════════════════════════════════════════════════════════════════════════╣
# ║                                                                             ║
# ║  🔑 FAANG FOLLOW-UP QUESTIONS (ye zaroor poochenge):                        ║
# ║                                                                             ║
# ║  Q: "Graph disconnected hai to?" (Multiple components)                     ║
# ║  A: Loop lagao har unvisited node pe — dono code mein ye already hai       ║
# ║                                                                             ║
# ║  Q: "Self-loop hai to?"                                                    ║
# ║  A: Undirected: neighbor != parent check handle karega                     ║
# ║     Directed: rec_stack[curr] = True set karte hi, agar curr ka            ║
# ║     neighbor curr hi hai to rec_stack[curr] = True milega → cycle          ║
# ║                                                                             ║
# ║  Q: "Cycle print karo / path batao"                                        ║
# ║  A: Parent array maintain karo, jab cycle mile tab backtrack karo          ║
# ║                                                                             ║
# ║  Q: "Union-Find vs DFS kab?"                                               ║
# ║  A: Union-Find jab edges dynamically add ho rahe hain (online query)       ║
# ║     DFS jab poora graph ek baar mein diya hai (offline)                    ║
# ║                                                                             ║
# ║  Q: "BFS se cycle detect ho sakta hai directed mein?"                      ║
# ║  A: Haan! Kahn's Algorithm — Topological sort karo, agar saare nodes      ║
# ║     process nahi hue → cycle hai (in-degree based approach)                ║
# ║                                                                             ║
# ╠══════════════════════════════════════════════════════════════════════════════╣
# ║                                                                             ║
# ║  💡 QUICK DECISION FORMULA (Interview mein ye bolo):                        ║
# ║                                                                             ║
# ║  "Sir, pehle main check karunga ki graph directed hai ya undirected.       ║
# ║   Agar undirected hai → DFS with parent tracking, O(V+E).                  ║
# ║   Agar directed hai → DFS with recursion stack to detect back edges.       ║
# ║   Disconnected components ke liye main har unvisited node se DFS           ║
# ║   start karunga."                                                           ║
# ║                                                                             ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
#
# ==============================================================================


class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


def create_graph(V):
    graph = [[] for _ in range(V)]

    graph[0].append(Edge(0, 1))
    graph[0].append(Edge(0, 2))
    graph[0].append(Edge(0, 3))

    graph[1].append(Edge(1, 0))
    graph[1].append(Edge(1, 2))

    graph[2].append(Edge(2, 0))
    graph[2].append(Edge(2, 1))

    graph[3].append(Edge(3, 0))
    graph[3].append(Edge(3, 4))

    graph[4].append(Edge(4, 3))

    return graph


def is_cyclic_util(graph, visited, curr, parent):
    visited[curr] = True

    for edge in graph[curr]:
        neighbor = edge.dest

        # Case 1: Not visited → DFS
        if not visited[neighbor]:
            if is_cyclic_util(graph, visited, neighbor, curr):
                return True

        # Case 2: Visited and not parent → Cycle
        elif neighbor != parent:
            return True

    return False


# O(V + E)
def is_cyclic(graph):
    visited = [False] * len(graph)

    for i in range(len(graph)):
        if not visited[i]:
            if is_cyclic_util(graph, visited, i, -1):
                return True

    return False


# Main
V = 5
graph = create_graph(V)

print("Adjacency List (from code):")
for i in range(V):
    neighbors = [edge.dest for edge in graph[i]]
    print(f"  {i} -> {neighbors}")
print()

print("Detailed Edge Info:")
for i in range(V):
    print(f"  Node {i} -> ", end="")
    for edge in graph[i]:
        print(f"(dest={edge.dest}", end=" ")
    print()
print("=" * 60)

result = is_cyclic(graph)
print(f"Cycle Detected (Undirected): {result}")

# ========================= DRY RUN (Undirected Graph) =========================
# Graph:
#   0 -- 1
#   |  / |
#   2    |
#   |
#   3 -- 4
#
# Adjacency List:
#   0 -> [1, 2, 3]
#   1 -> [0, 2]
#   2 -> [0, 1]
#   3 -> [0, 4]
#   4 -> [3]
#
# DFS starts at node 0, parent = -1
#   visited = [T, F, F, F, F]
#   Explore neighbor 1 (not visited) → DFS(1, parent=0)
#       visited = [T, T, F, F, F]
#       Explore neighbor 0 → visited but parent → skip
#       Explore neighbor 2 (not visited) → DFS(2, parent=1)
#           visited = [T, T, T, F, F]
#           Explore neighbor 0 → visited and NOT parent (parent=1) → CYCLE FOUND!
#           Return True
#       Return True
#   Return True
#
# Result: Cycle Detected = True
# ==============================================================================


# ==============================================================================
# ================ DIRECTED GRAPH - Cycle Detection using DFS ==================
# ==============================================================================
# Approach: Use recursion stack (rec_stack) to detect back edges.
# A cycle exists if we visit a node that is already in the current recursion stack.
# Unlike undirected graphs, we can't just check "parent" because direction matters.

print("\n" + "=" * 60)
print("DIRECTED GRAPH - Cycle Detection")
print("=" * 60)


def create_directed_graph(V):
    graph = [[] for _ in range(V)]

    # Directed edges (one-way)
    graph[0].append(Edge(0, 1))
    graph[0].append(Edge(0, 2))
    graph[1].append(Edge(1, 3))
    graph[2].append(Edge(2, 3))
    graph[3].append(Edge(3, 4))
    graph[4].append(Edge(4, 1))  # Back edge: 4 -> 1 creates a cycle (1->3->4->1)

    return graph


def is_cyclic_directed_util(graph, visited, rec_stack, curr):
    visited[curr] = True
    rec_stack[curr] = True

    for edge in graph[curr]:
        neighbor = edge.dest

        # Case 1: Not visited → DFS deeper
        if not visited[neighbor]:
            if is_cyclic_directed_util(graph, visited, rec_stack, neighbor):
                return True

        # Case 2: Visited AND in current recursion stack → Cycle (back edge)
        elif rec_stack[neighbor]:
            return True

    # Backtrack: remove from recursion stack
    rec_stack[curr] = False
    return False


# O(V + E)
def is_cyclic_directed(graph):
    V = len(graph)
    visited = [False] * V
    rec_stack = [False] * V

    for i in range(V):
        if not visited[i]:
            if is_cyclic_directed_util(graph, visited, rec_stack, i):
                return True

    return False


# Main - Directed Graph
V_directed = 5
directed_graph = create_directed_graph(V_directed)

print("\nDirected Adjacency List:")
for i in range(V_directed):
    neighbors = [edge.dest for edge in directed_graph[i]]
    print(f"  {i} -> {neighbors}")
print()

result_directed = is_cyclic_directed(directed_graph)
print(f"Cycle Detected (Directed): {result_directed}")

# ========================= DRY RUN (Directed Graph) ===========================
# Graph (Directed):
#   0 → 1 → 3 → 4
#   0 → 2 → 3     ↑
#              4 → 1  (back edge creating cycle: 1 → 3 → 4 → 1)
#
# Adjacency List:
#   0 -> [1, 2]
#   1 -> [3]
#   2 -> [3]
#   3 -> [4]
#   4 -> [1]   ← back edge
#
# DFS starts at node 0
#   visited = [T, F, F, F, F], rec_stack = [T, F, F, F, F]
#   Explore neighbor 1 → DFS(1)
#       visited = [T, T, F, F, F], rec_stack = [T, T, F, F, F]
#       Explore neighbor 3 → DFS(3)
#           visited = [T, T, F, T, F], rec_stack = [T, T, F, T, F]
#           Explore neighbor 4 → DFS(4)
#               visited = [T, T, F, T, T], rec_stack = [T, T, F, T, T]
#               Explore neighbor 1 → visited=True AND rec_stack[1]=True → CYCLE!
#               Return True
#           Return True
#       Return True
#   Return True
#
# Result: Cycle Detected = True
#
# Key Difference from Undirected:
#   - Undirected: Check if neighbor is visited and NOT parent
#   - Directed: Check if neighbor is in the current recursion stack (back edge)
#   - rec_stack tracks nodes in the current DFS path only
#   - A visited node NOT in rec_stack means it was fully processed (no cycle through it)
# ==============================================================================


'''undirected grapgh dfs (parent approach)'''

class Solution:

    def isCycle(self, adj):

        n = len(adj)

        visited = [False] * n

        def dfs(node, parent):

            visited[node] = True

            for neighbour in adj[node]:

                if not visited[neighbour]:

                    if dfs(neighbour, node):
                        return True

                elif neighbour != parent:

                    return True

            return False

        # Handle disconnected graph
        for i in range(n):

            if not visited[i]:

                if dfs(i, -1):
                    return True

        return False
    
'''Cycle detection in graph using bfs'''

from collections import deque

class Solution:

    def isCycle(self, adj):

        n = len(adj)

        visited = [False] * n

        def bfs(start):

            queue = deque()

            queue.append((start, -1))

            visited[start] = True

            while queue:

                node, parent = queue.popleft()

                for neighbour in adj[node]:

                    if not visited[neighbour]:

                        visited[neighbour] = True

                        queue.append((neighbour, node))

                    elif neighbour != parent:

                        return True

            return False

        # Handle disconnected graph
        for i in range(n):

            if not visited[i]:

                if bfs(i):
                    return True

        return False
    
    '''
    
    DFS vs BFS
DFS	BFS
Uses recursion	Uses queue
Passes (node, parent) through recursion	Stores (node, parent) in queue
dfs(neighbour, node)	queue.append((neighbour, node))
Same cycle condition	Same cycle condition
Time: O(V + E)	Time: O(V + E)
Space: O(V)	Space: O(V)
    
    '''
    
    
#Cycle Detection in Directed Graph (DFS)

#for this we need to use two array approach

class Solution:

    def isCycle(self, adj):

        n = len(adj)

        visited = [False] * n
        pathVisited = [False] * n

        def dfs(node):

            visited[node] = True
            pathVisited[node] = True

            for neighbour in adj[node]:

                if not visited[neighbour]:

                    if dfs(neighbour):
                        return True

                elif pathVisited[neighbour]:

                    return True

            # Remove node from current DFS path
            pathVisited[node] = False

            return False

        # Handle disconnected graph
        for i in range(n):

            if not visited[i]:

                if dfs(i):
                    return True

        return False
    
'''cyccle detection in directed graph using bfs


Detect Cycle in a Directed Graph using BFS
Last Updated :
11 Jul, 2025
Given a directed graph, check whether the graph contains a cycle or not. Your function should return true if the given graph contains at least one cycle, else return false. For example, the following graph contains two cycles 0->1->2->3->0 and 2->4->2, so your function must return true.



We have discussed a DFS based solution to detect cycle in a directed graph. In this post, BFS based solution is discussed.
The idea is to simply use Kahn's algorithm for Topological Sorting

Steps involved in detecting cycle in a directed graph using BFS.
Step-1: Compute in-degree (number of incoming edges) for each of the vertex present in the graph and initialize the count of visited nodes as 0.
Step-2: Pick all the vertices with in-degree as 0 and add them into a queue (Enqueue operation)
Step-3: Remove a vertex from the queue (Dequeue operation) and then. 

Increment count of visited nodes by 1.
Decrease in-degree by 1 for all its neighboring nodes.
If in-degree of a neighboring nodes is reduced to zero, then add it to the queue.
Step 4: Repeat Step 3 until the queue is empty.
Step 5: If count of visited nodes is not equal to the number of nodes in the graph has cycle, otherwise not.

How to find in-degree of each node? 
There are 2 ways to calculate in-degree of every vertex: 
Take an in-degree array which will keep track of 
1) Traverse the array of edges and simply increase the counter of the destination node by 1. 

for each node in Nodes
    indegree[node] = 0;
for each edge(src,dest) in Edges
    indegree[dest]++
Time Complexity: O(V+E)

2) Traverse the list for every node and then increment the in-degree of all the nodes connected to it by 1. 

    for each node in Nodes
        If (list[node].size()!=0) then
        for each dest in list
            indegree[dest]++;
Time Complexity: The outer for loop will be executed V number of times and the inner for loop will be executed E number of times, Thus overall time complexity is O(V+E).

The overall time complexity of the algorithm is O(V+E) 

'''

# A Python3 program to check if there is a cycle in  
# directed graph using BFS. 
import math
import sys
from collections import defaultdict

# # Class to represent a graph 
# class Graph:
#     def __init__(self,vertices):
#         self.graph=defaultdict(list)
#         self.V=vertices # No. of vertices' 
    
#     # function to add an edge to graph
#     def addEdge(self,u,v):
#         self.graph[u].append(v)

# This function returns true if there is a cycle 
# in directed graph, else returns false. 
def isCycleExist(n,graph):

    # Create a vector to store indegrees of all 
    # vertices. Initialize all indegrees as 0. 
    in_degree=[0]*n

    # Traverse adjacency lists to fill indegrees of 
    # vertices. This step takes O(V+E) time
    for i in range(n):
        for j in graph[i]:
            in_degree[j]+=1
    
    # Create an queue and enqueue all vertices with 
    # indegree 0
    queue=[]
    for i in range(len(in_degree)):
        if in_degree[i]==0:
            queue.append(i)
    
    # Initialize count of visited vertices
    cnt=0

    # One by one dequeue vertices from queue and enqueue 
    # adjacents if indegree of adjacent becomes 0 
    while(queue):

        # Extract front of queue (or perform dequeue) 
        # and add it to topological order 
        nu=queue.pop(0)

        # Iterate through all its neighbouring nodes 
        # of dequeued node u and decrease their in-degree 
        # by 1 
        for v in graph[nu]:
            in_degree[v]-=1

            # If in-degree becomes zero, add it to queue
            if in_degree[v]==0:
                queue.append(v)
        cnt+=1

    # Check if there was a cycle 
    if cnt==n:
        return False
    else:
        return True
        

# Driver program to test above functions 

    