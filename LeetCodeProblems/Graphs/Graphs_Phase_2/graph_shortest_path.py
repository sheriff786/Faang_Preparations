"""
================================================================================
GRAPH SHORTEST PATH — Complete FAANG Interview Guide
================================================================================

DECISION FRAMEWORK (memorize this table — interviewers LOVE asking "which algo?"):

    ┌──────────────────────┬──────────────────────┬────────────────────────┐
    │ Graph Type           │ Algorithm            │ Time Complexity        │
    ├──────────────────────┼──────────────────────┼────────────────────────┤
    │ Unweighted           │ BFS                  │ O(V + E)               │
    │ Weighted (positive)  │ Dijkstra             │ O((V+E) log V)         │
    │ Weighted (negative)  │ Bellman-Ford          │ O(V * E)               │
    │ Negative cycles      │ Bellman-Ford (detect) │ O(V * E)               │
    │ All pairs            │ Floyd-Warshall       │ O(V³)                  │
    └──────────────────────┴──────────────────────┴────────────────────────┘

    QUICK RULE: "No weights? BFS. Positive weights? Dijkstra. Negative? Bellman-Ford."

================================================================================
PART 1: BFS SHORTEST PATH (Unweighted Graphs)
================================================================================

WHY BFS WORKS FOR SHORTEST PATH:
    BFS explores level by level → distance 0, then 1, then 2, ...
    The FIRST time BFS reaches a node IS the shortest distance.
    Think of it like dropping a stone in water — ripples expand equally in all directions.

WHY DFS CANNOT DO THIS:
    DFS dives deep first → might find a path of length 10 before finding one of length 2.
    DFS explores ONE direction fully, not all directions equally.

TEMPLATE (3 lines of core logic):
    dist[src] = 0
    for each neighbor: dist[neighbor] = dist[node] + 1
    return dist

    That's it. Everything else is just BFS boilerplate.

INTERVIEW TIP: If all edges have weight 1 (or equal weight), BFS is OPTIMAL.
              Don't use Dijkstra — it's overkill and shows you don't understand the tradeoff.
"""

from collections import deque

def shortest_path_unweighted(graph, src):
    n = len(graph)
    dist = [float('inf')] * n
    visited = [False] * n
    q = deque()

    q.append(src)
    visited[src] = True
    dist[src] = 0

    while q:
        node = q.popleft()
        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = True
                dist[nei] = dist[node] + 1  # Every edge = +1
                q.append(nei)

    return dist


graph_unweighted = [
    [1, 2],      # 0
    [0, 3, 4],   # 1
    [0, 5],      # 2
    [1],         # 3
    [1, 5],      # 4
    [2, 4]       # 5
]

print("BFS shortest:", shortest_path_unweighted(graph_unweighted, 0))
# Output: [0, 1, 1, 2, 2, 2]
# Node 0→0: 0, 0→1: 1 hop, 0→2: 1 hop, 0→3: 2 hops, 0→4: 2 hops, 0→5: 2 hops


