"""
================================================================================
CLONE GRAPH (LeetCode 133) — Complete Interview Guide
================================================================================

PATTERN NAME: DFS/BFS + HashMap (Old Node → New Node)
DIFFICULTY: Medium
FREQUENCY: Very High (Amazon, Facebook, Google, Microsoft)

================================================================================
THE ONE-LINE TRICK TO REMEMBER:
================================================================================

    "HashMap is your MEMORY — it prevents duplicates AND handles cycles."

    Think: visited set + result storage = ONE dictionary doing BOTH jobs.

================================================================================
WHERE THIS EXACT PATTERN REPEATS (same logic, different structure):
================================================================================

    1. Clone Graph (LeetCode 133)
    2. Copy List with Random Pointer (LeetCode 138)
    3. Deep Copy of Binary Tree with Random Pointer (LeetCode 1485)
    4. Clone N-ary Tree (LeetCode 1490)

    RULE: Anytime you see "deep copy" + "cycles or back-references" → HashMap pattern.

================================================================================
PROBLEM IN 10 SECONDS:
================================================================================

    Given ONE node of an undirected connected graph → return deep copy of ENTIRE graph.

    class Node:
        def __init__(self, val=0, neighbors=None):
            self.val = val
            self.neighbors = neighbors if neighbors else []

    Example:
        1 --- 2
        |     |
        4 --- 3

    Input: node pointing to 1
    Output: completely new graph with same structure, different memory addresses.

================================================================================
WHY NAIVE APPROACH FAILS (2 reasons — interviewers test this understanding):
================================================================================

    REASON 1: DUPLICATE NODES
    ─────────────────────────
    If you just do: copy.neighbors.append(Node(neighbor.val))
    Every time you visit a node, you create a NEW copy.
    Node 1 gets cloned 3 times → broken graph, wrong answer.

    REASON 2: INFINITE LOOP (cycles)
    ─────────────────────────────────
    Graph: 1 → 2 → 3 → 4 → 1 → 2 → 3 → ... (never stops)
    Without tracking "already visited", DFS loops forever.

    KEY INSIGHT: The HashMap solves BOTH problems simultaneously!
        - Prevents infinite loops (acts as visited set)
        - Prevents duplicate nodes (returns existing clone)

================================================================================
ALGORITHM — 3 STEPS (memorize this):
================================================================================

    Step 1: If node already in HashMap → RETURN its clone (stops cycles + reuse)
    Step 2: Create new node, IMMEDIATELY store in HashMap (before recursing!)
    Step 3: For each neighbor → recurse, append result to clone's neighbors

    WHY store BEFORE recursing?
    → Because a cycle might bring you back to this node mid-recursion.
    → If it's already in the map, you safely return without infinite loop.

================================================================================
VISUAL WALKTHROUGH:
================================================================================

    Graph: 1 --- 2       HashMap (clone): {}
           |     |
           4 --- 3

    DFS(1): clone = {1: 1'}  → recurse neighbors [2, 4]
      DFS(2): clone = {1: 1', 2: 2'} → recurse neighbors [1, 3]
        DFS(1): 1 is in clone → return 1' ✓ (cycle handled!)
        DFS(3): clone = {1: 1', 2: 2', 3: 3'} → recurse neighbors [2, 4]
          DFS(2): 2 is in clone → return 2' ✓
          DFS(4): clone = {1: 1', 2: 2', 3: 3', 4: 4'} → recurse neighbors [1, 3]
            DFS(1): return 1' ✓
            DFS(3): return 3' ✓
          return 4'
        return 3'
      return 2'
      DFS(4): 4 is in clone → return 4' ✓
    return 1' ← FINAL ANSWER

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(V + E) — visit every node once, traverse every edge once
    Space: O(V) — HashMap stores V nodes + recursion stack up to V deep

================================================================================
CODING INTERVIEW TIPS:
================================================================================

    TIP 1: Start by asking "Can the input be null?" → Handle edge case first.

    TIP 2: Tell interviewer: "I need a HashMap to map original → clone because:
            (a) it acts as my visited set to handle cycles
            (b) it ensures each node is cloned exactly once"

    TIP 3: Store clone in map BEFORE recursing into neighbors.
            This is the #1 bug candidates make — they store AFTER and get infinite loop.

    TIP 4: If interviewer asks for BFS version → same HashMap, just use a queue
            instead of recursion. Mention you know both approaches.

    TIP 5: If asked "what if graph is disconnected?" →
            This problem guarantees connected, but if not, you'd need access to all
            nodes (e.g., a list) and clone each component separately.

    TIP 6: Time yourself — this should take < 5 minutes to code in an interview.
            If it takes longer, practice the pattern more.

================================================================================
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ══════════════════════════════════════════════════════════════════════════════
# SOLUTION 1: DFS (Recursive) — Most common in interviews
# ══════════════════════════════════════════════════════════════════════════════
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        clone = {}  # old_node → new_node (this is your MEMORY)

        def dfs(curr):
            if curr in clone:          # Already cloned? Return it. (handles cycles)
                return clone[curr]

            copy = Node(curr.val)      # Create clone
            clone[curr] = copy         # Store IMMEDIATELY (before recursing!)

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))  # Recurse & connect

            return copy

        return dfs(node)


# ══════════════════════════════════════════════════════════════════════════════
# SOLUTION 2: BFS (Iterative) — Good to mention as alternative
# ══════════════════════════════════════════════════════════════════════════════
from collections import deque

class SolutionBFS:
    def cloneGraph(self, node):
        if not node:
            return None

        clone = {node: Node(node.val)}  # Start by cloning the first node
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clone:           # Not yet cloned
                    clone[neighbor] = Node(neighbor.val)  # Clone it
                    queue.append(neighbor)           # Add to queue for processing
                clone[curr].neighbors.append(clone[neighbor])  # Connect

        return clone[node]


# ══════════════════════════════════════════════════════════════════════════════
# QUICK RECALL CHEAT SHEET (read this 1 min before interview):
# ══════════════════════════════════════════════════════════════════════════════
#
#   Pattern:  clone = {}  →  if seen return clone[node]  →  create & store  →  recurse neighbors
#   Edge case: None input → return None
#   Complexity: O(V+E) time, O(V) space
#   Key phrase: "HashMap maps original to clone — acts as visited + storage"
#

'''
Interview Pattern to Memorize ⭐

This is the template you should recognize instantly:

def dfs(node):

    if node in hashmap:
        return hashmap[node]

    copy = Node(node.val)

    hashmap[node] = copy

    for neighbour in node.neighbors:
        copy.neighbors.append(dfs(neighbour))

    return copy

'''
