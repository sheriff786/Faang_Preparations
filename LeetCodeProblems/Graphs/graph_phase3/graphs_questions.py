"""
================================================================================
LeetCode 1584 — Min Cost to Connect All Points (FAANG Interview Guide)
================================================================================

PATTERN: MST (Prim's Algorithm)
DIFFICULTY: Medium
FREQUENCY: Very High (Amazon, Google, Facebook)

================================================================================
PROBLEM IN 10 SECONDS:
================================================================================

    Given n points on a 2D plane, connect ALL points with minimum total cost.
    Cost between two points = Manhattan Distance = |x1-x2| + |y1-y2|

================================================================================
WHY THIS IS AN MST PROBLEM:
================================================================================

    Every point = a node.
    Every pair of points = an edge with weight = Manhattan distance.
    "Connect all with min cost, no cycles" = Minimum Spanning Tree.

    Since every point connects to every other → COMPLETE graph → E = V*(V-1)/2
    Dense graph → Prim's is the best choice (not Kruskal's).

================================================================================
EXAMPLE — PLOTTING POINTS ON XY COORDINATES:
================================================================================

    points = [[0,0], [2,2], [3,10], [5,2], [7,0]]

    Y
    10 |          P2(3,10)
     9 |
     8 |
     7 |
     6 |
     5 |
     4 |
     3 |
     2 |    P1(2,2)    P3(5,2)
     1 |
     0 | P0(0,0)             P4(7,0)
       └──────────────────────────── X
         0  1  2  3  4  5  6  7

================================================================================
MANHATTAN DISTANCE TABLE (all pairs):
================================================================================

    Formula: |x1-x2| + |y1-y2|

            P0(0,0)   P1(2,2)   P2(3,10)  P3(5,2)   P4(7,0)
    P0(0,0)    0         4        13         7         7
    P1(2,2)    4         0         9         3         7
    P2(3,10)  13         9         0        10        14
    P3(5,2)    7         3        10         0         4
    P4(7,0)    7         7        14         4         0

    How to read: Row P0, Column P1 = 4 means cost to connect P0↔P1 is 4.

    Example calculations:
        P0↔P1 = |0-2| + |0-2| = 2+2 = 4
        P1↔P3 = |2-5| + |2-2| = 3+0 = 3   ← cheapest non-zero edge!
        P3↔P4 = |5-7| + |2-0| = 2+2 = 4
        P1↔P2 = |2-3| + |2-10| = 1+8 = 9

================================================================================
PRIM'S ALGORITHM STEP-BY-STEP WALKTHROUGH:
================================================================================

    Start from P0. Heap = [(0, P0)]. Visited = {}

    ── STEP 1: Pop (0, P0) ──────────────────────────────────────────────
    Visit P0. Push distances to all unvisited points:
        P0→P1: 4, P0→P2: 13, P0→P3: 7, P0→P4: 7
    Heap: [(4,P1), (7,P3), (7,P4), (13,P2)]
    MST cost: 0

    ── STEP 2: Pop (4, P1) ── cheapest in heap ─────────────────────────
    Visit P1. Push distances to unvisited:
        P1→P2: 9, P1→P3: 3, P1→P4: 7
    Heap: [(3,P3), (7,P3), (7,P4), (9,P2), (13,P2), (7,P4)]
    MST cost: 0 + 4 = 4
    MST edge: P0 ──4── P1

    ── STEP 3: Pop (3, P3) ── cheapest ─────────────────────────────────
    Visit P3. Push distances to unvisited:
        P3→P2: 10, P3→P4: 4
    Heap: [(4,P4), (7,P3★stale), (7,P4), (9,P2), (10,P2), (13,P2)]
    MST cost: 4 + 3 = 7
    MST edge: P1 ──3── P3

    ── STEP 4: Pop (4, P4) ────────────────────────────────────────────
    Visit P4. Push distances to unvisited:
        P4→P2: 14
    Heap: [(7,P3★skip), (7,P4★skip), (9,P2), (10,P2), (13,P2), (14,P2)]
    MST cost: 7 + 4 = 11
    MST edge: P3 ──4── P4

    ── STEP 5: Pop stale entries, then (9, P2) ────────────────────────
    Visit P2. Last node — done!
    MST cost: 11 + 9 = 20
    MST edge: P1 ──9── P2

    FINAL MST:
                   9
            P2(3,10)
            │
         P1(2,2)
        ╱       ╲
    P0(0,0)    P3(5,2)
      cost=4   cost=3  ╲
                      P4(7,0)
                      cost=4

    ANSWER: 4 + 3 + 4 + 9 = 20

================================================================================
ALGORITHM:
================================================================================

    1. Start from any point (e.g., point 0), push (cost=0, index=0) into min-heap
    2. Pop cheapest (cost, point) from heap
    3. If already visited → skip (stale entry)
    4. Mark visited, add cost to total
    5. For every OTHER unvisited point: calculate Manhattan distance, push to heap
    6. Repeat until all points visited
    7. Return total cost

    KEY: No adjacency list needed! Compute edge weights on-the-fly from coordinates.

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(V² log V)
        - V points, each pushes up to V edges → V² heap operations
        - Each heap push/pop = O(log(V²)) = O(log V)
        - Total: O(V² log V)

    Space: O(V²)
        - Heap can hold up to V² entries in worst case
        - visited array: O(V)

    WHY NOT KRUSKAL'S HERE?
        Kruskal's needs to sort ALL edges first: O(E log E) = O(V² log V²) = O(V² log V)
        Same time, but Kruskal's also needs O(V²) space for edge list + Union-Find.
        Prim's is more natural when edges are computed on-the-fly.

================================================================================
FAANG INTERVIEW TIPS:
================================================================================

    TIP 1: Tell interviewer: "This is a complete graph (every node connects to every
            other), so E = V². Prim's with a heap is ideal for dense graphs."

    TIP 2: Don't build an adjacency list! Compute Manhattan distance on-the-fly.
            Building adj list = O(V²) space wasted.

    TIP 3: Early termination: stop when edges_used == n (all nodes in MST).
            Avoids processing remaining stale heap entries.

    TIP 4: If V is very large (>10000), consider optimized Prim's with a key[] array
            instead of pushing duplicates to heap. But standard heap approach passes.

    TIP 5: Common follow-up: "What if we use Euclidean distance instead?"
            → Same algorithm, just change the distance formula.
            Manhattan: |x1-x2| + |y1-y2|
            Euclidean: sqrt((x1-x2)² + (y1-y2)²)

================================================================================
"""

import heapq


def manhattan_distance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    return abs(x1 - x2) + abs(y1 - y2)


def minCostConnectPoints(points):

    n = len(points)

    visited = [False] * n

    min_heap = [(0, 0)]  # (cost, point_index)

    total_cost = 0

    edges_used = 0

    while min_heap and edges_used < n:

        cost, i = heapq.heappop(min_heap)

        if visited[i]:
            continue

        # Add point to MST
        visited[i] = True

        total_cost += cost

        edges_used += 1

        # Connect current point to every unvisited point
        for j in range(n):

            if not visited[j]:

                distance = manhattan_distance(
                    points[i],
                    points[j]
                )

                heapq.heappush(
                    min_heap,
                    (distance, j)
                )

    return total_cost
