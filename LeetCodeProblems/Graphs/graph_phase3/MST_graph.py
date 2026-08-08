"""
================================================================================
MINIMUM SPANNING TREE (MST) — Complete FAANG Interview Guide
================================================================================

PATTERN NAME: Greedy Edge Selection (Prim's / Kruskal's)
DIFFICULTY: Medium-Hard
FREQUENCY: High (Amazon, Google, Microsoft, Facebook)

================================================================================
3 TERMS YOU MUST KNOW BEFORE CODING:
================================================================================

    1. SPANNING: Connects ALL vertices (every node reachable from every other)
    2. TREE:     V vertices, exactly V-1 edges, NO cycles
    3. MINIMUM:  Total edge weight is the smallest possible

    MST = cheapest way to wire all nodes together without loops.

================================================================================
ONE-LINE TRICK TO REMEMBER:
================================================================================

    Prim's:   "Dijkstra but you push EDGE WEIGHT, not total distance."
    Kruskal's: "Sort all edges, pick cheapest that doesn't create cycle (Union-Find)."

================================================================================
MST vs SHORTEST PATH (interviewers test this confusion):
================================================================================

    Shortest Path: "Cheapest route from A to B" → one path matters
    MST:           "Cheapest way to connect ALL nodes" → entire network matters

    Example: Building roads between cities
        Shortest path = best route for ONE trip
        MST = cheapest road network so every city is reachable

================================================================================
KEY PROPERTIES OF MST (quick facts for interviews):
================================================================================

    • V vertices → exactly V-1 edges in MST
    • MST may NOT be unique (multiple MSTs if edges have equal weights)
    • Adding any non-MST edge creates exactly ONE cycle
    • Removing any MST edge disconnects the tree into 2 components
    • MST only exists for CONNECTED graphs (or one MST per component)
    • Works on undirected weighted graphs only

================================================================================
ALGORITHM DECISION:
================================================================================

    ┌─────────────┬──────────────────────┬──────────────┬──────────────────────┐
    │ Algorithm   │ Best When            │ Time         │ Data Structure       │
    ├─────────────┼──────────────────────┼──────────────┼──────────────────────┤
    │ Prim's      │ Dense graph (E ≈ V²) │ O((V+E)logV) │ Min-Heap + visited[] │
    │ Kruskal's   │ Sparse graph (E ≈ V) │ O(E log E)   │ Sort + Union-Find    │
    └─────────────┴──────────────────────┴──────────────┴──────────────────────┘

    FAANG RULE: Know BOTH. Prim's for adjacency list. Kruskal's for edge list.

================================================================================
================================================================================
PART 1: PRIM'S ALGORITHM
================================================================================
================================================================================

SUMMARY: "Start from any node. Greedily pick cheapest edge to an unvisited node. Repeat."

WHY IT LOOKS LIKE DIJKSTRA:
    Dijkstra:  push (TOTAL distance from source, node)
    Prim's:    push (EDGE weight to this node, node)

    Dijkstra finds cheapest PATH. Prim's finds cheapest EDGE to expand the tree.

ALGORITHM IN 4 STEPS:
    Step 1: visited = [False]*V, min_heap = [(0, start_node)], total_cost = 0
    Step 2: Pop cheapest (cost, node) — if already visited, skip
    Step 3: Mark visited, add cost to total
    Step 4: Push all edges to unvisited neighbors into heap

    Repeat until heap empty → total_cost is the MST weight.

VISUAL WALKTHROUGH:
    Graph:
         4         6
    0 ───── 1     1 ─── 2
    │     ╱            ╱
   2│  (6)          (1)
    │ ╱            ╱
    2 ─────────── 3
          1

    Edges: (0,1,4), (0,2,2), (1,2,6), (2,3,1), (0,3,5)

    Step │ Pop        │ Action                    │ MST edges    │ Cost
    ─────┼────────────┼───────────────────────────┼──────────────┼──────
    1    │ (0, node0) │ Visit 0, push (4,1)(2,2)(5,3) │            │ 0
    2    │ (2, node2) │ Visit 2, push (6,1)(1,3)      │ 0─2 (w=2)  │ 2
    3    │ (1, node3) │ Visit 3                        │ 2─3 (w=1)  │ 3
    4    │ (4, node1) │ Visit 1                        │ 0─1 (w=4)  │ 7
    DONE │            │ All visited                    │             │ 7

    MST: 0──2──3, 0──1  │  Total cost = 2 + 1 + 4 = 7

COMPLEXITY:
    Time:  O((V + E) log V) — each edge pushed/popped from heap
    Space: O(V + E)
"""