"""
================================================================================
PART 2: DIJKSTRA'S ALGORITHM (Positive Weighted Graphs)
================================================================================

ONE-LINE SUMMARY:
    "BFS with a priority queue instead of a regular queue, picking cheapest node first."

WHY BFS FAILS ON WEIGHTED GRAPHS:
    BFS says: "1 hop = closest"  → WRONG when edges have different weights.
    Example: 0→1 (weight 10), 0→2 (weight 1), 2→1 (weight 2)
    BFS finds 0→1 = 1 hop. But 0→2→1 = 3 cost, which is CHEAPER.

THE KEY INSIGHT — RELAXATION (this is the HEART of Dijkstra):
    "Can I reach this neighbor CHEAPER through the current node?"

    if dist[node] + weight < dist[neighbor]:
        dist[neighbor] = dist[node] + weight

    This ONE line is what makes Dijkstra work. Everything else is scaffolding.

WHY MIN-HEAP (not just a queue)?
    We always want to process the CHEAPEST unfinished node first.
    Why? Because once we pop a node from the min-heap, its shortest distance is FINAL.
    This is the GREEDY property — processing cheapest first guarantees optimality.

WHY "if curr_dist > dist[node]: continue" (THE STALE ENTRY TRICK)?
    We might push (dist=5, node=3) and later push (dist=3, node=3).
    When we pop (dist=5, node=3), node 3 already has dist=3 → skip it.
    This avoids reprocessing and keeps time complexity correct.
    INTERVIEW TIP: Forgetting this line still gives correct answers but O(V*E) time.

ALGORITHM IN 4 STEPS:
    1. dist = [inf] * n, dist[src] = 0, push (0, src) into min-heap
    2. Pop cheapest (curr_dist, node) — skip if stale
    3. For each neighbor: RELAX → if cheaper, update dist and push to heap
    4. Return dist array

VISUAL WALKTHROUGH:
        (4)
     0 ─────── 1
     │       ╱  │
  (1)│    (2)   │(1)
     │  ╱       │
     2 ─────── 3
        (5)

    Step  │ Pop         │ Relax                  │ dist[]          │ Heap
    ──────┼─────────────┼────────────────────────┼─────────────────┼──────────────────
    init  │             │                        │ [0, ∞, ∞, ∞]   │ [(0,0)]
    1     │ (0, 0)      │ 0→1: 0+4=4, 0→2: 0+1=1│ [0, 4, 1, ∞]   │ [(1,2), (4,1)]
    2     │ (1, 2)      │ 2→1: 1+2=3✓, 2→3: 1+5=6│ [0, 3, 1, 6]  │ [(3,1), (4,1), (6,3)]
    3     │ (3, 1)      │ 1→3: 3+1=4✓            │ [0, 3, 1, 4]   │ [(4,1), (4,3), (6,3)]
    4     │ (4, 1) STALE│ skip (3 < 4)           │ [0, 3, 1, 4]   │ [(4,3), (6,3)]
    5     │ (4, 3)      │ no improvement         │ [0, 3, 1, 4]   │ [(6,3)]
    6     │ (6, 3) STALE│ skip (4 < 6)           │ [0, 3, 1, 4]   │ []
    DONE! │             │                        │ [0, 3, 1, 4]   │

    Shortest paths: 0→0=0, 0→1=3 (via 2), 0→2=1, 0→3=4 (via 2→1)

COMPLEXITY:
    Time:  O((V + E) log V) — each push/pop is O(log V), at most E pushes
    Space: O(V + E)

================================================================================
FAANG INTERVIEW TIPS FOR DIJKSTRA:
================================================================================

    TIP 1: "Why not BFS?" → Because edges have different weights. BFS assumes equal cost.

    TIP 2: "Why not DFS?" → DFS explores one path fully. Greedy min-heap guarantees
            we always extend the globally cheapest partial path.

    TIP 3: "Why does Dijkstra fail with negative weights?"
            → Dijkstra's greedy assumption: "once popped, distance is final."
            → Negative edge AFTER a popped node can make a cheaper path retroactively.
            → Example: A→B=1, A→C=5, C→B=-10. Dijkstra pops B with dist=1.
              But A→C→B = 5+(-10) = -5 < 1. Too late — B is already finalized. WRONG.

    TIP 4: Always use (distance, node) tuple in heap — distance FIRST so heap sorts by cost.

    TIP 5: If asked to find shortest path (not just distance), add a parent[] array:
            parent[neighbor] = node during relaxation, then backtrack from target to source.

    TIP 6: If edges are 0 or 1 weight only → use 0-1 BFS (deque trick) instead of Dijkstra.
            appendleft for 0-weight, append for 1-weight. O(V+E) instead of O((V+E)logV).
"""

import heapq

graph_weighted = [
    [(1, 4), (2, 1)],          # 0
    [(0, 4), (2, 2), (3, 1)],  # 1
    [(0, 1), (1, 2), (3, 5)],  # 2
    [(1, 1), (2, 5)]           # 3
]


class Solution:

    def dijkstra(self, graph, src):
        n = len(graph)
        dist = [float('inf')] * n
        dist[src] = 0
        min_heap = [(0, src)]  # (distance, node)

        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)

            if curr_dist > dist[node]:  # Stale entry — skip
                continue

            for neighbor, weight in graph[node]:
                new_dist = dist[node] + weight
                if new_dist < dist[neighbor]:       # RELAXATION — the heart of Dijkstra
                    dist[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))

        return dist


obj = Solution()
print("Dijkstra:", obj.dijkstra(graph_weighted, 0))
# Output: [0, 3, 1, 4]


