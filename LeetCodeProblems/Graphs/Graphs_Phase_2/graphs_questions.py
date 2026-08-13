"""
================================================================================
LeetCode 787 — Cheapest Flights Within K Stops (FAANG Interview Guide)
================================================================================

PATTERN: Modified Bellman-Ford (limited iterations)
DIFFICULTY: Medium
FREQUENCY: Very High (Amazon, Google, Facebook, Microsoft)

================================================================================
PROBLEM IN 10 SECONDS:
================================================================================

    Find cheapest price from src → dst using AT MOST k stops.
    k stops = k+1 flights max.

    Think: booking a flight with layover limit.

================================================================================
ONE-LINE TRICK TO REMEMBER:
================================================================================

    "Bellman-Ford but only K+1 rounds, and use a COPY each round to prevent chaining."

================================================================================
WHY NOT DIJKSTRA? WHY NOT REGULAR BELLMAN-FORD?
================================================================================

    DIJKSTRA fails because:
        → Dijkstra finds cheapest path overall, but IGNORES the stop limit.
        → It might find 0→2→3→4→5 (cheapest but 4 stops) when k=1.
        → Modified Dijkstra with state (cost, node, stops) works but is complex.

    REGULAR BELLMAN-FORD fails because:
        → Standard Bellman-Ford runs V-1 rounds = allows unlimited stops.
        → We need EXACTLY K+1 rounds to limit to K stops.
        → AND we must use dist.copy() to prevent using multiple flights in one round.

    MODIFIED BELLMAN-FORD is perfect:
        → K+1 rounds = K+1 flights max = K stops max
        → temp = dist.copy() each round = prevents chaining (using 2+ flights per round)

================================================================================
EXAMPLE:
================================================================================

    n = 6 cities (0 to 5)
    src = 0, dst = 5, k = 1 (at most 1 stop → at most 2 flights)

    flights = [
        [0,1,100], [0,2,50],  [1,2,20],  [1,3,200],
        [2,3,100], [2,4,150], [3,4,50],  [3,5,100],
        [4,5,30],  [1,5,500], [0,5,1000]
    ]

    Graph:
                  100         200
        0 ──────────→ 1 ──────────→ 3
        │             │             │
        │50         20│500       100│50
        ↓             ↓             ↓
        2             5             4
        │                           │
     100│  150                   30│
        ↓                          ↓
        3             4 ──────────→ 5

================================================================================
FLIGHT COST TABLE (helps visualize all edges):
================================================================================

    From → To    Cost     Allowed with k=1?
    ─────────────────────────────────────────
    0  →  1      100      ✓ (1 flight)
    0  →  2       50      ✓ (1 flight)
    0  →  5     1000      ✓ (1 flight, direct)
    1  →  2       20      ✓ only if 0→1→2 (2 flights = 1 stop)
    1  →  3      200      ✓ only if 0→1→3
    1  →  5      500      ✓ only if 0→1→5
    2  →  3      100      ✓ only if 0→2→3
    2  →  4      150      ✓ only if 0→2→4
    3  →  4       50      ✗ needs 0→?→3→4 = 2 stops minimum
    3  →  5      100      ✗ needs 0→?→3→5 = 2 stops minimum
    4  →  5       30      ✗ needs 0→?→4→5 = 2 stops minimum

================================================================================
ALGORITHM — 4 STEPS (memorize this):
================================================================================

    Step 1: dist = [inf]*n, dist[src] = 0
    Step 2: Loop K+1 times (K stops = K+1 flights)
    Step 3: COPY dist into temp BEFORE processing (prevents chaining!)
    Step 4: For each flight (u,v,w): if dist[u]+w < temp[v] → update temp[v]
            Then dist = temp

    THE COPY IS THE KEY. Without it, one round could chain multiple flights.

================================================================================
WHY THE COPY? (THE #1 INTERVIEW QUESTION about this problem):
================================================================================

    WITHOUT copy (WRONG):
        Round 2 processes flight 0→2 (cost 50), updates dist[2]=50
        SAME round processes flight 2→3 (cost 100), sees dist[2]=50 (just updated!)
        Updates dist[3] = 50+100 = 150
        Then processes 3→5 (cost 100), sees dist[3]=150
        Updates dist[5] = 250

        Result: 0→2→3→5 = 250  ← used 3 flights in ONE round! WRONG for k=1.

    WITH copy (CORRECT):
        temp = dist.copy() at start of round
        Process flight 2→3: check dist[2] (from PREVIOUS round), not temp[2]
        If dist[2] was ∞ in previous round → skip. No chaining possible.

    ANALOGY: "Each round is a snapshot. You can only extend paths from the
             PREVIOUS snapshot, not from updates made in the CURRENT round."

================================================================================
STEP-BY-STEP TRACE:
================================================================================

    Initial: dist = [0, ∞, ∞, ∞, ∞, ∞]

    ── ROUND 1 (paths with 1 flight) ──────────────────────────────────
    prev = [0, ∞, ∞, ∞, ∞, ∞]  (copy of dist)

    Flight [0,1,100]: prev[0]+100 = 100 < ∞   → dist[1] = 100
    Flight [0,2,50]:  prev[0]+50  = 50  < ∞   → dist[2] = 50
    Flight [0,5,1000]:prev[0]+1000= 1000 < ∞  → dist[5] = 1000
    All other flights: source city has ∞ in prev → skip

    After Round 1: dist = [0, 100, 50, ∞, ∞, 1000]

    Meaning: With 1 flight from city 0:
        City 1 costs 100, City 2 costs 50, City 5 costs 1000

    ── ROUND 2 (paths with up to 2 flights = 1 stop) ─────────────────
    prev = [0, 100, 50, ∞, ∞, 1000]  (copy of dist)

    Flight [0,1,100]: 0+100=100, not < 100     → no change
    Flight [0,2,50]:  0+50=50, not < 50         → no change
    Flight [1,2,20]:  100+20=120, not < 50      → no change (direct 0→2 is cheaper)
    Flight [1,3,200]: 100+200=300 < ∞           → dist[3] = 300
    Flight [2,3,100]: 50+100=150 < 300          → dist[3] = 150 ✓ (0→2→3)
    Flight [2,4,150]: 50+150=200 < ∞            → dist[4] = 200
    Flight [1,5,500]: 100+500=600 < 1000        → dist[5] = 600 ✓ (0→1→5)
    Flight [3,4,50]:  prev[3]=∞ → SKIP          ← can't chain, 3 not reachable in 1 flight
    Flight [3,5,100]: prev[3]=∞ → SKIP          ← THIS is why copy matters!
    Flight [4,5,30]:  prev[4]=∞ → SKIP
    Flight [0,5,1000]:0+1000=1000, not < 600    → no change

    After Round 2: dist = [0, 100, 50, 150, 200, 600]

    DONE. k+1 = 2 rounds complete.

    ── ANSWER ─────────────────────────────────────────────────────────
    dist[dst] = dist[5] = 600
    Best route: 0 → 1 → 5 (cost: 100 + 500 = 600)

    ── WHY NOT 0→2→3→5 = 250? ────────────────────────────────────────
    That path uses 3 flights = 2 stops. But k=1, so only 1 stop allowed!
    The copy mechanism in Round 2 prevented 3→5 from being used (prev[3]=∞).

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(K * E) — K+1 rounds, each scans all E flights
    Space: O(V) — dist array + temp copy

    Much better than Dijkstra+state approach for this problem.

================================================================================
FAANG INTERVIEW TIPS:
================================================================================

    TIP 1: "Why Bellman-Ford and not Dijkstra?"
            → Bellman-Ford naturally limits rounds. K+1 rounds = K stops.
            → Dijkstra needs extra state (cost, node, stops_left) and is harder to code.

    TIP 2: The COPY is the most important line. Without it, answer is wrong.
            If interviewer asks "what happens without the copy?" → explain chaining bug.

    TIP 3: "K stops" vs "K flights" — be very careful!
            K stops = K+1 flights = K+1 Bellman-Ford rounds.
            Off-by-one here = wrong answer.

    TIP 4: Why check "prev[u] != inf" before relaxing?
            → If source u is unreachable, inf + w could chain wrongly.
            → Also prevents integer overflow in some languages.

    TIP 5: This problem can also be solved with BFS + state (cost, node, stops).
            But Bellman-Ford is cleaner, shorter, and harder to mess up.

    TIP 6: If k >= n-1, the stop limit doesn't matter → just run regular
            Bellman-Ford or Dijkstra for plain shortest path.

    TIP 7: Variations interviewers ask:
            → "Return the actual path" → track parent[v] = u during relaxation
            → "What if k=0?" → only direct flights, check if 0→5 edge exists
            → "What if no valid path?" → return -1 (dist[dst] is still inf)

================================================================================
"""


