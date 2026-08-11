"""
================================================================================
BRIDGES & ARTICULATION POINTS — Tarjan's Algorithm (FAANG Interview Guide)
================================================================================

PATTERN: DFS + disc[] + low[] (Tarjan's)
DIFFICULTY: Hard
FREQUENCY: High (Google, Amazon, Facebook — LC 1192 Critical Connections)

================================================================================
WHAT IS A BRIDGE? (remember this ONE image forever)
================================================================================

    A bridge is an edge that, if removed, SPLITS the graph into 2 pieces.

    Think of it like a real bridge between two islands:

        Island A ════BRIDGE════ Island B

        Remove the bridge → islands are disconnected. No other way across.

    Example:
        0 ── 1 ── 3          Remove 1-3 → node 3 is stranded
        |   /                  → (1,3) IS a bridge
        2
                              Remove 0-1 → still connected via 0→2→1
                               → (0,1) is NOT a bridge (has alternate route)

    RULE: An edge is a bridge if there's NO alternative path around it.

================================================================================
TWO ARRAYS — THE ONLY THINGS YOU NEED TO MEMORIZE:
================================================================================

    disc[node] = "WHEN did DFS first discover this node?" (timestamp)
    low[node]  = "What's the EARLIEST ancestor this node can reach via back edges?"

    That's it. Two arrays. The entire algorithm is just updating these.

    MEMORY TRICK:
        disc = "discovery TIME"    (a clock that ticks: 0, 1, 2, 3...)
        low  = "how LOW can I go?" (lowest/earliest ancestor reachable)

================================================================================
WHAT IS A BACK EDGE? (the key to understanding low[])
================================================================================

    DFS tree:          Actual graph:
        0                 0 ── 1
        |                 |   /
        1                  2
        |
        2

    DFS visits: 0 → 1 → 2
    Then 2 sees neighbor 0 (already visited, not parent) → that's a BACK EDGE.

    Back edge = an edge from a node to an ANCESTOR in the DFS tree.
    It means: "There's a cycle! I can reach back up to an older node."

    If a subtree has a back edge to an ancestor → it has an ALTERNATE route
    → removing any single edge in that cycle WON'T disconnect the graph
    → those edges are NOT bridges.

================================================================================
THE BRIDGE CONDITION — ONE LINE TO REMEMBER:
================================================================================

    low[child] > disc[parent]  →  (parent, child) IS A BRIDGE

    WHY?
    ├── low[child] = earliest ancestor the child's subtree can reach
    ├── disc[parent] = when parent was discovered
    ├── If low[child] > disc[parent]:
    │     The child's ENTIRE subtree cannot reach parent or anything above it
    │     through any back edge → removing parent-child disconnects the subtree
    │     → IT'S A BRIDGE
    └── If low[child] ≤ disc[parent]:
          The child can reach parent (or higher) via another route
          → removing parent-child does NOT disconnect → NOT a bridge

    ANALOGY: "Can my child find its way back to me (or my ancestors) without
             using our direct edge? If NO → bridge. If YES → not a bridge."

================================================================================
ALGORITHM — 5 STEPS:
================================================================================

    Step 1: Initialize disc[] = [-1]*n, low[] = [-1]*n, timer = 0
    Step 2: DFS from any node
    Step 3: For each node visited:
                disc[node] = low[node] = timer++
    Step 4: For each neighbor:
                If unvisited  → recurse, then low[node] = min(low[node], low[child])
                If visited & not parent → low[node] = min(low[node], disc[neighbor])
    Step 5: After recursing child: if low[child] > disc[node] → BRIDGE found

    PSEUDOCODE:
        dfs(node, parent):
            disc[node] = low[node] = timer++
            for neighbor in graph[node]:
                if not visited(neighbor):
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])    ← propagate up
                    if low[neighbor] > disc[node]:               ← BRIDGE CHECK
                        bridges.append((node, neighbor))
                elif neighbor != parent:
                    low[node] = min(low[node], disc[neighbor])   ← back edge

================================================================================
VISUAL WALKTHROUGH — LeetCode 1192 Example:
================================================================================

    n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]

    Graph:
        0 ── 1 ── 3
        |   /
        2

    ── DFS from node 0 (parent = -1) ─────────────────────────────────

    Visit 0: disc[0]=0, low[0]=0, timer=1

        │ Neighbor 1: unvisited → recurse
        │
        ├── Visit 1: disc[1]=1, low[1]=1, timer=2
        │       │
        │       │ Neighbor 2: unvisited → recurse
        │       │
        │       ├── Visit 2: disc[2]=2, low[2]=2, timer=3
        │       │       │
        │       │       │ Neighbor 0: visited & not parent(1)
        │       │       │   → back edge! low[2] = min(2, disc[0]) = min(2,0) = 0
        │       │       │
        │       │       └── Return to 1
        │       │
        │       │ Back from 2: low[1] = min(low[1], low[2]) = min(1, 0) = 0
        │       │ Bridge check: low[2]=0 > disc[1]=1? → 0 > 1? NO → not bridge ✓
        │       │
        │       │ Neighbor 3: unvisited → recurse
        │       │
        │       ├── Visit 3: disc[3]=3, low[3]=3, timer=4
        │       │       │
        │       │       │ No unvisited neighbors, no back edges
        │       │       │
        │       │       └── Return to 1
        │       │
        │       │ Back from 3: low[1] = min(low[1], low[3]) = min(0, 3) = 0
        │       │ Bridge check: low[3]=3 > disc[1]=1? → 3 > 1? YES → (1,3) IS BRIDGE ✓
        │       │
        │       └── Return to 0
        │
        │ Back from 1: low[0] = min(low[0], low[1]) = min(0, 0) = 0
        │ Bridge check: low[1]=0 > disc[0]=0? → 0 > 0? NO → not bridge ✓

    ── RESULTS ────────────────────────────────────────────────────────

    disc[] = [0, 1, 2, 3]      (discovery timestamps)
    low[]  = [0, 0, 0, 3]      (earliest reachable ancestor)

    Node │ disc │ low │ Why low has this value
    ─────┼──────┼─────┼────────────────────────────────────
      0  │  0   │  0  │ It's the root, can reach itself
      1  │  1   │  0  │ Child 2 has back edge to 0 → propagated up
      2  │  2   │  0  │ Has back edge directly to 0 (disc[0]=0)
      3  │  3   │  3  │ No back edges, stuck at its own discovery time

    Bridge check for each edge:
        (0,1): low[1]=0 > disc[0]=0? → NO  → not bridge (cycle 0-1-2-0)
        (1,2): low[2]=0 > disc[1]=1? → NO  → not bridge (cycle 0-1-2-0)
        (1,3): low[3]=3 > disc[1]=1? → YES → BRIDGE! ✓

    ANSWER: [[1, 3]]

================================================================================
WHY low[node] = min(low[node], disc[neighbor]) FOR BACK EDGES
AND NOT low[neighbor]?
================================================================================

    For back edges we use disc[neighbor] (not low[neighbor]).

    WHY? Because a back edge goes to an ALREADY VISITED ancestor.
    We know we can reach that ancestor directly. disc[neighbor] is its timestamp.

    For tree edges (child returns from recursion) we use low[child]
    because whatever the child can reach, we can reach too (through the child).

    SUMMARY:
        Back edge to ancestor   → use disc[ancestor]  (direct connection)
        Tree edge to child      → use low[child]      (inherit child's reachability)

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(V + E) — standard DFS, visits every node and edge once
    Space: O(V) — disc[], low[], recursion stack

================================================================================
FAANG INTERVIEW TIPS:
================================================================================

    TIP 1: Bridge condition: low[child] > disc[parent]
            Articulation point:  low[child] >= disc[parent] (≥ not >)
            The ONLY difference is > vs >=. Mention this to impress.

    TIP 2: "Why not just remove each edge and check connectivity?"
            → That's O(E × (V+E)) brute force. Tarjan's is O(V+E). Much faster.

    TIP 3: For undirected graphs, track parent to avoid treating the edge
            you came from as a back edge. neighbor != parent is critical.

    TIP 4: If graph has parallel edges (multiple edges between same nodes),
            track parent by EDGE INDEX instead of node, or use a count.

    TIP 5: Common follow-up: "Find articulation POINTS (not edges)"
            → Same algorithm, change condition to low[child] >= disc[node]
            → Special case: root is articulation point if it has 2+ children in DFS tree

    TIP 6: LC 1192 (Critical Connections) is the only direct bridge problem,
            but the disc[]/low[] pattern appears in:
            → Strongly Connected Components (Tarjan's SCC)
            → Biconnected Components
            → 2-Edge-Connected Components

    TIP 7: If recursion depth worries you (V up to 10⁵), mention you could
            convert to iterative DFS with an explicit stack. But recursive passes on LC.

================================================================================
"""