"""
================================================================================
QUICK REVISION CHEAT SHEET (read 2 min before interview):
================================================================================

    BFS (unweighted):
        dist[src]=0 → pop node → dist[nei] = dist[node]+1 → push nei
        O(V+E). Use when all edges equal weight.

    Dijkstra (positive weights):
        dist[src]=0 → pop CHEAPEST → relax: if dist[node]+w < dist[nei] update → push
        O((V+E) log V). Skip stale entries. NEVER use with negative weights.

    When interviewer asks "which algorithm?":
        No weights / equal weights  → BFS
        Positive weights            → Dijkstra
        Negative weights            → Bellman-Ford
        "Shortest with K stops"     → Modified BFS/Dijkstra with state (dist, node, stops)

    Common mistakes to avoid:
        ✗ Using DFS for shortest path
        ✗ Forgetting the stale-entry check in Dijkstra
        ✗ Using Dijkstra with negative weights
        ✗ Putting (node, distance) instead of (distance, node) in heap

================================================================================
MUST-SOLVE LEETCODE PROBLEMS (in order):
================================================================================

    1. Network Delay Time (743)              → Basic Dijkstra (warm-up)
    2. Path With Minimum Effort (1631)       → Modified Dijkstra (max edge on path)
    3. Cheapest Flights Within K Stops (787) → Dijkstra + extra state (stops left)
    4. Swim in Rising Water (778)            → Modified Dijkstra (minimax path)
    5. Shortest Path in Binary Matrix (1091) → BFS (unweighted grid)
    6. 01 Matrix (542)                       → Multi-source BFS
"""


#Part 3 bellman Ford