def findCheapestPrice(n, flights, src, dst, k):
    if src == dst:
        return 0

    dist = [float('inf')] * n
    dist[src] = 0

    for _ in range(k + 1):          # K stops = K+1 flights = K+1 rounds
        prev = dist[:]              # COPY — prevents chaining within same round
        for u, v, w in flights:
            if prev[u] != float('inf') and prev[u] + w < dist[v]:
                dist[v] = prev[u] + w

    return dist[dst] if dist[dst] != float('inf') else -1


# ── Example ──
flights = [
    [0, 1, 100], [0, 2, 50],  [1, 2, 20],  [1, 3, 200],
    [2, 3, 100], [2, 4, 150], [3, 4, 50],  [3, 5, 100],
    [4, 5, 30],  [1, 5, 500], [0, 5, 1000]
]

print("k=1:", findCheapestPrice(6, flights, 0, 5, 1))  # 600  (0→1→5)
print("k=2:", findCheapestPrice(6, flights, 0, 5, 2))  # 250  (0→2→3→5)
print("k=0:", findCheapestPrice(6, flights, 0, 5, 0))  # 1000 (0→5 direct only)
print("src==dst, k=-1:", findCheapestPrice(6, flights, 0, 0, -1))  # 0 (already there)


"""
================================================================================
QUICK REVISION CHEAT SHEET:
================================================================================

    Pattern: Modified Bellman-Ford with K+1 rounds + dist.copy()

    Template:
        dist = [inf]*n, dist[src] = 0
        for K+1 rounds:
            prev = dist[:]                          ← THE KEY LINE
            for u, v, w in flights:
                if prev[u] + w < dist[v]: update
        return dist[dst] or -1

    K stops = K+1 flights = K+1 rounds
    Copy prevents chaining multiple flights per round
    Time: O(K*E)  Space: O(V)

    Common mistakes:
        ✗ Forgetting the copy → chains flights, exceeds K stops
        ✗ range(k) instead of range(k+1) → off by one
        ✗ Using dist[u] instead of prev[u] → same as no copy
================================================================================
"""