import heapq


# ══════════════════════════════════════════════════════════════════════════════
# PRIM'S ALGORITHM — Adjacency List + Min-Heap
# ══════════════════════════════════════════════════════════════════════════════
def prim(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, 0)]  # (edge_weight, node) — start from node 0
    total_cost = 0
    edges_used = 0

    while min_heap and edges_used < n:
        cost, node = heapq.heappop(min_heap)

        if visited[node]:  # Already in MST — skip (same trick as Dijkstra stale check)
            continue

        visited[node] = True
        total_cost += cost
        edges_used += 1

        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight, neighbor))

    return total_cost


# ── Example ──
graph_adj = [
    [(1, 4), (2, 2), (3, 5)],  # 0: connects to 1(w=4), 2(w=2), 3(w=5)
    [(0, 4), (2, 6)],           # 1: connects to 0(w=4), 2(w=6)
    [(0, 2), (1, 6), (3, 1)],  # 2: connects to 0(w=2), 1(w=6), 3(w=1)
    [(0, 5), (2, 1)]            # 3: connects to 0(w=5), 2(w=1)
]

print("Prim's MST cost:", prim(graph_adj))  # Output: 7 (edges: 0-2=2, 2-3=1, 0-1=4)


"""
================================================================================
================================================================================
PART 2: KRUSKAL'S ALGORITHM
================================================================================
================================================================================

SUMMARY: "Sort all edges by weight. Pick edges smallest-first. Skip if it creates a cycle."

WHY UNION-FIND IS NEEDED:
    "Does adding this edge create a cycle?" = "Are both endpoints already connected?"
    Union-Find answers this in nearly O(1) per query.

ALGORITHM IN 3 STEPS:
    Step 1: Sort all edges by weight (ascending)
    Step 2: For each edge (u, v, w): if u and v are in DIFFERENT components → take it
    Step 3: Stop when you have V-1 edges

    "How to check different components?" → Union-Find (Disjoint Set Union / DSU)

UNION-FIND CRASH COURSE (3 operations):
    find(x):    What component does x belong to? (follow parent until root)
    union(x,y): Merge the components of x and y
    connected(x,y): Are x and y in the same component? (find(x) == find(y))

    TWO OPTIMIZATIONS (always use both):
    • Path compression: point every node directly to root during find()
    • Union by rank: attach shorter tree under taller tree

    With both: nearly O(1) per operation (amortized O(α(n)) ≈ constant)

VISUAL WALKTHROUGH:
    Edges sorted: (2,3,1), (0,2,2), (0,1,4), (0,3,5), (1,2,6)

    Step │ Edge      │ Same component? │ Action      │ MST edges
    ─────┼───────────┼─────────────────┼─────────────┼──────────────
    1    │ (2,3, w=1)│ No              │ union(2,3)  │ {2-3}
    2    │ (0,2, w=2)│ No              │ union(0,2)  │ {2-3, 0-2}
    3    │ (0,1, w=4)│ No              │ union(0,1)  │ {2-3, 0-2, 0-1}
    STOP │ 3 edges = V-1 = done        │             │ Total = 7
    ─────┼───────────┼─────────────────┼─────────────┼──────────────
    skip │ (0,3, w=5)│ YES (0,3 same)  │ skip        │
    skip │ (1,2, w=6)│ YES (1,2 same)  │ skip        │

COMPLEXITY:
    Time:  O(E log E) — dominated by sorting (Union-Find is nearly O(1))
    Space: O(V) — parent and rank arrays

================================================================================
FAANG INTERVIEW TIPS FOR MST:
================================================================================

    TIP 1: "Prim's vs Kruskal's?" →
            Dense graph (E ≈ V²): Prim's with adjacency list + heap
            Sparse graph (E ≈ V): Kruskal's with edge list + sort
            If given edge list directly → Kruskal's is natural choice

    TIP 2: Prim's code is almost identical to Dijkstra. If you know Dijkstra,
            change dist[neighbor] = dist[node] + weight → just push (weight, neighbor).

    TIP 3: If interview asks "return MST EDGES (not just cost)" →
            Prim's: track parent of each node when pushing to heap
            Kruskal's: collect edges as you union them (easier)

    TIP 4: "What if graph is disconnected?" →
            MST doesn't exist. You get a Minimum Spanning FOREST.
            Detect: if edges_used < V after Prim's → disconnected.

    TIP 5: Union-Find is useful BEYOND MST:
            - Number of connected components
            - Detect cycle in undirected graph
            - Accounts merge problem
            - "Are X and Y in the same group?"

    TIP 6: LeetCode problems using MST:
            • Min Cost to Connect All Points (LC 1584) → Kruskal's or Prim's
            • Connecting Cities With Min Cost (LC 1135) → Kruskal's
            • Optimize Water Distribution (LC 1168) → MST with virtual node
            • Redundant Connection (LC 684) → Union-Find (cycle detection)

    TIP 7: If all edge weights are DISTINCT → MST is UNIQUE.
            If some weights are equal → multiple valid MSTs may exist.

================================================================================
"""