"""
================================================================================
PART 3: BELLMAN-FORD ALGORITHM (Handles Negative Weights + Detects Negative Cycles)
================================================================================

ONE-LINE SUMMARY:
    "Relax ALL edges V-1 times. If V-th pass still relaxes → negative cycle."

================================================================================
WHY BELLMAN-FORD EXISTS (when to pick it over Dijkstra):
================================================================================

    Dijkstra BREAKS with negative edges (greedy assumption fails).
    Bellman-Ford is NOT greedy — it brute-forces relaxation until stable.

    USE BELLMAN-FORD WHEN:
        ✓ Graph has negative edge weights
        ✓ Need to DETECT negative cycles
        ✓ "Shortest path with at most K edges" (just run K iterations instead of V-1)

    USE DIJKSTRA INSTEAD WHEN:
        ✓ All weights are non-negative (Dijkstra is faster: O((V+E)logV) vs O(V*E))

================================================================================
THE KEY INSIGHT — WHY V-1 ITERATIONS?
================================================================================

    In a graph with V nodes, the longest shortest path has AT MOST V-1 edges.
    (More edges = you revisited a node = not shortest)

    Each iteration guarantees at least ONE more node gets its correct distance.

    Iteration 1: Nodes 1 edge away from source get correct dist
    Iteration 2: Nodes 2 edges away get correct dist
    ...
    Iteration V-1: Nodes V-1 edges away get correct dist → ALL nodes done.

    ANALOGY: "Information propagates one hop per iteration, like a wave."

================================================================================
NEGATIVE CYCLE DETECTION — WHY THE V-TH PASS WORKS:
================================================================================

    After V-1 passes, all shortest paths are finalized (if no negative cycle).
    If the V-th pass STILL finds a shorter path → distances keep decreasing infinitely
    → NEGATIVE CYCLE exists.

    Example of negative cycle: A→B=1, B→C=2, C→A=-5
    Going around: 1+2+(-5) = -2 → each loop reduces total by 2 → infinite reduction.

================================================================================
ALGORITHM IN 3 STEPS (memorize this):
================================================================================

    Step 1: dist = [inf]*V, dist[src] = 0
    Step 2: Repeat V-1 times → for every edge (u,v,w): if dist[u]+w < dist[v] → update
    Step 3: One more pass → if any edge still relaxes → NEGATIVE CYCLE

    That's it. No heap, no visited set, no adjacency list needed.
    Input is just an EDGE LIST — simpler data structure than Dijkstra.

================================================================================
VISUAL WALKTHROUGH:
================================================================================

    Edges: (0→1, w=4), (0→2, w=5), (1→3, w=3), (2→3, w=-2)
    V=4, src=0

    Initial:     dist = [0, ∞, ∞, ∞]

    Iteration 1: Process all edges
        (0,1,4): dist[0]+4=4 < ∞   → dist[1]=4     dist = [0, 4, ∞, ∞]
        (0,2,5): dist[0]+5=5 < ∞   → dist[2]=5     dist = [0, 4, 5, ∞]
        (1,3,3): dist[1]+3=7 < ∞   → dist[3]=7     dist = [0, 4, 5, 7]
        (2,3,-2): dist[2]+(-2)=3 < 7 → dist[3]=3   dist = [0, 4, 5, 3]

    Iteration 2: Process all edges again
        (0,1,4): 0+4=4, not < 4    → no change
        (0,2,5): 0+5=5, not < 5    → no change
        (1,3,3): 4+3=7, not < 3    → no change
        (2,3,-2): 5+(-2)=3, not < 3 → no change

    Iteration 3: Same — no changes. Already converged.

    V-th pass (cycle check): No edge relaxes → NO negative cycle ✓

    ANSWER: [0, 4, 5, 3]
    Path to node 3: 0→2→3 (cost 5 + (-2) = 3) — cheaper than 0→1→3 (cost 7)

================================================================================
COMPARISON TABLE (paste this in your brain):
================================================================================

    ┌─────────────────┬──────────────────────┬────────────────────────────────┐
    │                 │ Dijkstra             │ Bellman-Ford                   │
    ├─────────────────┼──────────────────────┼────────────────────────────────┤
    │ Approach        │ Greedy (min-heap)    │ Brute-force (relax all edges)  │
    │ Negative edges  │ ✗ FAILS              │ ✓ Works                        │
    │ Negative cycles │ ✗ Can't detect       │ ✓ Detects (V-th pass)          │
    │ Time            │ O((V+E) log V)       │ O(V * E)                       │
    │ Space           │ O(V + E)             │ O(V)                           │
    │ Graph format    │ Adjacency list       │ Edge list (simpler)            │
    │ When to use     │ Positive weights,    │ Negative weights,              │
    │                 │ need speed            │ cycle detection, K-edge limit  │
    └─────────────────┴──────────────────────┴────────────────────────────────┘

================================================================================
FAANG INTERVIEW TIPS FOR BELLMAN-FORD:
================================================================================

    TIP 1: "Why V-1 iterations?" → Longest possible shortest path = V-1 edges.
            Each iteration propagates correct distance one hop further.

    TIP 2: "Why check dist[u] != inf before relaxing?"
            → If source can't reach u, then u's outgoing edges are irrelevant.
            → Without this check, inf + negative_weight could give a wrong finite value.

    TIP 3: "Cheapest Flights Within K Stops" (LeetCode 787) →
            Run only K+1 iterations (not V-1). Use a COPY of dist each iteration
            to prevent using updates from the same iteration (chaining problem).

    TIP 4: If interviewer says "detect if negative cycle exists" → Bellman-Ford.
            If they say "find nodes AFFECTED by negative cycle" → run V-th pass,
            any node that gets relaxed (and nodes reachable from it) = affected.

    TIP 5: Bellman-Ford on UNDIRECTED graph with any negative edge = instant negative cycle.
            Because u→v and v→u with negative weight = you can bounce forever.
            So Bellman-Ford with negative weights only makes sense on DIRECTED graphs.

    TIP 6: Space optimization — you only need the dist array (no heap, no adjacency list).
            The edge list input is often given directly in the problem.

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(V * E) — V-1 iterations, each scanning all E edges
    Space: O(V) — just the distance array

    WHY SLOWER THAN DIJKSTRA: Dijkstra smartly picks cheapest node (skips many edges).
    Bellman-Ford blindly processes ALL edges every iteration — brute force but safe.

================================================================================
"""


class SolutionBellmanFord:

    def bellmanFord(self, V, edges, src):
        dist = [float('inf')] * V
        dist[src] = 0

        # Relax all edges V-1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # V-th pass: if any edge still relaxes → negative cycle
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return "Negative Cycle Detected"

        return dist


# ── Example: Directed graph with a negative edge ──
edges = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 3, 3),
    (2, 3, -2)   # Negative weight — Dijkstra would fail here
]

V = 4
src = 0

obj2 = SolutionBellmanFord()
print("Bellman-Ford:", obj2.bellmanFord(V, edges, src))
# Output: [0, 4, 5, 3]  (node 3 via 0→2→3 = 5+(-2) = 3, cheaper than 0→1→3 = 7)


"""
================================================================================
BONUS: LeetCode 787 — Cheapest Flights Within K Stops (Bellman-Ford variant)
================================================================================

    KEY MODIFICATION: Run K+1 iterations (not V-1) + use COPY of dist each iteration.

    Why copy? Without copy, relaxation chains within one iteration — you might use
    paths with MORE than K stops. Copy ensures each iteration adds exactly 1 edge.
"""