"""
================================================================================
================================================================================
SOLUTION 2: MODIFIED DIJKSTRA (with stops as extra state)
================================================================================
================================================================================

KEY DIFFERENCE FROM REGULAR DIJKSTRA:
    Regular Dijkstra state:  (cost, node)
    Modified Dijkstra state: (cost, node, stops_used)

    We track HOW MANY STOPS we've used to reach each node.
    A node can be visited MULTIPLE TIMES with different stop counts.

    Why? Because a CHEAPER path with MORE stops might not lead to destination
    within K stops, but a COSTLIER path with FEWER stops might.

================================================================================
STEP 1: CONVERT EDGE LIST → ADJACENCY LIST
================================================================================

    flights = [[0,1,100], [0,2,50], [1,2,20], ...]

    Adjacency List (dict of lists):
        graph = {
            0: [(1, 100), (2, 50), (5, 1000)],
            1: [(2, 20), (3, 200), (5, 500)],
            2: [(3, 100), (4, 150)],
            3: [(4, 50), (5, 100)],
            4: [(5, 30)],
            5: []
        }

    Conversion code:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

================================================================================
PSEUDOCODE:
================================================================================

    function cheapestFlightDijkstra(n, flights, src, dst, k):

        1. BUILD adjacency list from flights
              graph[u] → list of (neighbor, cost)

        2. CREATE min-heap, push (cost=0, node=src, stops=0)

        3. CREATE stops_visited[node] = min stops used to reach node (or inf)
              This REPLACES the regular visited[] array.
              Why? A node can be worth revisiting with FEWER stops.

        4. WHILE heap not empty:
              pop (cost, node, stops)

              if node == dst → return cost (first time we pop dst = cheapest!)

              if stops > k → skip (used too many stops)

              if stops >= stops_visited[node] → skip (already reached with same/fewer stops)
              stops_visited[node] = stops

              for each (neighbor, weight) in graph[node]:
                  push (cost + weight, neighbor, stops + 1)

        5. RETURN -1 (destination unreachable within K stops)

================================================================================
WHY stops_visited[] INSTEAD OF visited[]?
================================================================================

    Regular Dijkstra: once visited, never revisit. (Cheapest = final)

    HERE: a node might be reached cheaply with 5 stops, but we need ≤ 1 stop.
    So we MUST allow revisiting with fewer stops.

    Example:
        First reach node 3 via 0→2→3 (cost=150, stops=1)
        Later reach node 3 via 0→1→3 (cost=300, stops=1)

        Same stops but costlier → skip (heap pops cheaper first anyway).

        But if we reached node 3 via 0→1→2→3 (cost=120, stops=2)
        and later via 0→2→3 (cost=150, stops=1)

        The second path is COSTLIER but uses FEWER stops → worth exploring!
        It might reach dst within K stops where the first path can't.

    RULE: Skip only if we already reached this node with SAME or fewer stops.

================================================================================
VISUAL WALKTHROUGH (src=0, dst=5, k=1):
================================================================================

    Heap initially: [(0, 0, 0)]

    Step │ Pop                │ Action                           │ Push
    ─────┼────────────────────┼──────────────────────────────────┼─────────────────────
    1    │ (0, node0, 0 stop) │ Process neighbors of 0           │ (100,1,1)(50,2,1)(1000,5,1)
    2    │ (50, node2, 1 stop)│ Process neighbors of 2           │ (150,3,2)(200,4,2)
    3    │ (100,node1, 1 stop)│ Process neighbors of 1           │ (120,2,2)(300,3,2)(600,5,2)
    4    │ (120,node2, 2 stop)│ stops=2 > k=1 → SKIP            │
    5    │ (150,node3, 2 stop)│ stops=2 > k=1 → SKIP            │
    6    │ (200,node4, 2 stop)│ stops=2 > k=1 → SKIP            │
    7    │ (300,node3, 2 stop)│ stops=2 > k=1 → SKIP            │
    8    │ (600,node5, 2 stop)│ stops=2 > k=1 → SKIP            │
    9    │(1000,node5, 1 stop)│ node5 == dst → RETURN 1000?      │

    Wait — that gives 1000, but Bellman-Ford gave 600!

    THE PROBLEM: With this pruning, (600, 5, 2) was skipped because stops=2 > k=1.
    But stops counts EDGES, and k=1 stop = 2 edges.

    FIX: Count stops as INTERMEDIATE nodes, not edges.
    Push (cost+w, neighbor, stops+1) but check stops+1 > k+1 (not stops > k).

    OR simpler: push stops as "stops used so far" where the SOURCE doesn't count.
    The destination's stop count = number of intermediate cities.

    Let's re-trace with correct counting (stops = intermediate nodes visited):

    Heap: [(0, 0, 0)]     ← 0 stops used (we're at source)

    Step │ Pop                │ Check                            │ Push
    ─────┼────────────────────┼──────────────────────────────────┼─────────────────────
    1    │ (0, node0, 0)      │ 0 stops ≤ k=1 ✓                 │ (100,1,1)(50,2,1)(1000,5,1)
         │                    │ neighbors get stops+1=1          │ (but 5 is dst, stops don't matter)
    2    │ (50, node2, 1)     │ 1 stop ≤ k=1 ✓                  │ (150,3,2)(200,4,2)
    3    │ (100, node1, 1)    │ 1 stop ≤ k=1 ✓                  │ (120,2,2)(300,3,2)(600,5,2)
    4    │ (120, node2, 2)    │ 2 stops > k=1 → SKIP            │
    5    │ (150, node3, 2)    │ 2 stops > k=1 → SKIP            │
    6    │ (200, node4, 2)    │ 2 stops > k=1 → SKIP            │
    7    │ (300, node3, 2)    │ 2 stops > k=1 → SKIP            │
    8    │ (600, node5, 2)    │ node5 == dst → RETURN 600 ✓     │

    KEY: We check "stops > k" BEFORE processing neighbors, but AFTER checking
    if it's the destination. Reaching dst with any number of stops is fine —
    we only limit INTERMEDIATE stops.

    ANSWER: 600 ✓ (matches Bellman-Ford)

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(V * K * log(V * K)) — each (node, stops) pair pushed once, heap operations
    Space: O(V * K) — heap can hold up to V*K entries

    vs Bellman-Ford: O(K * E) time, O(V) space
    Bellman-Ford is simpler and often faster for this problem.

================================================================================
BELLMAN-FORD vs MODIFIED DIJKSTRA — WHEN TO USE WHICH:
================================================================================

    ┌──────────────────┬──────────────────────┬──────────────────────────┐
    │                  │ Modified Bellman-Ford │ Modified Dijkstra        │
    ├──────────────────┼──────────────────────┼──────────────────────────┤
    │ Code complexity  │ Simple (8 lines)     │ Medium (15 lines)        │
    │ Time             │ O(K * E)             │ O(V*K * log(V*K))        │
    │ Space            │ O(V)                 │ O(V * K)                 │
    │ Interview pick   │ ✓ Preferred          │ Good to mention as alt   │
    │ Shows knowledge  │ Bellman-Ford mastery  │ State-space Dijkstra     │
    └──────────────────┴──────────────────────┴──────────────────────────┘

    TIP: Code Bellman-Ford first (faster to write), then MENTION you know
         the Dijkstra approach too. Interviewer will be impressed.

================================================================================
"""