# ══════════════════════════════════════════════════════════════════════════════
# UNION-FIND (Disjoint Set Union) — needed for Kruskal's
# ══════════════════════════════════════════════════════════════════════════════
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already connected — adding edge would create cycle
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px  # Union by rank
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


# ══════════════════════════════════════════════════════════════════════════════
# KRUSKAL'S ALGORITHM — Edge List + Union-Find
# ══════════════════════════════════════════════════════════════════════════════
def kruskal(n, edges):
    """edges = [(u, v, weight), ...]"""
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(n)
    total_cost = 0
    edges_used = 0

    for u, v, w in edges:
        if uf.union(u, v):  # Different components → take this edge
            total_cost += w
            edges_used += 1
            if edges_used == n - 1:  # MST complete
                break

    return total_cost if edges_used == n - 1 else -1  # -1 if disconnected


# ── Example ──
edges_list = [
    (0, 1, 4),
    (0, 2, 2),
    (0, 3, 5),
    (1, 2, 6),
    (2, 3, 1)
]

print("Kruskal's MST cost:", kruskal(4, edges_list))  # Output: 7


"""
================================================================================
BONUS: LeetCode 1584 — Min Cost to Connect All Points (Classic MST)
================================================================================

    Given n points, connect ALL with minimum total Manhattan distance.
    Every pair of points has an implicit edge → complete graph → E = V²/2
    Dense graph → Prim's is ideal here.
"""


def minCostConnectPoints(points):
    n = len(points)
    visited = [False] * n
    min_heap = [(0, 0)]  # Start from point 0
    total_cost = 0
    edges_used = 0

    while min_heap and edges_used < n:
        cost, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        total_cost += cost
        edges_used += 1

        for next_node in range(n):
            if not visited[next_node]:
                # Manhattan distance as edge weight
                dist = abs(points[node][0] - points[next_node][0]) + \
                       abs(points[node][1] - points[next_node][1])
                heapq.heappush(min_heap, (dist, next_node))

    return total_cost


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print("LC 1584 Min Cost:", minCostConnectPoints(points))  # Output: 20


"""
================================================================================
QUICK REVISION CHEAT SHEET (2 min before interview):
================================================================================

    MST = connect ALL nodes, minimum total weight, no cycles, exactly V-1 edges.

    PRIM'S (grow one tree):
        visited[] + min_heap[(weight, node)]
        Pop cheapest → mark visited → push neighbor edges
        Like Dijkstra but push EDGE WEIGHT not total distance
        O((V+E) log V)

    KRUSKAL'S (pick cheapest edges):
        Sort edges → for each: if union(u,v) succeeds → take it
        Stop at V-1 edges
        O(E log E)

    UNION-FIND template:
        find(x): path compression → parent[x] = find(parent[x])
        union(x,y): by rank, return False if same component

    Decision: Dense → Prim's. Sparse / edge list given → Kruskal's.

    Common mistake: Forgetting the "if visited[node]: continue" in Prim's
                    (same as stale-entry skip in Dijkstra)
================================================================================
"""