def findCheapestPrice(n, flights, src, dst, k):
    dist = [float('inf')] * n
    dist[src] = 0

    for _ in range(k + 1):  # K stops = K+1 edges
        prev = dist[:]      # COPY — prevents chaining within same iteration
        for u, v, w in flights:
            if prev[u] != float('inf') and prev[u] + w < dist[v]:
                dist[v] = prev[u] + w

    return dist[dst] if dist[dst] != float('inf') else -1


# Example: 3 cities, src=0, dst=2, at most 1 stop
flights = [(0, 1, 100), (1, 2, 100), (0, 2, 500)]
print("Cheapest with K=1 stop:", findCheapestPrice(3, flights, 0, 2, 1))
# Output: 200 (path: 0→1→2, cost 100+100)


"""
================================================================================
FINAL CHEAT SHEET — ALL 4 ALGORITHMS:
================================================================================

    BFS:            Queue    │ Unweighted       │ O(V+E)       │ Level-by-level
    Dijkstra:       Min-Heap │ Positive weights  │ O((V+E)logV) │ Greedy (cheapest first)
    Bellman-Ford:   Edge List│ Negative weights  │ O(V*E)       │ Brute-force V-1 passes
    Floyd-Warshall: Matrix   │ All-pairs         │ O(V³)        │ Try every intermediate

    "Which algorithm?" decision in 3 seconds:
        → Negative weights or cycle detection? → Bellman-Ford
        → Positive weights, single source?     → Dijkstra
        → All equal weights / unweighted?      → BFS
        → ALL pairs shortest path?             → Floyd-Warshall

    Bellman-Ford pattern:
        for V-1 times: for every edge: relax → one more pass → negative cycle check

    Floyd-Warshall pattern:
        for k: for i: for j: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
================================================================================
"""