from collections import defaultdict


# ══════════════════════════════════════════════════════════════════════════════
# LeetCode 1192 — Critical Connections in a Network
# ══════════════════════════════════════════════════════════════════════════════
def criticalConnections(n, connections):
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    bridges = []
    timer = [0]  # List so inner function can modify it

    def dfs(node, parent):
        disc[node] = low[node] = timer[0]
        timer[0] += 1

        for neighbor in graph[node]:
            if disc[neighbor] == -1:        # Unvisited → tree edge
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])   # Propagate child's reach
                if low[neighbor] > disc[node]:              # BRIDGE CHECK
                    bridges.append([node, neighbor])
            elif neighbor != parent:        # Visited & not parent → back edge
                low[node] = min(low[node], disc[neighbor])

    dfs(0, -1)
    return bridges


# ── Example 1: LC 1192 ──
connections1 = [[0, 1], [1, 2], [2, 0], [1, 3]]
print("Bridges:", criticalConnections(4, connections1))  # [[1, 3]]

# ── Example 2: No bridges (complete cycle) ──
connections2 = [[0, 1], [1, 2], [2, 0]]
print("Bridges:", criticalConnections(3, connections2))  # []

# ── Example 3: Multiple bridges ──
#   0 ── 1 ── 2 ── 3 ── 4
connections3 = [[0, 1], [1, 2], [2, 3], [3, 4]]
print("Bridges:", criticalConnections(5, connections3))  # All edges are bridges


