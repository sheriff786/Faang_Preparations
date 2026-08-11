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