"""
================================================================================
PART 4: FLOYD-WARSHALL ALGORITHM (All-Pairs Shortest Path)
================================================================================

ONE-LINE SUMMARY:
    "For every pair (i,j), try every node k as a middle-man. 3 nested loops. Done."

================================================================================
WHEN TO USE FLOYD-WARSHALL (vs running Dijkstra V times):
================================================================================

    USE FLOYD-WARSHALL WHEN:
        ✓ Need shortest path between EVERY pair of nodes
        ✓ Graph is SMALL (V ≤ 400-500, because O(V³))
        ✓ Graph has negative edges (Dijkstra can't handle this)
        ✓ Need to detect negative cycles (diagonal becomes negative)
        ✓ Graph given as adjacency MATRIX (natural input format)

    USE DIJKSTRA V TIMES INSTEAD WHEN:
        ✓ Graph is large + sparse + positive weights
        ✓ V × O((V+E)logV) < O(V³) when E is small

    FAANG RULE: If V ≤ 400 and problem says "all pairs" → Floyd-Warshall.
                If V > 1000 → probably Dijkstra from each source.

================================================================================
THE KEY INSIGHT — WHY IT WORKS (Dynamic Programming):
================================================================================

    Core idea: "Is it cheaper to go i→j directly, or i→k→j through some middle node k?"

    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    This ONE line is the entire algorithm. Everything else is just 3 for-loops.

    WHY k IS THE OUTER LOOP (interviewers ask this!):
        k = "which intermediate nodes am I ALLOWED to use?"
        After k=0: paths can use node 0 as intermediate
        After k=1: paths can use nodes {0,1} as intermediates
        After k=V-1: paths can use ALL nodes → final answer

        If you put k inside (wrong order), you're checking intermediates
        before their own distances are finalized → WRONG answers.

    ANALOGY: "Adding highways one by one. Each new highway (node k) might create
             shortcuts between cities that didn't have a direct route."

================================================================================
NEGATIVE CYCLE DETECTION WITH FLOYD-WARSHALL:
================================================================================

    After running the algorithm, check the diagonal:
        if dist[i][i] < 0 for any i → negative cycle exists through node i.

    Why? dist[i][i] starts at 0 (distance from node to itself).
    If it becomes negative → there's a cycle from i back to i with negative total weight.

================================================================================
VISUAL WALKTHROUGH:
================================================================================

    Graph (directed):
          3         2
    0 ────────→ 1 ────────→ 3
    │                        ↑
    │8                       │1
    ↓                        │
    2 ───────────────────────┘

    Initial Distance Matrix (adjacency matrix):
              0      1      2      3
        0  [  0,     3,     8,     ∞  ]
        1  [  ∞,     0,     ∞,     2  ]
        2  [  ∞,     ∞,     0,     1  ]
        3  [  ∞,     ∞,     ∞,     0  ]

    k=0 (try node 0 as intermediate):
        Can anyone reach someone cheaper via node 0?
        i=1,j=2: dist[1][0]+dist[0][2] = ∞+8 = ∞ → no improvement
        No changes. (Because no one can reach node 0 except node 0 itself)

    k=1 (try node 1 as intermediate):
        i=0,j=3: dist[0][1]+dist[1][3] = 3+2 = 5 < ∞ → dist[0][3] = 5 ✓
        Matrix now:
        0  [  0,     3,     8,     5  ]   ← 0→3 via node 1, cost 5
        1  [  ∞,     0,     ∞,     2  ]
        2  [  ∞,     ∞,     0,     1  ]
        3  [  ∞,     ∞,     ∞,     0  ]

    k=2 (try node 2 as intermediate):
        i=0,j=3: dist[0][2]+dist[2][3] = 8+1 = 9, not < 5 → no change
        No improvements.

    k=3 (try node 3 as intermediate):
        No outgoing edges from node 3 (all ∞) → no improvements.

    FINAL ANSWER:
              0      1      2      3
        0  [  0,     3,     8,     5  ]   ← from 0: to 1=3, to 2=8, to 3=5(via 1)
        1  [  ∞,     0,     ∞,     2  ]
        2  [  ∞,     ∞,     0,     1  ]
        3  [  ∞,     ∞,     ∞,     0  ]

================================================================================
ALGORITHM IN 3 LINES OF LOGIC (memorize this):
================================================================================

    for k in range(V):          # intermediate node
        for i in range(V):      # source
            for j in range(V):  # destination
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    That's it. The ENTIRE algorithm is 3 nested loops + 1 relaxation line.

================================================================================
FAANG INTERVIEW TIPS FOR FLOYD-WARSHALL:
================================================================================

    TIP 1: "Why k outer?" → k represents "allowed intermediates so far."
            Wrong loop order = using intermediate distances before they're computed.
            This is THE most common follow-up question.

    TIP 2: Don't forget: dist[i][i] = 0 (diagonal), dist[i][j] = weight or ∞.
            Copy the matrix before modifying (or modify in-place, both work here since
            dist[k][j] doesn't change when i≠k).

    TIP 3: Path reconstruction — maintain a next[i][j] matrix:
            next[i][j] = j initially (direct edge)
            When dist[i][k]+dist[k][j] < dist[i][j]: next[i][j] = next[i][k]
            To get path i→j: follow next[i][j] → next[next[i][j]][j] → ... → j

    TIP 4: "Find if graph has negative cycle?" → Run Floyd-Warshall, check if any
            dist[i][i] < 0. O(V³) but gives you ALL negative cycles at once.

    TIP 5: Space optimization: Floyd-Warshall works in-place on the input matrix.
            No extra space needed beyond the V×V matrix you already have.

    TIP 6: Common FAANG problems using this pattern:
            - "Find the city with smallest number of reachable neighbors" (LC 1334)
            - "Shortest path visiting all nodes" (LC 847, modified)
            - Any "all pairs" problem with small V

    TIP 7: Time limit check — V=400 → 400³ = 64 million operations ≈ OK.
            V=1000 → 10⁹ = TOO SLOW. Switch to Dijkstra from each source.

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(V³) — three nested loops over V
    Space: O(V²) — the distance matrix (can be in-place)

    COMPARISON:
        Floyd-Warshall: O(V³), simple, works with negative edges
        Dijkstra × V:  O(V(V+E)logV), faster for sparse graphs, positive only
        Bellman-Ford × V: O(V²E), slowest, but handles negative edges

================================================================================
"""

INF = float('inf')


class SolutionFloydWarshall:

    def floydWarshall(self, graph):
        V = len(graph)
        dist = [row[:] for row in graph]  # Copy — don't modify original

        for k in range(V):          # Intermediate
            for i in range(V):      # Source
                for j in range(V):  # Destination
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist

    def hasNegativeCycle(self, graph):
        dist = self.floydWarshall(graph)
        for i in range(len(dist)):
            if dist[i][i] < 0:
                return True
        return False


