"""
Generate a comprehensive Graph DSA PDF guide for FAANG/MAANG interview prep.
Covers all phases from beginner to advanced.
"""

from fpdf import FPDF


class GraphGuidePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, "Graph DSA - FAANG/MAANG Interview Guide", align="L")
            self.cell(0, 8, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
            self.line(10, 16, 200, 16)
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, "Confidential - Personal Study Material", align="C")

    def cover_page(self):
        self.add_page()
        self.ln(50)
        self.set_font("Helvetica", "B", 32)
        self.set_text_color(20, 60, 120)
        self.cell(0, 15, "Graph Data Structures", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 15, "& Algorithms", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(8)
        self.set_font("Helvetica", "", 18)
        self.set_text_color(80, 80, 80)
        self.cell(0, 12, "Complete FAANG / MAANG Interview Guide", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(15)
        self.set_draw_color(20, 60, 120)
        self.set_line_width(1)
        self.line(60, self.get_y(), 150, self.get_y())
        self.ln(15)
        self.set_font("Helvetica", "", 13)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, "Beginner to Advanced | 8 Phases | 30+ Problems", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 10, "Tricks, Traces, Templates & Interview Tips", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(40)
        self.set_font("Helvetica", "I", 11)
        self.cell(0, 10, "Personal Study Guide - 2026", align="C", new_x="LMARGIN", new_y="NEXT")

    def section_title(self, title, r=20, g=60, b=120):
        self.ln(4)
        self.set_fill_color(r, g, b)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, f"  {title}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(3)

    def sub_title(self, title):
        self.ln(2)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(20, 80, 140)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def sub_sub_title(self, title):
        self.ln(1)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(60, 60, 60)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)

    def body(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 5.5, text)

    def bold_body(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 10)
        self.multi_cell(0, 5.5, text)

    def trick_box(self, trick_text):
        self.ln(2)
        self.set_x(self.l_margin)
        self.set_fill_color(255, 248, 220)
        self.set_draw_color(200, 160, 50)
        self.set_line_width(0.4)
        x = self.get_x()
        y = self.get_y()
        self.set_font("Helvetica", "B", 9)
        # calculate height
        w = self.w - self.l_margin - self.r_margin - 6
        lines = self.multi_cell(w, 5, trick_text, dry_run=True, output="LINES")
        h = len(lines) * 5 + 6
        if y + h > self.h - 25:
            self.add_page()
            y = self.get_y()
        self.rect(x, y, self.w - self.l_margin - self.r_margin, h, style="DF")
        self.set_xy(x + 3, y + 3)
        self.set_font("Helvetica", "BI", 9)
        self.set_text_color(120, 80, 0)
        self.multi_cell(w, 5, trick_text)
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def code_block(self, code):
        self.ln(1)
        self.set_x(self.l_margin)
        self.set_fill_color(240, 240, 245)
        self.set_font("Courier", "", 8.5)
        lines = code.split("\n")
        x = self.get_x()
        y = self.get_y()
        h = len(lines) * 4.5 + 4
        if y + h > self.h - 25:
            self.add_page()
            y = self.get_y()
        self.rect(x, y, self.w - self.l_margin - self.r_margin, h, style="F")
        self.set_xy(x + 3, y + 2)
        for line in lines:
            self.cell(0, 4.5, line, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x + 3)
        self.set_xy(x, y + h)
        self.ln(2)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        x = self.l_margin
        self.set_x(x + 3)
        self.cell(5, 5.5, "- ", new_x="END")
        w = self.w - self.get_x() - self.r_margin
        self.multi_cell(w, 5.5, text)


    def table_row(self, cells, widths, bold=False, fill=False):
        self.set_font("Helvetica", "B" if bold else "", 9)
        if fill:
            self.set_fill_color(220, 230, 245)
        h = 6
        x_start = self.l_margin
        self.set_x(x_start)
        max_h = h
        for i, cell in enumerate(cells):
            lines = self.multi_cell(widths[i], h, cell, dry_run=True, output="LINES")
            cell_h = len(lines) * h
            if cell_h > max_h:
                max_h = cell_h
        if self.get_y() + max_h > self.h - 25:
            self.add_page()
        y_start = self.get_y()
        for i, cell in enumerate(cells):
            self.set_xy(x_start + sum(widths[:i]), y_start)
            self.multi_cell(widths[i], h, cell, border=1, fill=fill, align="L")
        self.set_xy(x_start, y_start + max_h)


def build_pdf():
    pdf = GraphGuidePDF()

    # ── COVER PAGE ──
    pdf.cover_page()

    # ══════════════════════════════════════════════════════════════════
    # TABLE OF CONTENTS
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("TABLE OF CONTENTS")
    toc = [
        "1.  Roadmap Overview - 8 Phases at a Glance",
        "2.  Foundation - Graph Representations (Adjacency List & Matrix)",
        "3.  Phase 1 - BFS, DFS & Connectivity Problems",
        "4.  Phase 1.5 - Cycle Detection (Directed & Undirected)",
        "5.  Phase 2 - Topological Sort & Course Scheduling",
        "6.  Phase 2.5 - Clone Graph Pattern",
        "7.  Phase 3 - Shortest Path Algorithms (BFS, Dijkstra, Bellman-Ford, Floyd-Warshall)",
        "8.  Phase 4 - Minimum Spanning Tree (Prim's & Kruskal's)",
        "9.  Phase 5 - Advanced DFS (Bridges, Articulation Points, Tarjan's)",
        "10. FAANG Problem Set - 30+ Must-Solve Problems by Phase",
        "11. Master Cheat Sheet - All Tricks, Templates & Decision Trees",
    ]
    for item in toc:
        pdf.bullet(item)
    pdf.ln(5)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 1: ROADMAP
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("1. ROADMAP OVERVIEW - 8 Phases at a Glance")
    pdf.body("This roadmap takes you from zero graph knowledge to FAANG-ready in a structured progression. Each phase builds on the previous one.\n")

    widths = [15, 55, 60, 30]
    pdf.table_row(["Phase", "Topic", "Key Algorithms", "Status"], widths, bold=True, fill=True)
    rows = [
        ["1", "BFS / DFS / Connectivity", "BFS, DFS, Flood Fill, Multi-src BFS", "Done"],
        ["1.5", "Cycle Detection", "Parent-track, Rec-stack, Kahn's, UF", "Done"],
        ["2", "Topological Sort", "Kahn's BFS, DFS Topo Sort", "Done"],
        ["2.5", "Clone Graph", "HashMap + DFS/BFS", "Done"],
        ["3", "Shortest Path", "Dijkstra, Bellman-Ford, Floyd-Warshall", "Done"],
        ["4", "MST", "Prim's, Kruskal's, Union-Find (DSU)", "Done"],
        ["5", "Advanced DFS", "Bridges, Articulation Pts, Tarjan's SCC", "In Progress"],
        ["6", "Bipartite", "2-coloring BFS/DFS", "Pending"],
        ["7", "Adv. Shortest Path", "A*, 0-1 BFS, Johnson's", "Pending"],
        ["8", "Graph DP / SCC", "SCC + DP, Euler Path", "Pending"],
    ]
    for row in rows:
        pdf.table_row(row, widths)

    pdf.ln(5)
    pdf.sub_title("Learning Order (Follow This Exactly)")
    pdf.body(
        "Build Graph -> BFS/DFS -> Connectivity -> Cycle Detection -> "
        "Topological Sort -> Clone Graph -> Shortest Path (BFS -> Dijkstra -> "
        "Bellman-Ford -> Floyd-Warshall) -> MST (Prim's -> Kruskal's) -> "
        "Bridges/Articulation -> Bipartite -> Advanced"
    )

    # ══════════════════════════════════════════════════════════════════
    # SECTION 2: FOUNDATION - GRAPH REPRESENTATIONS
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("2. FOUNDATION - Graph Representations", 40, 100, 60)

    pdf.sub_title("The 2x2 Decision Grid")
    pdf.body("Every graph has two independent properties. Pick one from each row:\n")

    widths2 = [45, 50, 55]
    pdf.table_row(["Property", "Option A", "Option B"], widths2, bold=True, fill=True)
    pdf.table_row(["Direction", "Directed (one-way)", "Undirected (two-way)"], widths2)
    pdf.table_row(["Weight", "Unweighted (0/1)", "Weighted (has cost)"], widths2)
    pdf.ln(2)
    pdf.body("This gives 4 types: Directed-Unweighted, Directed-Weighted, Undirected-Unweighted, Undirected-Weighted.")
    pdf.body("Each can be stored as Adjacency List or Adjacency Matrix = 8 total combinations.\n")

    pdf.trick_box('MASTER TRICK: "Direction decides HOW MANY times you write. Weight decides WHAT you write."')

    pdf.sub_title("Adjacency List vs Adjacency Matrix")
    widths3 = [40, 55, 55]
    pdf.table_row(["Aspect", "Adjacency List", "Adjacency Matrix"], widths3, bold=True, fill=True)
    pdf.table_row(["Storage", "O(V + E)", "O(V^2)"], widths3)
    pdf.table_row(["Edge Lookup", "O(degree)", "O(1)"], widths3)
    pdf.table_row(["Add Edge", "O(1)", "O(1)"], widths3)
    pdf.table_row(["Best For", "Sparse graphs", "Dense graphs, V < 1000"], widths3)
    pdf.table_row(["Interview Default", "Almost always this", "Only if asked"], widths3)

    pdf.ln(3)
    pdf.sub_title("6 Memory Tricks for Graph Construction")
    tricks = [
        '1. Mirror Rule: Directed = 1 line of code (graph[u].append(v)). Undirected = mirror it (2 lines: graph[u].append(v), graph[v].append(u)).',
        '2. Count Your Appends: 1 append = directed. 2 appends = undirected.',
        '3. Backpack Analogy: Each node has a backpack. Unweighted = note "I know node X". Weighted = note "I know X, distance=5".',
        '4. Matrix Symmetry: Undirected matrix is always symmetric. Directed is NOT.',
        '5. Matrix Golden Rule: matrix[source][destination] = value. Row = FROM, Column = TO.',
        '6. What Do I Store? List: dest vs (dest, weight). Matrix: 1 vs weight_value.',
    ]
    for t in tricks:
        pdf.bullet(t)

    pdf.ln(3)
    pdf.sub_title("Universal Graph Builder Template")
    pdf.code_block(
        "def build_graph(n, edges, directed=False, weighted=False):\n"
        "    graph = [[] for _ in range(n)]\n"
        "    for edge in edges:\n"
        "        u, v = edge[0], edge[1]\n"
        "        w = edge[2] if weighted else 1\n"
        "        graph[u].append((v, w) if weighted else v)\n"
        "        if not directed:\n"
        "            graph[v].append((u, w) if weighted else u)\n"
        "    return graph"
    )

    # ══════════════════════════════════════════════════════════════════
    # SECTION 3: PHASE 1 - BFS / DFS / CONNECTIVITY
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("3. PHASE 1 - BFS, DFS & Connectivity", 0, 120, 100)

    pdf.sub_title("BFS vs DFS - The Two Fundamental Traversals")
    widths4 = [35, 55, 55]
    pdf.table_row(["Aspect", "BFS (Breadth-First)", "DFS (Depth-First)"], widths4, bold=True, fill=True)
    pdf.table_row(["Data Structure", "Queue (deque, FIFO)", "Stack / Recursion (LIFO)"], widths4)
    pdf.table_row(["Order", "Level by level", "Go deep, then backtrack"], widths4)
    pdf.table_row(["Shortest Path?", "YES (unweighted)", "NO"], widths4)
    pdf.table_row(["Use Cases", "Shortest path, level order", "Cycle detection, topo sort"], widths4)
    pdf.table_row(["Space", "O(V) worst case", "O(V) worst case"], widths4)
    pdf.table_row(["Time", "O(V + E)", "O(V + E)"], widths4)

    pdf.ln(3)
    pdf.sub_title("BFS Template")
    pdf.code_block(
        "from collections import deque\n\n"
        "def bfs(graph, start):\n"
        "    visited = set([start])\n"
        "    queue = deque([start])\n"
        "    while queue:\n"
        "        node = queue.popleft()\n"
        "        for neighbor in graph[node]:\n"
        "            if neighbor not in visited:\n"
        "                visited.add(neighbor)\n"
        "                queue.append(neighbor)"
    )

    pdf.sub_title("DFS Template")
    pdf.code_block(
        "def dfs(graph, node, visited):\n"
        "    visited.add(node)\n"
        "    for neighbor in graph[node]:\n"
        "        if neighbor not in visited:\n"
        "            dfs(graph, neighbor, visited)"
    )

    pdf.sub_title("Disconnected Graphs - The Outer Loop")
    pdf.body("If the graph might be disconnected, wrap BFS/DFS in a loop over all nodes:\n")
    pdf.code_block(
        "components = 0\n"
        "visited = set()\n"
        "for node in range(n):\n"
        "    if node not in visited:\n"
        "        dfs(graph, node, visited)  # or bfs\n"
        "        components += 1"
    )

    pdf.sub_title("Phase 1 Problems")

    # Problem 1
    pdf.sub_sub_title("1. Count Connected Components")
    pdf.body("Pattern: DFS outer loop. Count how many times you start a new DFS = number of components.")
    pdf.trick_box("Trick: Components = number of DFS calls from the outer loop.")

    # Problem 2
    pdf.sub_sub_title("2. Number of Provinces (LC 547)")
    pdf.body("Same as connected components but input is adjacency MATRIX. Scan row for neighbors.")
    pdf.code_block(
        "# Key difference: neighbors from matrix row\n"
        "for j in range(n):\n"
        "    if isConnected[node][j] == 1 and j not in visited:\n"
        "        dfs(j)"
    )

    # Problem 3
    pdf.sub_sub_title("3. Number of Islands (LC 200)")
    pdf.body("2D grid DFS. Each '1' cell is a node. 4-directional neighbors. Flood fill to mark visited.\n"
             "Count how many times you start a new DFS on an unvisited '1'.")
    pdf.code_block(
        "directions = [(0,1), (0,-1), (1,0), (-1,0)]  # R, L, D, U\n"
        "for dr, dc in directions:\n"
        "    nr, nc = r + dr, c + dc\n"
        "    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':\n"
        "        dfs(nr, nc)"
    )
    pdf.trick_box("Grid DFS trick: directions array [(0,1),(0,-1),(1,0),(-1,0)] replaces 4 if-statements.")

    # Problem 4
    pdf.sub_sub_title("4. Flood Fill (LC 733)")
    pdf.body("DFS from starting pixel. Replace old color with new color. Spread to same-color neighbors.")

    # Problem 5
    pdf.sub_sub_title("5. Rotting Oranges (LC 994) - Multi-Source BFS")
    pdf.body("All rotten oranges go into queue FIRST. Each BFS level = 1 minute. Track minutes.")
    pdf.trick_box('MULTI-SOURCE BFS: "Spread, Infection, Fire, Virus, Distance from nearest" = queue ALL sources first, BFS levels = time.')
    pdf.code_block(
        "queue = deque()\n"
        "for r in range(rows):\n"
        "    for c in range(cols):\n"
        "        if grid[r][c] == 2:  # all rotten oranges\n"
        "            queue.append((r, c))\n"
        "minutes = 0\n"
        "while queue:\n"
        "    for _ in range(len(queue)):  # one BFS level\n"
        "        r, c = queue.popleft()\n"
        "        for dr, dc in directions:\n"
        "            # spread to fresh oranges\n"
        "    minutes += 1"
    )

    # Problem 6
    pdf.sub_sub_title("6. Print All Paths (Source to Target)")
    pdf.body("DFS + Backtracking. Key: set visited[node] = False AFTER recursing to allow other paths.")
    pdf.code_block(
        "def all_paths(graph, curr, target, visited, path, result):\n"
        "    visited[curr] = True\n"
        "    path.append(curr)\n"
        "    if curr == target:\n"
        "        result.append(path[:])\n"
        "    else:\n"
        "        for neighbor in graph[curr]:\n"
        "            if not visited[neighbor]:\n"
        "                all_paths(graph, neighbor, target, visited, path, result)\n"
        "    path.pop()\n"
        "    visited[curr] = False  # BACKTRACK - the key line"
    )

    # ══════════════════════════════════════════════════════════════════
    # SECTION 4: CYCLE DETECTION
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("4. PHASE 1.5 - Cycle Detection", 140, 40, 40)

    pdf.trick_box("FAANG Decision Formula: Undirected -> parent tracking. Directed -> recursion stack. Disconnected -> loop all unvisited.")

    pdf.sub_title("Undirected Graph - 3 Methods")
    pdf.ln(1)

    pdf.sub_sub_title("Method 1: DFS + Parent Tracking (Most Common)")
    pdf.body("If a neighbor is visited AND it's not the parent who sent us here = CYCLE.\n")
    pdf.code_block(
        "def has_cycle_undirected(graph, node, visited, parent):\n"
        "    visited.add(node)\n"
        "    for neighbor in graph[node]:\n"
        "        if neighbor not in visited:\n"
        "            if has_cycle_undirected(graph, neighbor, visited, node):\n"
        "                return True\n"
        "        elif neighbor != parent:  # visited + not parent = CYCLE\n"
        "            return True\n"
        "    return False"
    )
    pdf.trick_box("Why check parent? In undirected, edge A-B means A sees B as visited (B saw A too). That's not a cycle, that's just the edge we came from.")

    pdf.sub_sub_title("Method 2: BFS + Parent Tracking")
    pdf.body("Same logic, queue stores (node, parent). If neighbor is visited and not parent = cycle.")

    pdf.sub_sub_title("Method 3: Union-Find (Best for Dynamic Edges)")
    pdf.body("For each edge (u, v): if find(u) == find(v) before union = cycle. Best for online queries.")

    pdf.ln(3)
    pdf.sub_title("Directed Graph - 2 Methods")

    pdf.sub_sub_title("Method 1: DFS + Recursion Stack (3-Color)")
    pdf.body("Two arrays: visited[] and rec_stack[]. A back edge to a node in rec_stack = CYCLE.\n"
             "Think of 3 colors: WHITE (unvisited), GRAY (in current path), BLACK (fully processed).\n")
    pdf.code_block(
        "def has_cycle_directed(graph, node, visited, rec_stack):\n"
        "    visited[node] = True\n"
        "    rec_stack[node] = True    # GRAY: in current DFS path\n"
        "    for neighbor in graph[node]:\n"
        "        if not visited[neighbor]:\n"
        "            if has_cycle_directed(graph, neighbor, visited, rec_stack):\n"
        "                return True\n"
        "        elif rec_stack[neighbor]:  # visited + in current path = CYCLE\n"
        "            return True\n"
        "    rec_stack[node] = False   # BLACK: done, remove from path\n"
        "    return False"
    )
    pdf.trick_box("Key difference from undirected: We need rec_stack (not parent). visited + in_current_path = back edge = cycle.")

    pdf.sub_sub_title("Method 2: Kahn's Algorithm (BFS Topological Sort)")
    pdf.body("If Kahn's processes fewer than V nodes, there's a cycle (stuck nodes have indegree > 0).")

    pdf.ln(3)
    pdf.sub_title("Common Mistakes")
    pdf.bullet("DON'T use recursion stack on undirected graphs (unnecessary, parent tracking is enough)")
    pdf.bullet("DON'T use parent tracking on directed graphs (misses cycles)")
    pdf.bullet("DON'T forget the outer loop for disconnected graphs")

    # ══════════════════════════════════════════════════════════════════
    # SECTION 5: TOPOLOGICAL SORT
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("5. PHASE 2 - Topological Sort & Course Scheduling", 100, 50, 150)

    pdf.sub_title("What is Topological Sort?")
    pdf.body(
        "A linear ordering of vertices in a DAG (Directed Acyclic Graph) such that for every "
        "edge u -> v, u comes before v in the ordering.\n\n"
        "Real-life: course prerequisites, build dependencies, task scheduling.\n"
    )
    pdf.trick_box("One-liner: Topological sort = valid order to do tasks when some must come before others. Only works on DAGs (no cycles).")

    pdf.sub_title("Kahn's Algorithm (BFS Topological Sort) - Preferred in Interviews")
    pdf.body("The idea: repeatedly remove nodes with no incoming edges (indegree = 0).\n")
    pdf.code_block(
        "from collections import deque\n\n"
        "def topological_sort(n, edges):\n"
        "    graph = [[] for _ in range(n)]\n"
        "    indegree = [0] * n\n"
        "    for u, v in edges:\n"
        "        graph[u].append(v)\n"
        "        indegree[v] += 1\n\n"
        "    queue = deque(c for c in range(n) if indegree[c] == 0)\n"
        "    order = []\n\n"
        "    while queue:\n"
        "        node = queue.popleft()\n"
        "        order.append(node)\n"
        "        for neighbor in graph[node]:\n"
        "            indegree[neighbor] -= 1\n"
        "            if indegree[neighbor] == 0:\n"
        "                queue.append(neighbor)\n\n"
        "    return order if len(order) == n else []  # empty = cycle"
    )
    pdf.trick_box("Sticky-note analogy: Tasks have sticky notes saying 'wait for X'. Start with tasks that have NO sticky notes (indegree 0). Complete them, peel their notes off others. Repeat.")

    pdf.sub_title("Phase 2 Problems")

    pdf.sub_sub_title("1. Course Schedule I (LC 207) - Can all courses be completed?")
    pdf.body("Convert to: Does the directed graph have a cycle? Use Kahn's. If processed < n = cycle = False.\n")

    pdf.sub_sub_title("2. Course Schedule II (LC 210) - Return a valid order")
    pdf.body("Exact same Kahn's code, but collect order. Return order if len == n, else empty list.\n")
    pdf.trick_box("CS-I vs CS-II: Same algorithm. CS-I returns True/False. CS-II returns the order list.")

    pdf.sub_sub_title("3. Alien Dictionary (LC 269)")
    pdf.body(
        "Two phases:\n"
        "Phase 1: Compare adjacent words character by character to find ordering rules (edges).\n"
        "Phase 2: Topological sort on the character graph.\n"
        "Edge case: if a longer word comes before its prefix (e.g., 'abc' before 'ab'), return empty.\n"
    )

    pdf.sub_sub_title("4. Complete All Courses with Dependencies")
    pdf.body(
        "Input: arrays a[] and b[] where a[i] must be taken before b[i].\n"
        "Same as Course Schedule I. Draw a[i] -> b[i], run Kahn's, check completed == n.\n"
    )

    # ══════════════════════════════════════════════════════════════════
    # SECTION 6: CLONE GRAPH
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("6. PHASE 2.5 - Clone Graph Pattern", 80, 40, 120)

    pdf.sub_title("Clone Graph (LC 133)")
    pdf.body("Deep copy a graph where nodes can have cycles. HashMap maps original -> clone.\n")
    pdf.trick_box('One-liner: "HashMap is your MEMORY - prevents duplicates AND handles cycles."')

    pdf.code_block(
        "def clone_graph(node):\n"
        "    if not node: return None\n"
        "    hashmap = {}\n\n"
        "    def dfs(node):\n"
        "        if node in hashmap:\n"
        "            return hashmap[node]  # already cloned\n"
        "        copy = Node(node.val)\n"
        "        hashmap[node] = copy     # store BEFORE recursing!\n"
        "        for neighbor in node.neighbors:\n"
        "            copy.neighbors.append(dfs(neighbor))\n"
        "        return copy\n\n"
        "    return dfs(node)"
    )

    pdf.sub_title("Critical Detail")
    pdf.body("Store clone in hashmap BEFORE recursing into neighbors. Otherwise, cycles cause infinite recursion.\n")

    pdf.sub_title("Same Pattern Appears In")
    pdf.bullet("Clone Graph (LC 133)")
    pdf.bullet("Copy List with Random Pointer (LC 138)")
    pdf.bullet("Deep Copy Binary Tree (LC 1485)")
    pdf.bullet("Clone N-ary Tree (LC 1490)")
    pdf.trick_box('Rule: "Deep copy + cycles or back-references = HashMap pattern"')

    # ══════════════════════════════════════════════════════════════════
    # SECTION 7: SHORTEST PATH
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("7. PHASE 3 - Shortest Path Algorithms", 150, 80, 0)

    pdf.sub_title("The Decision Tree (Memorize This!)")
    pdf.code_block(
        "Need shortest path?\n"
        "  |\n"
        "  +-- All pairs? --> YES --> Floyd-Warshall (V <= 400)\n"
        "  |\n"
        "  +-- NO (single source)\n"
        "        |\n"
        "        +-- Negative weights? --> YES --> Bellman-Ford\n"
        "        |\n"
        "        +-- NO\n"
        "              |\n"
        "              +-- Weighted? --> YES --> Dijkstra\n"
        "              |\n"
        "              +-- NO --> BFS"
    )
    pdf.trick_box('Quick Rule: "No weights? BFS. Positive weights? Dijkstra. Negative? Bellman-Ford. All pairs? Floyd-Warshall."')

    pdf.ln(2)
    widths5 = [38, 35, 38, 38]
    pdf.table_row(["Algorithm", "Graph Type", "Time", "Space"], widths5, bold=True, fill=True)
    pdf.table_row(["BFS", "Unweighted", "O(V + E)", "O(V)"], widths5)
    pdf.table_row(["Dijkstra", "Weighted (positive)", "O((V+E) log V)", "O(V)"], widths5)
    pdf.table_row(["Bellman-Ford", "Weighted (negative ok)", "O(V * E)", "O(V)"], widths5)
    pdf.table_row(["Floyd-Warshall", "All pairs", "O(V^3)", "O(V^2)"], widths5)

    # ─── BFS Shortest Path ───
    pdf.ln(3)
    pdf.sub_title("Algorithm 1: BFS Shortest Path (Unweighted)")
    pdf.body("First arrival at a node via BFS = shortest distance. Each edge has weight 1.\n")
    pdf.code_block(
        "def bfs_shortest(graph, src, n):\n"
        "    dist = [-1] * n\n"
        "    dist[src] = 0\n"
        "    queue = deque([src])\n"
        "    while queue:\n"
        "        node = queue.popleft()\n"
        "        for neighbor in graph[node]:\n"
        "            if dist[neighbor] == -1:\n"
        "                dist[neighbor] = dist[node] + 1\n"
        "                queue.append(neighbor)\n"
        "    return dist"
    )

    # ─── Dijkstra ───
    pdf.sub_title("Algorithm 2: Dijkstra (Positive Weights Only)")
    pdf.body("Greedy: always process the cheapest unvisited node. Uses a min-heap.\n")
    pdf.trick_box('Dijkstra in one line: "BFS with a priority queue, always picking the cheapest node first."')
    pdf.body("Heart of Dijkstra = RELAXATION:\n"
             "  if dist[node] + weight < dist[neighbor]: update dist[neighbor]\n")
    pdf.code_block(
        "import heapq\n\n"
        "def dijkstra(graph, src, n):\n"
        "    dist = [float('inf')] * n\n"
        "    dist[src] = 0\n"
        "    heap = [(0, src)]  # (cost, node)\n\n"
        "    while heap:\n"
        "        cost, node = heapq.heappop(heap)\n"
        "        if cost > dist[node]:  # stale entry, skip\n"
        "            continue\n"
        "        for neighbor, weight in graph[node]:\n"
        "            new_dist = dist[node] + weight\n"
        "            if new_dist < dist[neighbor]:\n"
        "                dist[neighbor] = new_dist\n"
        "                heapq.heappush(heap, (new_dist, neighbor))\n"
        "    return dist"
    )
    pdf.sub_sub_title("Why Dijkstra Fails with Negative Weights")
    pdf.body(
        "Dijkstra is greedy - once a node is popped, it's considered final. "
        "But a negative edge discovered later could provide a shorter path to an already-finalized node. "
        "Dijkstra would miss it.\n"
    )

    # ─── Bellman-Ford ───
    pdf.add_page()
    pdf.sub_title("Algorithm 3: Bellman-Ford (Handles Negative Weights)")
    pdf.body("Relax ALL edges, V-1 times. Guaranteed to find shortest paths.\n")
    pdf.trick_box('One-liner: "Relax ALL edges V-1 times. If the V-th pass still relaxes, there is a negative cycle."')
    pdf.body("Why V-1 iterations? The longest shortest path has at most V-1 edges. "
             "Each iteration propagates the shortest path by one more edge.\n")
    pdf.code_block(
        "def bellman_ford(n, edges, src):\n"
        "    dist = [float('inf')] * n\n"
        "    dist[src] = 0\n\n"
        "    for _ in range(n - 1):           # V-1 iterations\n"
        "        for u, v, w in edges:\n"
        "            if dist[u] != float('inf') and dist[u] + w < dist[v]:\n"
        "                dist[v] = dist[u] + w\n\n"
        "    # Negative cycle detection (V-th pass)\n"
        "    for u, v, w in edges:\n"
        "        if dist[u] != float('inf') and dist[u] + w < dist[v]:\n"
        "            return None  # negative cycle!\n"
        "    return dist"
    )

    pdf.sub_sub_title("LC 787: Cheapest Flights Within K Stops (Modified Bellman-Ford)")
    pdf.body("Run K+1 rounds instead of V-1. Use dist.copy() each round to prevent chaining.\n")
    pdf.trick_box("The COPY is the key! Without dist.copy(), one round chains multiple flights, exceeding K stops.")
    pdf.code_block(
        "def findCheapestPrice(n, flights, src, dst, k):\n"
        "    dist = [float('inf')] * n\n"
        "    dist[src] = 0\n"
        "    for _ in range(k + 1):      # K stops = K+1 flights\n"
        "        prev = dist[:]           # COPY prevents chaining\n"
        "        for u, v, w in flights:\n"
        "            if prev[u] + w < dist[v]:\n"
        "                dist[v] = prev[u] + w\n"
        "    return dist[dst] if dist[dst] != float('inf') else -1"
    )

    # ─── Floyd-Warshall ───
    pdf.sub_title("Algorithm 4: Floyd-Warshall (All Pairs)")
    pdf.body("For every pair (i,j), try every node k as a middle-man. Three nested loops.\n")
    pdf.trick_box('Core: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]). K is the OUTER loop!')
    pdf.code_block(
        "def floyd_warshall(n, dist):\n"
        "    # dist[i][j] = edge weight or inf\n"
        "    for k in range(n):           # k = intermediate node (OUTER!)\n"
        "        for i in range(n):\n"
        "            for j in range(n):\n"
        "                if dist[i][k] + dist[k][j] < dist[i][j]:\n"
        "                    dist[i][j] = dist[i][k] + dist[k][j]\n"
        "    # Negative cycle: dist[i][i] < 0 for some i\n"
        "    return dist"
    )
    pdf.sub_sub_title("Why K Must Be the Outer Loop (Interviewers Ask This!)")
    pdf.body(
        "k represents 'allowed intermediates so far.' With k as outer loop, when we consider "
        "node k as a shortcut, we've already computed shortest paths using nodes 0..k-1. "
        "If k were inner, we'd try shortcuts before knowing if they're optimal.\n"
    )

    # ══════════════════════════════════════════════════════════════════
    # SECTION 7.5: SNAKES AND LADDERS
    # ══════════════════════════════════════════════════════════════════
    pdf.sub_title("Snakes and Ladders (LC 909) - BFS Application")
    pdf.body(
        "Board cell = node. Dice roll = edge (up to 6 per node). Snake/ladder = forced teleport.\n"
        "Minimum dice rolls = shortest path in unweighted graph = BFS.\n"
    )
    pdf.trick_box("Each BFS level = one dice roll. Mark TELEPORT DESTINATION visited (not the snake/ladder cell). You never stay on a teleport cell.")
    pdf.code_block(
        "def snakes_and_ladders(n, moves):\n"
        "    queue = deque([0])  # 0-indexed\n"
        "    visited = [False] * n\n"
        "    visited[0] = True\n"
        "    rolls = 0\n"
        "    while queue:\n"
        "        for _ in range(len(queue)):  # one BFS level = one roll\n"
        "            curr = queue.popleft()\n"
        "            if curr == n - 1: return rolls\n"
        "            for dice in range(1, 7):\n"
        "                nxt = curr + dice\n"
        "                if nxt >= n: continue\n"
        "                if moves[nxt] != -1: nxt = moves[nxt]  # teleport\n"
        "                if not visited[nxt]:\n"
        "                    visited[nxt] = True\n"
        "                    queue.append(nxt)\n"
        "        rolls += 1\n"
        "    return -1"
    )

    # ══════════════════════════════════════════════════════════════════
    # SECTION 8: MST
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("8. PHASE 4 - Minimum Spanning Tree (MST)", 0, 100, 80)

    pdf.sub_title("What is an MST?")
    pdf.body(
        "A subset of edges that connects ALL vertices with minimum total weight, using exactly V-1 edges, "
        "with no cycles. Think: cheapest way to wire all houses together.\n"
    )
    pdf.body("3 Must-Know Properties: Spanning (all vertices), Tree (V-1 edges, no cycles), Minimum (smallest total weight).\n")

    pdf.sub_title("Prim's vs Kruskal's")
    widths6 = [35, 55, 55]
    pdf.table_row(["Aspect", "Prim's", "Kruskal's"], widths6, bold=True, fill=True)
    pdf.table_row(["Approach", "Grow tree from one node", "Pick cheapest edges globally"], widths6)
    pdf.table_row(["Data Structure", "Min-Heap + visited[]", "Sort edges + Union-Find"], widths6)
    pdf.table_row(["Best For", "Dense graphs (E ~ V^2)", "Sparse graphs (E ~ V)"], widths6)
    pdf.table_row(["Time", "O((V+E) log V)", "O(E log E)"], widths6)
    pdf.table_row(["Edge list given?", "Build adj list first", "Use directly"], widths6)

    pdf.trick_box("Prim's = Dijkstra but push EDGE WEIGHT, not total distance. Kruskal's = Sort edges, pick cheapest, skip if cycle (Union-Find).")

    pdf.sub_title("Prim's Algorithm")
    pdf.code_block(
        "import heapq\n\n"
        "def prims(graph, n):\n"
        "    visited = [False] * n\n"
        "    heap = [(0, 0)]  # (weight, start_node)\n"
        "    total = 0\n"
        "    edges_used = 0\n\n"
        "    while heap and edges_used < n:\n"
        "        weight, node = heapq.heappop(heap)\n"
        "        if visited[node]: continue\n"
        "        visited[node] = True\n"
        "        total += weight\n"
        "        edges_used += 1\n"
        "        for neighbor, w in graph[node]:\n"
        "            if not visited[neighbor]:\n"
        "                heapq.heappush(heap, (w, neighbor))\n"
        "    return total"
    )

    pdf.sub_title("Kruskal's Algorithm + Union-Find")
    pdf.code_block(
        "class UnionFind:\n"
        "    def __init__(self, n):\n"
        "        self.parent = list(range(n))\n"
        "        self.rank = [0] * n\n\n"
        "    def find(self, x):\n"
        "        if self.parent[x] != x:\n"
        "            self.parent[x] = self.find(self.parent[x])  # path compression\n"
        "        return self.parent[x]\n\n"
        "    def union(self, x, y):\n"
        "        px, py = self.find(x), self.find(y)\n"
        "        if px == py: return False  # already connected = cycle\n"
        "        if self.rank[px] < self.rank[py]: px, py = py, px\n"
        "        self.parent[py] = px\n"
        "        if self.rank[px] == self.rank[py]: self.rank[px] += 1\n"
        "        return True\n\n"
        "def kruskals(n, edges):\n"
        "    edges.sort(key=lambda x: x[2])  # sort by weight\n"
        "    uf = UnionFind(n)\n"
        "    total, count = 0, 0\n"
        "    for u, v, w in edges:\n"
        "        if uf.union(u, v):  # no cycle\n"
        "            total += w\n"
        "            count += 1\n"
        "            if count == n - 1: break\n"
        "    return total"
    )

    pdf.sub_sub_title("LC 1584: Min Cost to Connect All Points")
    pdf.body("Complete graph (every pair connected) with Manhattan distance |x1-x2| + |y1-y2|. Use Prim's (dense graph).")

    # ══════════════════════════════════════════════════════════════════
    # SECTION 9: ADVANCED DFS
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("9. PHASE 5 - Advanced DFS (Bridges & Articulation Points)", 100, 0, 100)

    pdf.sub_title("Tarjan's Algorithm - Two Key Arrays")
    pdf.body(
        "disc[node] = discovery timestamp (WHEN did DFS find this node?)\n"
        "low[node] = lowest disc reachable from this node's subtree via back edges.\n"
    )
    pdf.trick_box('Memory trick: disc = "discovery TIME". low = "how LOW (early) can I reach?"')

    pdf.sub_title("Bridges (Critical Connections) - LC 1192")
    pdf.body(
        "An edge (parent, child) is a bridge if removing it disconnects the graph.\n"
        "Condition: low[child] > disc[parent] (strictly greater).\n"
        "Meaning: child's subtree has NO back edge to parent or above. Removing the edge isolates the subtree.\n"
    )
    pdf.trick_box('Bridge analogy: "Can my child find its way back to me without our direct edge? If NO, our edge is a bridge."')
    pdf.code_block(
        "def find_bridges(graph, n):\n"
        "    disc = [-1] * n\n"
        "    low = [-1] * n\n"
        "    bridges = []\n"
        "    timer = [0]\n\n"
        "    def dfs(node, parent):\n"
        "        disc[node] = low[node] = timer[0]\n"
        "        timer[0] += 1\n"
        "        for neighbor in graph[node]:\n"
        "            if disc[neighbor] == -1:        # unvisited (tree edge)\n"
        "                dfs(neighbor, node)\n"
        "                low[node] = min(low[node], low[neighbor])\n"
        "                if low[neighbor] > disc[node]:  # BRIDGE\n"
        "                    bridges.append((node, neighbor))\n"
        "            elif neighbor != parent:         # back edge\n"
        "                low[node] = min(low[node], disc[neighbor])\n"
        "    \n"
        "    for i in range(n):\n"
        "        if disc[i] == -1:\n"
        "            dfs(i, -1)\n"
        "    return bridges"
    )

    pdf.sub_title("Articulation Points")
    pdf.body(
        "A vertex whose removal disconnects the graph.\n"
        "Condition: low[child] >= disc[node] (greater or EQUAL) + special case: root with 2+ DFS children.\n"
    )
    pdf.trick_box("Bridge: > (strictly greater). Articulation Point: >= (greater or equal). That's the ONLY difference in the condition.")

    pdf.sub_title("Updating low[] - The Rules")
    pdf.bullet("Tree edge (unvisited child): low[node] = min(low[node], low[child])")
    pdf.bullet("Back edge (visited ancestor, not parent): low[node] = min(low[node], disc[ancestor])")
    pdf.bold_body("\nIMPORTANT: Use disc[ancestor], NOT low[ancestor] for back edges!\n")

    # ══════════════════════════════════════════════════════════════════
    # SECTION 10: FAANG PROBLEM SET
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("10. FAANG PROBLEM SET - 30+ Must-Solve by Phase", 20, 20, 20)

    pdf.sub_title("Phase 1: BFS / DFS / Connectivity")
    w7 = [20, 70, 60]
    pdf.table_row(["LC #", "Problem", "Pattern"], w7, bold=True, fill=True)
    phase1 = [
        ["200", "Number of Islands", "DFS flood fill on grid"],
        ["547", "Number of Provinces", "DFS on adjacency matrix"],
        ["733", "Flood Fill", "DFS color replacement"],
        ["994", "Rotting Oranges", "Multi-source BFS"],
        ["695", "Max Area of Island", "DFS + area tracking"],
        ["1091", "Shortest Path in Binary Matrix", "BFS on grid"],
        ["127", "Word Ladder", "BFS word transformation"],
        ["542", "01 Matrix", "Multi-source BFS"],
        ["286", "Walls and Gates", "Multi-source BFS"],
        ["797", "All Paths From Source to Target", "DFS + backtracking"],
    ]
    for row in phase1:
        pdf.table_row(row, w7)

    pdf.ln(4)
    pdf.sub_title("Phase 1.5: Cycle Detection")
    pdf.table_row(["LC #", "Problem", "Pattern"], w7, bold=True, fill=True)
    phase15 = [
        ["--", "Cycle in Undirected Graph", "DFS + parent tracking"],
        ["--", "Cycle in Directed Graph", "DFS + recursion stack"],
        ["684", "Redundant Connection", "Union-Find cycle detection"],
    ]
    for row in phase15:
        pdf.table_row(row, w7)

    pdf.ln(4)
    pdf.sub_title("Phase 2: Topological Sort")
    pdf.table_row(["LC #", "Problem", "Pattern"], w7, bold=True, fill=True)
    phase2 = [
        ["207", "Course Schedule I", "Kahn's BFS (cycle detection)"],
        ["210", "Course Schedule II", "Kahn's BFS (return order)"],
        ["269", "Alien Dictionary", "Build graph + topo sort"],
        ["--", "Complete All Courses (IK)", "Same as LC 207"],
    ]
    for row in phase2:
        pdf.table_row(row, w7)

    pdf.ln(4)
    pdf.sub_title("Phase 2.5: Clone Graph")
    pdf.table_row(["LC #", "Problem", "Pattern"], w7, bold=True, fill=True)
    phase25 = [
        ["133", "Clone Graph", "HashMap + DFS"],
        ["138", "Copy List with Random Pointer", "Same HashMap pattern"],
    ]
    for row in phase25:
        pdf.table_row(row, w7)

    pdf.ln(4)
    pdf.sub_title("Phase 3: Shortest Path")
    pdf.table_row(["LC #", "Problem", "Pattern"], w7, bold=True, fill=True)
    phase3 = [
        ["743", "Network Delay Time", "Dijkstra (single source)"],
        ["787", "Cheapest Flights Within K Stops", "Modified Bellman-Ford / Dijkstra"],
        ["1631", "Path With Minimum Effort", "Dijkstra on grid"],
        ["778", "Swim in Rising Water", "Dijkstra / Binary Search + BFS"],
        ["1334", "Find City With Smallest Neighbors", "Floyd-Warshall"],
        ["909", "Snakes and Ladders", "BFS (unweighted shortest path)"],
        ["1976", "Number of Ways to Arrive at Destination", "Dijkstra + counting"],
        ["847", "Shortest Path Visiting All Nodes", "BFS + bitmask"],
    ]
    for row in phase3:
        pdf.table_row(row, w7)

    pdf.add_page()
    pdf.sub_title("Phase 4: Minimum Spanning Tree")
    pdf.table_row(["LC #", "Problem", "Pattern"], w7, bold=True, fill=True)
    phase4 = [
        ["1584", "Min Cost to Connect All Points", "Prim's (dense/complete graph)"],
        ["1135", "Connecting Cities With Min Cost", "Kruskal's / Prim's"],
        ["1168", "Optimize Water Distribution", "Virtual node + MST"],
        ["684", "Redundant Connection", "Union-Find"],
    ]
    for row in phase4:
        pdf.table_row(row, w7)

    pdf.ln(4)
    pdf.sub_title("Phase 5: Advanced DFS")
    pdf.table_row(["LC #", "Problem", "Pattern"], w7, bold=True, fill=True)
    phase5 = [
        ["1192", "Critical Connections in Network", "Tarjan's bridges"],
        ["--", "Articulation Points", "Tarjan's (>= condition)"],
    ]
    for row in phase5:
        pdf.table_row(row, w7)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 11: MASTER CHEAT SHEET
    # ══════════════════════════════════════════════════════════════════
    pdf.add_page()
    pdf.section_title("11. MASTER CHEAT SHEET - Tricks, Templates & Decision Trees", 180, 50, 50)

    pdf.sub_title("15 Memory Tricks to Remember Forever")
    tricks_list = [
        '1. "Direction decides HOW MANY appends. Weight decides WHAT you append."',
        '2. "Mirror Rule: Directed = 1 append. Undirected = 2 appends."',
        '3. "HashMap is your MEMORY - prevents duplicates AND handles cycles." (Clone Graph)',
        '4. "Prim = Dijkstra but push EDGE WEIGHT, not total distance."',
        '5. "Kruskal = Sort edges, pick cheapest, skip if Union-Find says cycle."',
        '6. "No weights? BFS. Positive? Dijkstra. Negative? Bellman-Ford."',
        '7. "Relax ALL edges V-1 times. V-th pass still relaxes = negative cycle."',
        '8. "Floyd-Warshall: 3 nested loops k-i-j. K must be OUTER."',
        '9. "disc = discovery TIME. low = how LOW can I reach?"',
        '10. "Can my child find way back without our edge? No = bridge."',
        '11. "Bridge: >. Articulation Point: >=. Only difference."',
        '12. "Undirected cycle: parent tracking. Directed cycle: recursion stack."',
        '13. "Spread/Infection/Fire = Multi-source BFS (queue ALL sources first)."',
        '14. "Deep copy + cycles = HashMap pattern."',
        '15. "Bellman-Ford + K+1 rounds + dist.copy() = flights with K stops."',
    ]
    for t in tricks_list:
        pdf.bullet(t)

    pdf.ln(4)
    pdf.sub_title("Pattern Recognition Quick Reference")
    w8 = [75, 75]
    pdf.table_row(["When you see...", "Think this..."], w8, bold=True, fill=True)
    patterns = [
        ['"Minimum steps/moves"', "BFS (unweighted shortest path)"],
        ['"Cheapest/shortest with weights"', "Dijkstra"],
        ['"With negative weights"', "Bellman-Ford"],
        ['"All pairs shortest"', "Floyd-Warshall (V<=400)"],
        ['"Must do X before Y"', "Topological Sort (Kahn's)"],
        ['"Is valid ordering possible?"', "Cycle detection"],
        ['"Count connected groups"', "DFS/BFS outer loop"],
        ['"Spread/infection/fire"', "Multi-source BFS"],
        ['"Grid traversal"', "DFS/BFS with directions array"],
        ['"Deep copy graph/list"', "HashMap (original -> clone)"],
        ['"Cheapest to connect all"', "MST (Prim's or Kruskal's)"],
        ['"Removing edge disconnects?"', "Bridges (Tarjan's)"],
        ['"Removing node disconnects?"', "Articulation Points (Tarjan's)"],
        ['"With limited stops/hops"', "Modified Bellman-Ford (K+1 rounds)"],
        ['"Board game, min dice rolls"', "BFS (each level = one roll)"],
    ]
    for p in patterns:
        pdf.table_row(p, w8)

    pdf.ln(4)
    pdf.sub_title("Complexity Quick Reference")
    w9 = [45, 35, 35, 35]
    pdf.table_row(["Algorithm", "Time", "Space", "Notes"], w9, bold=True, fill=True)
    complexities = [
        ["BFS / DFS", "O(V+E)", "O(V)", "Foundation"],
        ["Topological Sort", "O(V+E)", "O(V+E)", "DAGs only"],
        ["Dijkstra (heap)", "O((V+E)logV)", "O(V)", "No neg weights"],
        ["Bellman-Ford", "O(V*E)", "O(V)", "Handles neg weights"],
        ["Floyd-Warshall", "O(V^3)", "O(V^2)", "All pairs, V<=400"],
        ["Prim's (heap)", "O((V+E)logV)", "O(V)", "Dense graphs"],
        ["Kruskal's", "O(E log E)", "O(V)", "Sparse graphs"],
        ["Tarjan's", "O(V+E)", "O(V)", "Bridges / APs"],
        ["Union-Find", "O(alpha(N))", "O(V)", "Nearly O(1)"],
    ]
    for c in complexities:
        pdf.table_row(c, w9)

    pdf.ln(5)
    pdf.sub_title("The Ultimate Interview Checklist")
    checklist = [
        "Can I identify the graph type? (directed/undirected, weighted/unweighted)",
        "Do I know the representation? (adjacency list default, matrix if asked)",
        "Can I handle disconnected components? (outer loop over all nodes)",
        "Can I detect cycles? (parent for undirected, rec_stack for directed)",
        "Can I find shortest path? (BFS/Dijkstra/Bellman-Ford decision tree)",
        "Can I find MST? (Prim's for dense, Kruskal's for sparse)",
        "Can I find bridges/APs? (Tarjan's disc[] and low[])",
        "Can I do topological sort? (Kahn's with indegree queue)",
        "Can I clone a graph? (HashMap prevents cycles and duplicates)",
        "Can I explain TIME and SPACE complexity for each algorithm?",
    ]
    for item in checklist:
        pdf.bullet(item)

    return pdf


if __name__ == "__main__":
    import os
    pdf = build_pdf()
    output_path = os.path.join(os.path.dirname(__file__), "Graph_DSA_FAANG_Guide.pdf")
    pdf.output(output_path)
    print(f"PDF generated: {output_path}")
