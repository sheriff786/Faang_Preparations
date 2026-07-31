"""
=== COMPLETE GRAPH CONSTRUCTION CHEAT SHEET ===

How to Remember (Just 2 rules):

    DIRECTED:       graph[src] → dest           (one way only)
    UNDIRECTED:     graph[src] → dest AND       (both ways)
                    graph[dest] → src

    UNWEIGHTED:     store just the node         (0 or 1 in matrix)
    WEIGHTED:       store (node, weight) pair   (weight value in matrix)

That's it. Every combination below is just mixing these 2 rules.

─────────────────────────────────────────────────────────────────
Type                    │ List: what to store    │ Matrix: what to store
─────────────────────────────────────────────────────────────────
Directed Unweighted     │ dest                   │ 1
Directed Weighted       │ (dest, weight)         │ weight
Undirected Unweighted   │ dest (both ways)       │ 1 (both cells)
Undirected Weighted     │ (dest, weight) (both)  │ weight (both cells)
─────────────────────────────────────────────────────────────────
"""


# ═══════════════════════════════════════════════════════════════════
# 1. DIRECTED + UNWEIGHTED
# ═══════════════════════════════════════════════════════════════════
#
#   0 ───→ 1 ───→ 2
#   Only one direction. No weight.

class DirectedUnweightedList:

    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, src, dest):
        self.graph[src].append(dest)  # ONE direction

    def print_graph(self):
        for v in self.graph:
            print(f"  {v} → {self.graph[v]}")


class DirectedUnweightedMatrix:

    def __init__(self, vertices):
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, src, dest):
        self.matrix[src][dest] = 1  # ONE cell

    def print_graph(self):
        for i, row in enumerate(self.matrix):
            print(f"  {i} | {row}")


# ═══════════════════════════════════════════════════════════════════
# 2. DIRECTED + WEIGHTED
# ═══════════════════════════════════════════════════════════════════
#
#   0 ──5──→ 1 ──7──→ 2
#   Only one direction. Has weight.

class DirectedWeightedList:

    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))  # ONE direction + weight

    def print_graph(self):
        for v in self.graph:
            print(f"  {v} → {self.graph[v]}")


class DirectedWeightedMatrix:

    def __init__(self, vertices):
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.matrix[src][dest] = weight  # ONE cell = weight

    def print_graph(self):
        for i, row in enumerate(self.matrix):
            print(f"  {i} | {row}")


# ═══════════════════════════════════════════════════════════════════
# 3. UNDIRECTED (BIDIRECTIONAL) + UNWEIGHTED
# ═══════════════════════════════════════════════════════════════════
#
#   0 ←───→ 1 ←───→ 2
#   Both directions. No weight.

class UndirectedUnweightedList:

    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, src, dest):
        self.graph[src].append(dest)   # src → dest
        self.graph[dest].append(src)   # dest → src  (BOTH!)

    def print_graph(self):
        for v in self.graph:
            print(f"  {v} → {self.graph[v]}")


class UndirectedUnweightedMatrix:

    def __init__(self, vertices):
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, src, dest):
        self.matrix[src][dest] = 1   # BOTH cells = 1
        self.matrix[dest][src] = 1

    def print_graph(self):
        for i, row in enumerate(self.matrix):
            print(f"  {i} | {row}")


# ═══════════════════════════════════════════════════════════════════
# 4. UNDIRECTED (BIDIRECTIONAL) + WEIGHTED
# ═══════════════════════════════════════════════════════════════════
#
#   0 ←─5─→ 1 ←─7─→ 2
#   Both directions. Has weight.

class UndirectedWeightedList:

    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))   # BOTH + weight
        self.graph[dest].append((src, weight))

    def print_graph(self):
        for v in self.graph:
            print(f"  {v} → {self.graph[v]}")


class UndirectedWeightedMatrix:

    def __init__(self, vertices):
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.matrix[src][dest] = weight   # BOTH cells = weight
        self.matrix[dest][src] = weight

    def print_graph(self):
        for i, row in enumerate(self.matrix):
            print(f"  {i} | {row}")


# ═══════════════════════════════════════════════════════════════════
# DEMO — Run this file to see all 8 variations
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    print("=" * 60)
    print("1. DIRECTED + UNWEIGHTED")
    print("=" * 60)
    print("\n  Adjacency List:")
    g = DirectedUnweightedList(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.print_graph()

    print("\n  Adjacency Matrix:")
    g = DirectedUnweightedMatrix(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.print_graph()

    print("\n" + "=" * 60)
    print("2. DIRECTED + WEIGHTED")
    print("=" * 60)
    print("\n  Adjacency List:")
    g = DirectedWeightedList(4)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 7)
    g.print_graph()

    print("\n  Adjacency Matrix:")
    g = DirectedWeightedMatrix(4)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 7)
    g.print_graph()

    print("\n" + "=" * 60)
    print("3. UNDIRECTED (BIDIRECTIONAL) + UNWEIGHTED")
    print("=" * 60)
    print("\n  Adjacency List:")
    g = UndirectedUnweightedList(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.print_graph()

    print("\n  Adjacency Matrix:")
    g = UndirectedUnweightedMatrix(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.print_graph()

    print("\n" + "=" * 60)
    print("4. UNDIRECTED (BIDIRECTIONAL) + WEIGHTED")
    print("=" * 60)
    print("\n  Adjacency List:")
    g = UndirectedWeightedList(3)
    g.add_edge(0, 1, 5)
    g.add_edge(1, 2, 7)
    g.print_graph()

    print("\n  Adjacency Matrix:")
    g = UndirectedWeightedMatrix(3)
    g.add_edge(0, 1, 5)
    g.add_edge(1, 2, 7)
    g.print_graph()

    print("\n" + "=" * 60)
    print("QUICK MEMORY TRICK")
    print("=" * 60)
    print("""
    Ask yourself 2 questions:

    Q1: Direction?
        → Directed:   add ONCE      (src → dest)
        → Undirected: add TWICE     (src → dest AND dest → src)

    Q2: Weight?
        → Unweighted: store node    (list: dest,  matrix: 1)
        → Weighted:   store pair    (list: (dest,w), matrix: w)

    That's ALL. Every graph type is just a combination of these two answers.
    """)