# ── Example ──
graph_matrix = [
    [0,   3,   8,   INF],
    [INF, 0,   INF, 2  ],
    [INF, INF, 0,   1  ],
    [INF, INF, INF, 0  ]
]

obj3 = SolutionFloydWarshall()
result = obj3.floydWarshall(graph_matrix)
print("\nFloyd-Warshall (all-pairs shortest paths):")
for row in result:
    print([x if x != INF else "∞" for x in row])
# Output:
# [0, 3, 8, 5]    ← from node 0
# [∞, 0, ∞, 2]    ← from node 1
# [∞, ∞, 0, 1]    ← from node 2
# [∞, ∞, ∞, 0]    ← from node 3


"""
================================================================================
COMPLETE REVISION — ALL 4 SHORTEST PATH ALGORITHMS IN ONE GLANCE:
================================================================================

    ┌────────────────┬────────────┬──────────────┬─────────┬───────────────────────┐
    │ Algorithm      │ Input      │ Output       │ Time    │ Remember              │
    ├────────────────┼────────────┼──────────────┼─────────┼───────────────────────┤
    │ BFS            │ 1 source   │ dist[] array │ O(V+E)  │ Queue + level by level│
    │ Dijkstra       │ 1 source   │ dist[] array │O((V+E)lgV)│ Min-heap + relax    │
    │ Bellman-Ford   │ 1 source   │ dist[] array │ O(VE)   │ V-1 passes over edges │
    │ Floyd-Warshall │ all sources│ dist[][] matrix│ O(V³) │ 3 loops: k, i, j      │
    └────────────────┴────────────┴──────────────┴─────────┴───────────────────────┘

    NEGATIVE EDGE SUPPORT:
        BFS: N/A (unweighted)  │  Dijkstra: ✗  │  Bellman-Ford: ✓  │  Floyd-Warshall: ✓

    NEGATIVE CYCLE DETECTION:
        Bellman-Ford: V-th pass relaxes → cycle
        Floyd-Warshall: dist[i][i] < 0 → cycle

    INTERVIEW DECISION TREE:
        "All pairs?"  →  YES → Floyd-Warshall (if V ≤ 400)
                      →  NO  → "Negative weights?" → YES → Bellman-Ford
                                                    → NO  → "Weighted?" → YES → Dijkstra
                                                                          → NO  → BFS
================================================================================
"""

'''
questions we will solve it

| #  | Problem                                                                                         | Main Pattern              |
| -- | ----------------------------------------------------------------------------------------------- | ------------------------- |
| 1  | **Network Delay Time — LeetCode 743**                                                           | Dijkstra                  |
| 2  | **Path With Minimum Effort — LeetCode 1631**                                                    | Modified Dijkstra         |
| 3  | **Cheapest Flights Within K Stops — LeetCode 787**                                              | Shortest Path + State     |
| 4  | **Shortest Path in Binary Matrix — LeetCode 1091**                                              | BFS                       |
| 5  | **Word Ladder — LeetCode 127**                                                                  | BFS + Implicit Graph      |
| 6  | **Minimum Cost to Make at Least One Valid Path in a Grid — LeetCode 1368**                      | 0-1 BFS                   |
| 7  | **Swim in Rising Water — LeetCode 778**                                                         | Modified Dijkstra         |
| 8  | **Shortest Path Visiting All Nodes — LeetCode 847**                                             | BFS + Bitmask             |
| 9  | **Number of Ways to Arrive at Destination — LeetCode 1976**                                     | Dijkstra + Counting       |
| 10 | **Find the City With the Smallest Number of Neighbors at a Threshold Distance — LeetCode 1334** | Floyd-Warshall / Dijkstra |


'''

'''

IK questions

| Phase                               | Problem                                          | Main Concept                       |
| ----------------------------------- | ------------------------------------------------ | ---------------------------------- |
| **Phase 3 — Topological Sort**      | **Complete All Courses With Dependencies**       | Topological Sort / Cycle Detection |
| **Phase 4 — Shortest Path**         | **Snakes and Ladders Matrix**                    | BFS Shortest Path                  |
| **Phase 4 — Shortest Path**         | **Shortest Path in 2D Grid With Keys and Doors** | BFS + State + Bitmask              |
| **Phase 6 — Advanced Connectivity** | **Critical Connections**                         | Bridges + DFS + Tarjan             |

'''