import heapq
from collections import defaultdict


def findCheapestPriceDijkstra(n, flights, src, dst, k):
    if src == dst:
        return 0

    # Step 1: Build adjacency list
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    # Step 2: Min-heap with (cost, node, stops_used)
    min_heap = [(0, src, 0)]

    # Step 3: Track min stops used to reach each node
    stops_visited = [float('inf')] * n

    while min_heap:
        cost, node, stops = heapq.heappop(min_heap)

        if node == dst:         # Destination reached — heap guarantees cheapest
            return cost

        if stops > k:           # Exceeded stop limit — can't explore further
            continue

        if stops >= stops_visited[node]:  # Already reached with fewer/equal stops
            continue
        stops_visited[node] = stops

        for neighbor, weight in graph[node]:
            heapq.heappush(min_heap, (cost + weight, neighbor, stops + 1))

    return -1


# ── Example ──
flights2 = [
    [0, 1, 100], [0, 2, 50],  [1, 2, 20],  [1, 3, 200],
    [2, 3, 100], [2, 4, 150], [3, 4, 50],  [3, 5, 100],
    [4, 5, 30],  [1, 5, 500], [0, 5, 1000]
]

print("\n--- Modified Dijkstra ---")
print("k=1:", findCheapestPriceDijkstra(6, flights2, 0, 5, 1))  # 600
print("k=2:", findCheapestPriceDijkstra(6, flights2, 0, 5, 2))  # 250
print("k=0:", findCheapestPriceDijkstra(6, flights2, 0, 5, 0))  # 1000
print("src==dst, k=-1:", findCheapestPriceDijkstra(6, flights2, 0, 0, -1))  # 0