# ══════════════════════════════════════════════════════════════════════════════
# BONUS: ARTICULATION POINTS (same algo, >= instead of >)
# ══════════════════════════════════════════════════════════════════════════════
def articulationPoints(n, connections):
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    ap = set()
    timer = [0]

    def dfs(node, parent):
        disc[node] = low[node] = timer[0]
        timer[0] += 1
        children = 0

        for neighbor in graph[node]:
            if disc[neighbor] == -1:
                children += 1
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])

                if parent == -1 and children > 1:       # Root with 2+ children
                    ap.add(node)
                elif parent != -1 and low[neighbor] >= disc[node]:  # >= not >
                    ap.add(node)

            elif neighbor != parent:
                low[node] = min(low[node], disc[neighbor])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
    return list(ap)


# ── Example: node 1 is articulation point ──
#   0 ── 1 ── 3
#   |   /
#   2
print("Articulation Points:", articulationPoints(4, connections1))  # [1]


"""
================================================================================
QUICK REVISION CHEAT SHEET (2 min before interview):
================================================================================

    Two arrays:
        disc[node] = when DFS discovered this node (timestamp)
        low[node]  = earliest ancestor reachable from this node's subtree

    Updating low[]:
        Tree edge (unvisited child):  low[node] = min(low[node], low[child])
        Back edge (visited ancestor): low[node] = min(low[node], disc[ancestor])

    Bridge:             low[child] >  disc[parent]   (strictly greater)
    Articulation Point: low[child] >= disc[parent]   (greater or equal)
                        + root is AP if it has 2+ DFS children

    Template:
        dfs(node, parent):
            disc[node] = low[node] = timer++
            for neighbor:
                if unvisited: recurse → update low → check bridge
                elif not parent: update low (back edge)

    Time: O(V+E)  Space: O(V)

    THE ANALOGY: "Can my child's subtree find a way back to me (or above me)
                  without our direct edge? If NO → bridge. If YES → safe."
================================================================================
"""
