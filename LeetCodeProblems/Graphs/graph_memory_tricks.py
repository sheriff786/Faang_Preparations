"""
=== GRAPH CONSTRUCTION - MEMORY TRICKS ===

You only need to remember ONE template. Then answer 2 questions.


TRICK #1: The "Direction + Weight" Grid
────────────────────────────────────────

                    UNWEIGHTED          WEIGHTED
                    ──────────          ────────
    DIRECTED        store dest          store (dest, weight)
    (one-way)       add to src ONLY     add to src ONLY

    UNDIRECTED      store dest          store (dest, weight)
    (two-way)       add to BOTH         add to BOTH


TRICK #2: The "Mirror" Rule
────────────────────────────

    Directed   = ONE line of code    →  graph[src].append(...)
    Undirected = MIRROR it           →  graph[src].append(...)
                                        graph[dest].append(...)

    Same for matrix:
    Directed   = ONE cell            →  matrix[src][dest] = value
    Undirected = MIRROR cell         →  matrix[src][dest] = value
                                        matrix[dest][src] = value


TRICK #3: The "Backpack" Analogy
────────────────────────────────

    Think of each node as a person with a backpack.

    Unweighted: They put a NOTE in their backpack saying "I know node X"
                → graph[me].append(neighbor)

    Weighted:   They put a NOTE saying "I know node X, distance = 5"
                → graph[me].append((neighbor, 5))

    Directed:   Only YOU write the note (one-sided friendship)
    Undirected: BOTH of you write notes about each other


TRICK #4: The "Matrix Symmetry" Test
─────────────────────────────────────

    After building a matrix:
    - Directed graph   → matrix is NOT symmetric (top-right ≠ bottom-left)
    - Undirected graph → matrix IS symmetric     (mirror along diagonal)

    Example (directed):          Example (undirected):
        [0, 1, 0]                   [0, 1, 0]
        [0, 0, 1]  ← not mirror    [1, 0, 1]  ← mirror!
        [0, 0, 0]                   [0, 1, 0]


TRICK #5: Count Your "append" or "= 1" Lines
─────────────────────────────────────────────

    Directed   → 1 line  (one append or one matrix assignment)
    Undirected → 2 lines (two appends or two matrix assignments)

    If you wrote 1 line → directed
    If you wrote 2 lines → undirected
    That's your self-check.


TRICK #6: The "What Do I Store?" Decision
──────────────────────────────────────────

    ADJACENCY LIST:
        Unweighted → just the number:        graph[0] = [1, 2, 3]
        Weighted   → tuple (node, weight):   graph[0] = [(1,5), (2,3)]

    ADJACENCY MATRIX:
        Unweighted → 0 or 1:                 matrix[0][1] = 1
        Weighted   → 0 or weight:            matrix[0][1] = 5


=== THE ULTIMATE ONE-LINER TO REMEMBER ===

    "Direction decides HOW MANY times you write.
     Weight decides WHAT you write."

"""


# ─── Proof: Build any graph with just 2 decisions ─────────────────

def build_graph(vertices, edges, directed=True, weighted=False):
    """
    Universal graph builder. Just flip 2 booleans.

    edges format:
        unweighted: [(src, dest), ...]
        weighted:   [(src, dest, weight), ...]
    """
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        src, dest = edge[0], edge[1]
        weight = edge[2] if weighted else None

        # WHAT to store (weight decision)
        entry_forward = (dest, weight) if weighted else dest
        entry_backward = (src, weight) if weighted else src

        # HOW MANY times to store (direction decision)
        graph[src].append(entry_forward)
        if not directed:
            graph[dest].append(entry_backward)

    return graph


if __name__ == "__main__":

    print("=" * 55)
    print("  Same function, 4 different graphs. Just flip flags.")
    print("=" * 55)

    edges_unw = [(0, 1), (1, 2), (0, 2)]
    edges_w = [(0, 1, 5), (1, 2, 7), (0, 2, 3)]

    configs = [
        ("Directed + Unweighted",   edges_unw, True,  False),
        ("Directed + Weighted",     edges_w,   True,  True),
        ("Undirected + Unweighted", edges_unw, False, False),
        ("Undirected + Weighted",   edges_w,   False, True),
    ]

    for name, edges, directed, weighted in configs:
        print(f"\n{'─' * 55}")
        print(f"  {name}")
        print(f"  directed={directed}, weighted={weighted}")
        print(f"{'─' * 55}")
        g = build_graph(3, edges, directed, weighted)
        for node in g:
            print(f"    {node} → {g[node]}")

    print("\n" + "=" * 55)
    print("  REMEMBER:")
    print("    Direction → how many times you write (1 or 2)")
    print("    Weight    → what you write (node or (node,w))")
    print("=" * 55)