"""
================================================================================
ADJACENCY LIST VISUALIZATION (for reference):
================================================================================

    graph[0] = [(1,100), (2,50), (5,1000)]    0 → 1($100), 2($50), 5($1000)
    graph[1] = [(2,20), (3,200), (5,500)]     1 → 2($20), 3($200), 5($500)
    graph[2] = [(3,100), (4,150)]             2 → 3($100), 4($150)
    graph[3] = [(4,50), (5,100)]              3 → 4($50), 5($100)
    graph[4] = [(5,30)]                       4 → 5($30)
    graph[5] = []                             5 → (no outgoing)

================================================================================
QUICK REVISION — BOTH SOLUTIONS SIDE BY SIDE:
================================================================================

    BELLMAN-FORD (preferred):               MODIFIED DIJKSTRA (alternative):
    ─────────────────────────               ──────────────────────────────────
    dist = [inf]*n                          graph = adjacency list
    dist[src] = 0                           heap = [(0, src, 0)]
    for K+1 rounds:                         stops_visited = [inf]*n
        prev = dist[:]                      while heap:
        for u,v,w in flights:                   cost, node, stops = pop
            if prev[u]+w < dist[v]:             if node==dst: return cost
                update                          if stops>k: skip
    return dist[dst]                            if stops>=stops_visited: skip
                                                push (cost+w, nei, stops+1)

    O(K*E), O(V)                            O(VK*log(VK)), O(VK)
================================================================================
"""
"""
================================================================================
================================================================================
LeetCode 909 — Snakes and Ladders (FAANG Interview Guide)
================================================================================
================================================================================

PATTERN: BFS — Shortest Path in Unweighted Graph
DIFFICULTY: Medium
FREQUENCY: High (Amazon, Google, Goldman Sachs, Microsoft)

================================================================================
PROBLEM IN 10 SECONDS:
================================================================================

    Given an n×n board with snakes and ladders, find the MINIMUM number of
    dice rolls to reach the last cell from cell 1. Each roll gives 1–6.

    Think: "What's the fewest dice rolls to win the game?"

================================================================================
ONE-LINE TRICK TO REMEMBER:
================================================================================

    "Each cell is a NODE, each dice outcome is an EDGE, snakes/ladders are
     TELEPORTERS. BFS level = one dice roll. Levels to reach end = answer."

================================================================================
WHY BFS? WHY NOT DFS OR DIJKSTRA?
================================================================================

    BFS is correct because:
        → Every dice roll has cost = 1 (unweighted graph)
        → BFS finds shortest path in unweighted graphs
        → Each "level" of BFS = exactly one dice roll
        → First time we reach the last cell = minimum rolls

    DFS fails because:
        → DFS explores deep paths first, might find a long path before a short one
        → No guarantee of finding minimum rolls first

    Dijkstra is overkill because:
        → All edges have weight 1 → BFS is simpler and faster

================================================================================
THE MENTAL MODEL — Think of it as a GRAPH, not a board game:
================================================================================

    BOARD GAME VIEW (forget this):     GRAPH VIEW (think this):
    ┌──┬──┬──┬──┬──┐                  Cell 1 is the START NODE
    │20│19│18│17│16│                  Cell n*n is the END NODE
    ├──┼──┼──┼──┼──┤                  From any cell, you have UP TO 6 edges
    │11│12│13│14│15│                  (dice outcomes 1,2,3,4,5,6)
    ├──┼──┼──┼──┼──┤                  Snakes/ladders = forced redirections
    │10│ 9│ 8│ 7│ 6│                  BFS level count = dice rolls
    ├──┼──┼──┼──┼──┤
    │ 1│ 2│ 3│ 4│ 5│
    └──┴──┴──┴──┴──┘

    THE KEY INSIGHT:
    ┌────────────────────────────────────────────────────────────────┐
    │  Board cell  →  Graph node                                    │
    │  Dice roll   →  Edge (up to 6 edges per node)                 │
    │  Snake       →  Teleport DOWN (forced, no choice)             │
    │  Ladder      →  Teleport UP (forced, no choice)               │
    │  Min rolls   →  Shortest path in unweighted graph → BFS       │
    └────────────────────────────────────────────────────────────────┘

================================================================================
EXAMPLE (n=20 cells, 0-indexed for code):
================================================================================

    moves = [-1, 18, -1, -1, -1, -1, -1, -1, 2, -1,
             -1, -1, 15, -1, -1, -1, -1, -1, -1, -1]

    Index:   0   1   2   3   4   5   6   7   8   9  10  11  12  ...  19

    moves[i] = -1    → normal cell, no teleport
    moves[1] = 18    → LADDER at cell 1, teleports you to cell 18
    moves[8] = 2     → SNAKE at cell 8, teleports you DOWN to cell 2
    moves[12] = 15   → LADDER at cell 12, teleports you to cell 15

    Visual (1-indexed for clarity):
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │   Cell 2 ───LADDER───→ Cell 19  (moves[1]=18, 0-idx)   │
    │   Cell 9 ───SNAKE────→ Cell 3   (moves[8]=2,  0-idx)   │
    │   Cell 13──LADDER───→ Cell 16  (moves[12]=15, 0-idx)   │
    │                                                         │
    │   Goal: reach Cell 20 (index 19) from Cell 1 (index 0) │
    └─────────────────────────────────────────────────────────┘

================================================================================
ALGORITHM — 5 STEPS (memorize this):
================================================================================

    Step 1: queue = [start_cell], visited[start] = True, rolls = 0
    Step 2: Process ALL cells in current queue (= one BFS level = one roll)
    Step 3: For each cell, try dice 1–6 → compute next_cell
    Step 4: If next_cell has a snake/ladder → TELEPORT (next_cell = moves[next_cell])
    Step 5: If next_cell == last cell → return rolls + 1
            If not visited → mark visited, add to queue

    ┌─────────────────────────────────────────────────────────────────┐
    │  CRITICAL RULE: You CANNOT choose to stay at a snake/ladder    │
    │  cell. If you land there, you MUST teleport. That's why we     │
    │  mark the DESTINATION as visited, not the snake/ladder cell.   │
    └─────────────────────────────────────────────────────────────────┘

================================================================================
STEP-BY-STEP TRACE (n=20, 0-indexed):
================================================================================

    moves = [-1, 18, -1, -1, -1, -1, -1, -1, 2, -1, -1, -1, 15, -1, ...]

    Start: queue=[0], visited={0}, rolls=0

    ── ROLL 1 (BFS Level 1) ─────────────────────────────────────────
    Pop cell 0. Try dice 1–6:
        dice=1 → cell 1, moves[1]=18 → LADDER → teleport to 18. visited={0,18}
        dice=2 → cell 2, moves[2]=-1 → normal.                visited={0,18,2}
        dice=3 → cell 3, moves[3]=-1 → normal.                visited={0,18,2,3}
        dice=4 → cell 4, moves[4]=-1 → normal.                visited={0,18,2,3,4}
        dice=5 → cell 5, moves[5]=-1 → normal.                visited={...,5}
        dice=6 → cell 6, moves[6]=-1 → normal.                visited={...,6}

    After Roll 1: queue=[18, 2, 3, 4, 5, 6], rolls=1

    ── ROLL 2 (BFS Level 2) ─────────────────────────────────────────
    Pop cell 18. Try dice 1–6:
        dice=1 → cell 19 = LAST CELL → RETURN rolls+1 = 2 ✓

    ANSWER: 2 rolls

    Path: Cell 0 →(dice 1)→ Cell 1 →(ladder)→ Cell 18 →(dice 1)→ Cell 19
    In 1-indexed: Cell 1 → Cell 2 → [ladder to 19] → Cell 20 (WIN!)

================================================================================
WHY WE MARK THE TELEPORT DESTINATION, NOT THE LANDING CELL:
================================================================================

    When you land on cell 1 (which has a ladder to cell 18):

    WRONG: mark cell 1 as visited
        → Later, another path to cell 1 would be skipped
        → But cell 1 itself is never "occupied" — you teleport immediately

    CORRECT: mark cell 18 as visited (the teleport destination)
        → Cell 1 is just a redirect, you never stay there
        → You care about WHERE YOU END UP, not where you land

    Analogy: an airport with an automatic conveyor belt.
    You step on gate 1, it carries you to gate 18. You were never AT gate 1.

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(N) — each cell is visited at most once (N = total cells)
    Space: O(N) — visited array + queue

================================================================================
FAANG INTERVIEW TIPS:
================================================================================

    TIP 1: "Why BFS?" → All edges have weight 1 (one dice roll). BFS finds
            shortest path in unweighted graphs. This is the #1 follow-up.

    TIP 2: Snake/ladder cells are NOT "two edges." They are ONE edge
            that goes directly to the teleport destination. The intermediate
            cell doesn't exist as a stop.

    TIP 3: On LeetCode 909, the board is n×n with zigzag numbering.
            You need a helper to convert (row, col) ↔ cell number.
            Practice that conversion separately.

    TIP 4: "What if there's a snake at the last cell?"
            → Impossible by problem constraints, but clarify with interviewer.

    TIP 5: "Can a ladder lead to another ladder?"
            → Yes! But you DON'T chain them. You only teleport ONCE per landing.
            → (Some variants do chain — ask the interviewer.)

    TIP 6: Common mistake: forgetting to check next_cell >= n (going off board).
            Dice can push you past the last cell — those moves are invalid.

================================================================================
PATTERN RECOGNITION — When to use this approach:
================================================================================

    See this?                          → Think this:
    ─────────────────────────────────────────────────────
    "Minimum moves/steps/rolls"        → BFS shortest path
    "Grid/board with teleports"        → Nodes + redirect edges
    "Each move has equal cost"         → Unweighted → BFS not Dijkstra
    "Reach from start to end"          → Single-source shortest path

================================================================================
QUICK REVISION CHEAT SHEET:
================================================================================

    Pattern: BFS on unweighted graph (each roll = 1 level)

    Template:
        queue = [start], visited[start] = True, rolls = 0
        while queue:
            for each cell in current level:
                for dice 1–6:
                    next = cell + dice
                    if snake/ladder: next = moves[next]
                    if next == end: return rolls + 1
                    if not visited: add to queue
            rolls += 1
        return -1

    Key points:
        ✓ Mark teleport DESTINATION visited, not the snake/ladder cell
        ✓ Teleport is forced, not optional
        ✓ Don't go past the last cell
        ✓ Time O(N), Space O(N)

    Common mistakes:
        ✗ Using DFS → doesn't guarantee minimum
        ✗ Chaining teleports (ladder → ladder) → only teleport once
        ✗ Marking the snake/ladder cell visited instead of destination
        ✗ Forgetting bounds check (next_cell >= n)
================================================================================
"""
from collections import deque


def snakes_and_ladders(n, moves):
    queue = deque([0])                # 0-indexed: cell 1 = index 0
    visited = [False] * n
    visited[0] = True
    rolls = 0

    while queue:
        for _ in range(len(queue)):   # process one BFS level = one dice roll
            current = queue.popleft()

            if current == n - 1:      # reached the last cell
                return rolls

            for dice in range(1, 7):  # dice outcomes 1–6
                next_cell = current + dice

                if next_cell >= n:    # off the board
                    continue

                if moves[next_cell] != -1:        # snake or ladder
                    next_cell = moves[next_cell]   # forced teleport

                if not visited[next_cell]:
                    visited[next_cell] = True
                    queue.append(next_cell)

        rolls += 1

    return -1


# ── Example ──
n = 20
moves = [
    -1, 18, -1, -1, -1, -1, -1, -1,
     2, -1, -1, -1, 15, -1, -1, -1,
    -1, -1, -1, -1
]
print("\n--- Snakes and Ladders ---")
print("Min rolls:", snakes_and_ladders(n, moves))  # 2

"""
================================================================================
================================================================================
Complete All Courses With Dependencies (Course Schedule — FAANG Interview Guide)
================================================================================
================================================================================

PATTERN: Topological Sort (Kahn's BFS) / Cycle Detection in Directed Graph
DIFFICULTY: Medium
FREQUENCY: Very High (Amazon, Google, Facebook, Microsoft, Apple)
RELATED: LeetCode 207 (Course Schedule I), LeetCode 210 (Course Schedule II)

================================================================================
PROBLEM IN 10 SECONDS:
================================================================================

    Given n courses and prerequisite pairs (a[i] must come before b[i]),
    can you take ALL n courses without violating any prerequisite?

    Think: "Is there a valid order to do everything?"

================================================================================
ONE-LINE TRICK TO REMEMBER:
================================================================================

    "Prerequisite = arrow. Cycle = deadlock = impossible.
     No cycle = topological order exists = possible."

================================================================================
THE 3-SECOND MENTAL MODEL:
================================================================================

    See "A must happen before B" → Draw arrow A → B

    Then ask ONE question:

        "Does the graph have a CYCLE?"

        ┌──────────────┐              ┌──────────────┐
        │   NO CYCLE   │              │    CYCLE     │
        │              │              │              │
        │  A → B → C   │              │  A → B → C  │
        │  (can order)  │              │  ↑       ↓  │
        │              │              │  └───────┘  │
        │  return 1    │              │  (deadlock)  │
        │  (possible)  │              │  return 0    │
        └──────────────┘              └──────────────┘

================================================================================
WHY A CYCLE = IMPOSSIBLE (the deadlock analogy):
================================================================================

    Imagine 3 people at a door:

        Alice says: "I'll go in AFTER Bob"
        Bob says:   "I'll go in AFTER Carol"
        Carol says: "I'll go in AFTER Alice"

        Alice waits for Bob → Bob waits for Carol → Carol waits for Alice
        → EVERYONE WAITS FOREVER → DEADLOCK

    That's exactly what a cycle means in prerequisites:

        Course A needs B first
        Course B needs C first
        Course C needs A first

        A → B → C → A   (cycle → impossible)

================================================================================
EXAMPLE 1 (No Cycle → Possible):
================================================================================

    n = 4, a = [1, 1, 3], b = [0, 2, 1]

    Step 1: Convert pairs to arrows
        a[0]=1, b[0]=0  →  1 → 0  (take 1 before 0)
        a[1]=1, b[1]=2  →  1 → 2  (take 1 before 2)
        a[2]=3, b[2]=1  →  3 → 1  (take 3 before 1)

    Step 2: Draw the graph
             ┌──→ 0
             │
        3 → 1 ──→ 2

    Step 3: Check for cycle → NO CYCLE

    Step 4: Find a valid order
        Course 3 has no prerequisites → take it first
        Course 1 now has no remaining prerequisites → take it next
        Course 0 and 2 now free → take them

        Valid order: 3 → 1 → 0 → 2  ✓

    Answer: 1 (possible)

================================================================================
EXAMPLE 2 (Cycle → Impossible):
================================================================================

    n = 4, a = [1, 1, 3, 0], b = [0, 2, 1, 3]

    Step 1: Convert pairs to arrows
        1 → 0
        1 → 2
        3 → 1
        0 → 3    ← this creates a cycle!

    Step 2: Draw the graph
        3 → 1 → 0 → 3    ← CYCLE: 3 → 1 → 0 → 3

    Step 3: Trace the deadlock

        To take 1 → need 3 first
        To take 3 → need 0 first    (because 0 → 3)
        To take 0 → need 1 first    (because 1 → 0)

        1 needs 3 needs 0 needs 1 needs 3 needs 0 ... FOREVER

    Answer: 0 (impossible)

================================================================================
THE ALGORITHM — KAHN'S BFS TOPOLOGICAL SORT (memorize these 4 steps):
================================================================================

    ┌─────────────────────────────────────────────────────────────────────┐
    │                                                                     │
    │  Step 1: Build graph + count indegrees                              │
    │          For each a[i] → b[i]: add edge, indegree[b[i]] += 1       │
    │                                                                     │
    │  Step 2: Queue all courses with indegree = 0                        │
    │          (these have NO prerequisites — safe to take first)         │
    │                                                                     │
    │  Step 3: BFS loop — take a course, reduce indegrees of dependents   │
    │          When a dependent's indegree hits 0 → add to queue          │
    │                                                                     │
    │  Step 4: If completed == n → return 1 (all courses taken)           │
    │          If completed < n  → return 0 (cycle blocked some courses)  │
    │                                                                     │
    └─────────────────────────────────────────────────────────────────────┘

    REAL-LIFE ANALOGY:
        You have a pile of tasks with sticky notes saying "wait for X first."
        Start with tasks that have NO sticky notes (indegree 0).
        Complete them, then PEEL OFF their sticky notes from other tasks.
        Any task whose last sticky note was peeled → now ready to do.
        If you finish all tasks → success. If some still have sticky notes → cycle.

================================================================================
INDEGREE — THE KEY CONCEPT:
================================================================================

    Indegree of a node = number of arrows POINTING INTO it
                       = number of prerequisites it still needs

    Example 1: a=[1,1,3], b=[0,2,1]  (edges: 1→0, 1→2, 3→1)

        Course │ Arrows pointing in │ Indegree │ Meaning
        ───────┼────────────────────┼──────────┼────────────────────────
          0    │ 1→0                │    1     │ needs 1 course first
          1    │ 3→1                │    1     │ needs 1 course first
          2    │ 1→2                │    1     │ needs 1 course first
          3    │ (none)             │    0     │ NO prerequisites → START HERE

    Courses with indegree 0 = courses you can take RIGHT NOW.

================================================================================
STEP-BY-STEP TRACE — EXAMPLE 1:
================================================================================

    Graph: 3 → 1 → 0, 1 → 2
    Indegree: [1, 1, 1, 0]
    Queue starts with: [3]  (only course with indegree 0)
    completed = 0

    ── Iteration 1 ────────────────────────────────────────────────────
    Pop course 3
    completed = 1
    Course 3's neighbors: [1]
        indegree[1] = 1-1 = 0  → indegree is 0! → add 1 to queue

    Queue: [1]    Indegree: [1, 0, 1, 0]

    ── Iteration 2 ────────────────────────────────────────────────────
    Pop course 1
    completed = 2
    Course 1's neighbors: [0, 2]
        indegree[0] = 1-1 = 0  → add 0 to queue
        indegree[2] = 1-1 = 0  → add 2 to queue

    Queue: [0, 2]    Indegree: [0, 0, 0, 0]

    ── Iteration 3 ────────────────────────────────────────────────────
    Pop course 0
    completed = 3
    Course 0's neighbors: []  (nothing depends on 0)

    ── Iteration 4 ────────────────────────────────────────────────────
    Pop course 2
    completed = 4
    Course 2's neighbors: []

    Queue empty. completed = 4 = n → RETURN 1 ✓

    Order taken: 3 → 1 → 0 → 2

================================================================================
STEP-BY-STEP TRACE — EXAMPLE 2 (Cycle):
================================================================================

    Edges: 1→0, 1→2, 3→1, 0→3
    Indegree: [1, 1, 1, 1]   ← EVERY course has at least 1 prerequisite!

    Queue starts with: []  (NO course has indegree 0)

    Queue is immediately empty.
    completed = 0, but n = 4.
    0 ≠ 4 → RETURN 0 ✗ (cycle detected)

    Why? The cycle 0→3→1→0 means those 3 courses are stuck waiting for
    each other. None of them can ever reach indegree 0.

================================================================================
WHY completed < n MEANS CYCLE:
================================================================================

    In a cycle, every node in the cycle always has indegree ≥ 1.
    No node in the cycle ever gets added to the queue.
    So they never get "completed."

    If any nodes remain uncompleted → they must be part of (or blocked by) a cycle.

    ┌────────────────────────────────────────────────────┐
    │  completed == n  →  no cycle  →  all courses done  │
    │  completed < n   →  cycle     →  some stuck forever│
    └────────────────────────────────────────────────────┘

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(V + E) — visit each course once, process each edge once
           V = n (courses), E = len(a) (dependencies)
    Space: O(V + E) — adjacency list + indegree array + queue

================================================================================
FAANG INTERVIEW TIPS:
================================================================================

    TIP 1: "What algorithm is this?"
            → Kahn's Algorithm (BFS-based Topological Sort)
            → Equivalent to cycle detection in a directed graph

    TIP 2: "Can you also use DFS?"
            → Yes! DFS with 3-color marking (white/gray/black).
            → Gray node visited again = cycle (back edge).
            → Kahn's BFS is easier to code and explain.

    TIP 3: "What if they ask for the actual ORDER?" (Course Schedule II)
            → Same algorithm, just collect the order in a list:
              order.append(course) each time you pop from queue
            → Return order if len(order) == n, else return []

    TIP 4: "What if the graph is disconnected?"
            → Kahn's handles this automatically!
            → Multiple components each get their indegree-0 nodes queued.

    TIP 5: Common follow-ups:
            → "Return any valid order" → collect popped courses
            → "Return ALL valid orders" → backtracking
            → "Minimum semesters to finish" → BFS level count (parallel courses)

    TIP 6: Off-by-one trap — make sure you handle:
            → Courses labeled 0 to n-1 (not 1 to n)
            → Self-loops (a[i] == a[i] → instant cycle, but problem says a[i] != b[i])

================================================================================
THE FAMILY OF COURSE SCHEDULE PROBLEMS:
================================================================================

    Problem                     │ What it asks              │ Core technique
    ────────────────────────────┼───────────────────────────┼──────────────────
    Course Schedule I (LC 207)  │ Can all be completed?     │ Cycle detection
    Course Schedule II (LC 210) │ Return a valid order      │ Topological sort
    Course Schedule III (LC 630)│ Max courses by deadlines  │ Greedy + heap
    Course Schedule IV (LC 1462)│ Is A prerequisite of B?   │ Floyd-Warshall/BFS
    This problem                │ Same as LC 207            │ Kahn's BFS

================================================================================
PATTERN RECOGNITION — When to use Topological Sort:
================================================================================

    See this?                              → Think this:
    ─────────────────────────────────────────────────────────────
    "Must do X before Y"                   → Directed edge X → Y
    "Is there a valid ordering?"           → Cycle detection
    "Find a valid ordering"               → Topological sort
    "Build order / compile order"          → Same pattern
    "Minimum time with parallel tasks"     → BFS topo sort (level = time unit)

================================================================================
QUICK REVISION CHEAT SHEET:
================================================================================

    Pattern: Kahn's BFS Topological Sort

    Template:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for each a[i] → b[i]:
            graph[a[i]].append(b[i])
            indegree[b[i]] += 1
        queue = [c for c in range(n) if indegree[c] == 0]
        completed = 0
        while queue:
            course = queue.pop()
            completed += 1
            for next in graph[course]:
                indegree[next] -= 1
                if indegree[next] == 0: queue.append(next)
        return completed == n

    Key points:
        ✓ Indegree 0 = no prerequisites = safe to start
        ✓ Completing a course reduces dependents' indegree
        ✓ Cycle → some nodes never reach indegree 0 → completed < n
        ✓ Time O(V+E), Space O(V+E)

    Common mistakes:
        ✗ Forgetting to build the indegree array
        ✗ Using undirected edges (prerequisites are DIRECTED)
        ✗ Returning the wrong boolean (1 = possible, 0 = impossible)
        ✗ Not handling disconnected components (Kahn's handles it!)
================================================================================
"""

from collections import deque


def can_be_completed(n, a, b):
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for i in range(len(a)):
        graph[a[i]].append(b[i])
        indegree[b[i]] += 1

    queue = deque()
    for course in range(n):
        if indegree[course] == 0:
            queue.append(course)

    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1

        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    return completed == n


# ── Examples ──
print("\n--- Course Dependencies ---")
print("Example 1:", can_be_completed(4, [1, 1, 3], [0, 2, 1]))       # True  (order: 3→1→0→2)
print("Example 2:", can_be_completed(4, [1, 1, 3, 0], [0, 2, 1, 3])) # False (cycle: 0→3→1→0)



