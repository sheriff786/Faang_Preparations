
"""
================================================================================
================================================================================
        0/1 KNAPSACK — COMPLETE FAANG INTERVIEW GUIDE
================================================================================
================================================================================

PATTERN: 0/1 Knapsack (the MOTHER of all DP problems)
DIFFICULTY: Medium
FREQUENCY: Very High (Amazon, Google, Microsoft, Goldman Sachs, Facebook)

================================================================================
WHY THIS PROBLEM IS #1 IN DP:
================================================================================

    The 0/1 Knapsack pattern is the foundation for 6+ other DP problems:

    ┌─────────────────────────────────────────────────────────────┐
    │                    0/1 KNAPSACK                              │
    │                        │                                    │
    │    ┌───────────┬───────┼───────┬──────────┬──────────┐      │
    │    ▼           ▼       ▼       ▼          ▼          ▼      │
    │ Subset      Equal   Count   Minimum    Target    #Subsets   │
    │  Sum        Sum    Subset    Subset      Sum      Given     │
    │           Partition  Sum    Sum Diff              Diff      │
    └─────────────────────────────────────────────────────────────┘

    Learn Knapsack ONCE → solve 6 problems automatically.

================================================================================
PROBLEM IN 10 SECONDS:
================================================================================

    Given: a bag with weight capacity W, and n items each with weight & value.
    Goal:  pick items to MAXIMIZE total value WITHOUT exceeding weight W.
    Rule:  each item can be picked AT MOST ONCE (that's the "0/1" part).

    Think: you're a thief with a bag. What do you steal to maximize profit?

================================================================================
ONE-LINE TRICK TO REMEMBER:
================================================================================

    "For each item: either PICK it (add value, reduce capacity) or SKIP it.
     Take the MAX of both choices."

================================================================================
THE 3-STEP DP RECIPE (works for ALL knapsack-family problems):
================================================================================

    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │  Step 1: IDENTIFY what changes → those become DP dimensions │
    │          (here: n items remaining, w capacity remaining)    │
    │                                                             │
    │  Step 2: WRITE the choice diagram                           │
    │          (here: pick item OR skip item)                     │
    │                                                             │
    │  Step 3: CHOOSE optimization                                │
    │          (here: max of pick vs skip)                        │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘

================================================================================
THE CHOICE DIAGRAM (draw this in every interview):
================================================================================

    For each item i with weight wt[i] and value val[i]:

                    item i
                   /      \\
                  /        \\
        wt[i] <= W?        wt[i] > W?
        (can pick)         (too heavy)
         /      \\              |
        /        \\             |
     PICK       SKIP          SKIP
       |          |             |
   val[i] +      move to       move to
   solve(W -     next item     next item
   wt[i], n-1)   solve(W,n-1)  solve(W,n-1)

    If can pick: answer = max(PICK, SKIP)
    If too heavy: answer = SKIP (only option)

================================================================================
EXAMPLE:
================================================================================

    W = 7 (bag capacity)
    items:  weight = [1, 3, 4, 5]
            value  = [1, 4, 5, 7]

    Item │ Weight │ Value │ Value/Weight
    ─────┼────────┼───────┼─────────────
     0   │   1    │   1   │    1.0
     1   │   3    │   4   │    1.33
     2   │   4    │   5   │    1.25
     3   │   5    │   7   │    1.40

    Greedy (by value/weight ratio) would pick items 3+1 = weight 8 > 7. WRONG!
    That's why greedy fails and we need DP.

    Optimal: pick items 1 + 2 → weight = 3+4 = 7, value = 4+5 = 9
    OR: pick items 1 + 3? → weight = 3+5 = 8 > 7. Doesn't fit.
    OR: pick item 3 + 0? → weight = 5+1 = 6, value = 7+1 = 8. Fits but less.

    Answer: 9 (items 1 and 2)

================================================================================
APPROACH 1: RECURSION (Brute Force)
================================================================================

    Idea: try all possible subsets, pick the one with max value that fits.
    For each item: pick or skip → 2^n total subsets → O(2^n)

    Base case: n == 0 (no items left) OR w == 0 (bag full) → return 0

    TEMPLATE:
        def knapsack(wt, val, w, n):
            if n == 0 or w == 0:
                return 0
            if wt[n-1] <= w:   # can pick
                pick = val[n-1] + knapsack(wt, val, w - wt[n-1], n-1)
                skip = knapsack(wt, val, w, n-1)
                return max(pick, skip)
            else:              # too heavy, must skip
                return knapsack(wt, val, w, n-1)

    Time:  O(2^n) — exponential (each item has 2 choices)
    Space: O(n) — recursion stack depth

    WHY THIS IS SLOW: same subproblems solved repeatedly.
    Example: knapsack(w=4, n=2) might be called from multiple branches.

================================================================================
APPROACH 2: MEMOIZATION (Top-Down DP)
================================================================================

    Idea: same recursion, but CACHE results in a 2D table.
    Before solving, check: "Did I already solve this (n, w) pair?"

    WHAT CHANGES in recursion? → n and w
    So memo table is: memo[n+1][w+1] initialized to -1

    CONVERSION RECIPE (recursion → memoization, 3 lines):
        1. Create memo[n+1][w+1] = -1
        2. Before computing: if memo[n][w] != -1: return memo[n][w]
        3. Before returning: memo[n][w] = result

    Time:  O(n * W) — each (n, w) pair computed once
    Space: O(n * W) — memo table + O(n) recursion stack

================================================================================
APPROACH 3: BOTTOM-UP DP (Tabulation) — INTERVIEW PREFERRED
================================================================================

    Idea: build solution from smallest subproblems up.
    dp[i][j] = max value using first i items with capacity j.

    INITIALIZATION:
        dp[0][j] = 0 for all j  (0 items = 0 value)
        dp[i][0] = 0 for all i  (0 capacity = 0 value)

    TRANSITION:
        if wt[i-1] <= j:
            dp[i][j] = max(val[i-1] + dp[i-1][j - wt[i-1]],  # pick
                           dp[i-1][j])                          # skip
        else:
            dp[i][j] = dp[i-1][j]                               # can't pick

    ANSWER: dp[n][W]

    Time:  O(n * W)
    Space: O(n * W)

================================================================================
DP TABLE TRACE (THE INTERVIEW GOLD — draw this on whiteboard):
================================================================================

    W = 7, wt = [1, 3, 4, 5], val = [1, 4, 5, 7]

    dp[i][j] = max value using items 0..i-1 with capacity j

         j→  0    1    2    3    4    5    6    7
    i=0      0    0    0    0    0    0    0    0   ← no items
    i=1      0    1    1    1    1    1    1    1   ← item 0 (w=1,v=1)
    i=2      0    1    1    4    5    5    5    5   ← items 0-1 (w=3,v=4)
    i=3      0    1    1    4    5    6    6    9   ← items 0-2 (w=4,v=5)
    i=4      0    1    1    4    5    7    8    9   ← items 0-3 (w=5,v=7)

    Answer: dp[4][7] = 9

    HOW TO READ THE TABLE:
        dp[3][7] = 9 means: using items {0,1,2} with capacity 7, max value = 9
        This came from: pick item 2 (v=5) + dp[2][7-4] = dp[2][3] = 4 → 5+4 = 9

    HOW TO TRACE BACK WHICH ITEMS WERE PICKED:
        Start at dp[4][7] = 9
        Is dp[4][7] == dp[3][7]? → 9 == 9 → YES → item 3 was NOT picked
        Move to dp[3][7] = 9
        Is dp[3][7] == dp[2][7]? → 9 == 5 → NO → item 2 WAS picked!
        Remaining capacity: 7 - wt[2] = 7-4 = 3. Move to dp[2][3]
        Is dp[2][3] == dp[1][3]? → 4 == 1 → NO → item 1 WAS picked!
        Remaining capacity: 3 - wt[1] = 3-3 = 0. Move to dp[1][0]
        dp[1][0] = 0 → done.

        Items picked: 1, 2 (values 4+5 = 9, weights 3+4 = 7) ✓

================================================================================
THE KNAPSACK FAMILY — 6 VARIATIONS (ALL from same template):
================================================================================

    ┌──────────────────────┬──────────────────────────────────────────────┐
    │ Problem              │ How it differs from base 0/1 Knapsack        │
    ├──────────────────────┼──────────────────────────────────────────────┤
    │ Subset Sum           │ val = wt, W = target sum                     │
    │                      │ "Can we make exact sum S from array?"        │
    │                      │ dp[i][j] = True/False instead of max value   │
    ├──────────────────────┼──────────────────────────────────────────────┤
    │ Equal Sum Partition   │ Find if array can split into 2 equal halves  │
    │                      │ = Subset Sum with target = totalSum / 2      │
    │                      │ If totalSum is odd → impossible              │
    ├──────────────────────┼──────────────────────────────────────────────┤
    │ Count of Subset Sum  │ How MANY subsets sum to target?              │
    │                      │ dp[i][j] = count (use + instead of max)     │
    │                      │ pick + skip instead of max(pick, skip)       │
    ├──────────────────────┼──────────────────────────────────────────────┤
    │ Minimum Subset Sum   │ Partition into 2 subsets, minimize |S1-S2|   │
    │ Difference           │ = find all achievable sums in last row of    │
    │                      │   subset-sum DP, then min(total - 2*s)       │
    ├──────────────────────┼──────────────────────────────────────────────┤
    │ Target Sum (+/-)     │ Assign + or - to each element, reach target  │
    │                      │ = Count subsets with sum = (total+target)/2  │
    ├──────────────────────┼──────────────────────────────────────────────┤
    │ #Subsets Given Diff  │ Find subsets where S1-S2 = diff              │
    │                      │ = Count subsets with sum = (total+diff)/2    │
    └──────────────────────┴──────────────────────────────────────────────┘

================================================================================
HOW TO IDENTIFY "THIS IS A KNAPSACK PROBLEM" IN INTERVIEWS:
================================================================================

    PATTERN RECOGNITION:

    See this?                                → Think this:
    ────────────────────────────────────────────────────────────────────
    "Maximize value with weight limit"       → 0/1 Knapsack (direct)
    "Can you make exact sum from array?"     → Subset Sum
    "Split array into 2 equal halves?"       → Equal Sum Partition
    "How many ways to reach sum?"            → Count of Subset Sum
    "Minimize difference of 2 partitions"    → Min Subset Sum Diff
    "Assign +/- to reach target"            → Target Sum
    "Pick or skip each item"                → Knapsack family
    "Each item used AT MOST once"           → 0/1 (not unbounded)
    "Each item can be used UNLIMITED times" → Unbounded Knapsack

================================================================================
0/1 vs UNBOUNDED vs FRACTIONAL KNAPSACK:
================================================================================

    ┌──────────────────┬────────────────┬────────────────┬────────────────┐
    │                  │ 0/1 Knapsack   │ Unbounded      │ Fractional     │
    ├──────────────────┼────────────────┼────────────────┼────────────────┤
    │ Item usage       │ At most once   │ Unlimited      │ Can take parts │
    │ Technique        │ DP             │ DP             │ Greedy         │
    │ Key difference   │ dp[i-1][...]   │ dp[i][...]     │ Sort by v/w    │
    │ in transition    │ (prev row)     │ (same row)     │ take greedily  │
    │ Time             │ O(n*W)         │ O(n*W)         │ O(n log n)     │
    │ Interview freq   │ Very High      │ High           │ Medium         │
    └──────────────────┴────────────────┴────────────────┴────────────────┘

    THE ONE KEY DIFFERENCE between 0/1 and Unbounded:
        0/1:       dp[i][j] uses dp[i-1][j - wt[i-1]]  ← previous row (item used once)
        Unbounded: dp[i][j] uses dp[i][j - wt[i-1]]    ← SAME row (item can repeat)

================================================================================
RECURSION → MEMOIZATION → BOTTOM-UP (The 3-Step Conversion):
================================================================================

    Step 1: Write pure recursion with base case + choice diagram
    Step 2: Add memo table for CHANGING variables (n, W here)
            → Check memo before computing, store result before returning
    Step 3: Convert to iterative table-filling
            → Row = items (0 to n), Column = capacity (0 to W)
            → Fill row by row, each cell uses previous row's values

    CONVERSION TRICK:
    ┌──────────────────────────────────────────────────────────────────┐
    │ Recursion:    if n==0 or w==0: return 0                         │
    │                                                                  │
    │ Becomes in Bottom-Up:                                            │
    │               dp[0][j] = 0  (first row = 0)                     │
    │               dp[i][0] = 0  (first column = 0)                  │
    │                                                                  │
    │ Recursion:    max(val[n-1] + f(w-wt[n-1], n-1), f(w, n-1))     │
    │                                                                  │
    │ Becomes:      dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]],    │
    │                              dp[i-1][j])                         │
    │                                                                  │
    │ n → i,  w → j,  f(...) → dp[...][...]                          │
    └──────────────────────────────────────────────────────────────────┘

================================================================================
SPACE OPTIMIZATION (O(n*W) → O(W)):
================================================================================

    Since dp[i][j] only depends on dp[i-1][...] (previous row),
    we only need ONE row + temp, or traverse columns RIGHT TO LEFT.

    1D DP (space optimized):
        dp = [0] * (W + 1)
        for i in range(n):
            for j in range(W, wt[i] - 1, -1):   # RIGHT TO LEFT!
                dp[j] = max(dp[j], val[i] + dp[j - wt[i]])

    WHY RIGHT TO LEFT?
        If we go left to right, dp[j - wt[i]] might already be updated
        in this iteration = using item i TWICE. Right to left ensures we
        use the "previous row" values.

    For UNBOUNDED knapsack: go LEFT TO RIGHT (we WANT to reuse items).

================================================================================
FAANG INTERVIEW TIPS:
================================================================================

    TIP 1: ALWAYS start with the choice diagram on the whiteboard.
            Interviewer sees you have a structured approach.

    TIP 2: "How did you identify this as knapsack?"
            → "I see pick/skip decision + constraint (capacity/sum)."

    TIP 3: Base case = "smallest valid input."
            → 0 items = 0 value. 0 capacity = 0 value. Always both.

    TIP 4: If asked "optimize space," mention the 1D right-to-left trick.
            Shows advanced knowledge.

    TIP 5: The DP table dimensions = changing variables in recursion.
            If 2 things change (n, W), table is 2D.
            If 3 things change, table is 3D. And so on.

    TIP 6: "Why not greedy?" → Because item with best value/weight ratio
            might not lead to global optimum. Items are indivisible.
            (Greedy ONLY works for fractional knapsack.)

    TIP 7: Time complexity O(n*W) is PSEUDO-POLYNOMIAL.
            It's polynomial in the VALUE of W, not in the number of BITS.
            Interviewers sometimes ask this distinction.

    TIP 8: Common follow-ups:
            → "Print which items were picked" → trace back through dp table
            → "What if items can repeat?" → unbounded (use same row)
            → "What if you must pick exactly k items?" → add 3rd dimension

================================================================================
QUICK REVISION CHEAT SHEET:
================================================================================

    IDENTIFICATION:
        "Pick or skip" + "capacity/sum constraint" = Knapsack family

    CHOICE DIAGRAM:
        if wt[i] <= W: answer = max(pick, skip)
        else:          answer = skip

    3 APPROACHES:
        Recursion:    O(2^n) time, O(n) space
        Memoization:  O(n*W) time, O(n*W) space
        Bottom-Up:    O(n*W) time, O(n*W) space → can optimize to O(W)

    BOTTOM-UP TEMPLATE:
        dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])

    SPACE OPTIMIZED:
        for i in range(n):
            for j in range(W, wt[i]-1, -1):  # RIGHT TO LEFT
                dp[j] = max(dp[j], val[i] + dp[j - wt[i]])

    KEY DIFFERENCES:
        0/1 Knapsack:       dp[i-1][j-w] (prev row) + right-to-left in 1D
        Unbounded Knapsack: dp[i][j-w]   (same row) + left-to-right in 1D

    VARIATIONS:
        Subset Sum       → dp[i][j] = True/False, target = specific sum
        Count Subsets    → dp[i][j] = count, use + instead of max
        Min Subset Diff  → find achievable sums, minimize |total - 2*sum|
        Target Sum       → count subsets with sum = (total + target) / 2

================================================================================
"""

w=7
wt=[1,3,4,5]
val=[1,4,5,7]

'''return maximum profit

def knapsack_0_1_recursion(wt,val,w):
    
    
    #base condition(think of the smallest valid i/P)
    
    
    
    #choice diagram
    
    return
'''

def knapsack_0_1_recursion(wt,val,w,n):
    
    
    if n==0 or w==0:
        return 0
    
    # choice diagram
    if wt[n-1] <=w:
        return max(val[n-1] + knapsack_0_1_recursion(wt,val,w-wt[n-1],n-1),knapsack_0_1_recursion(wt,val,w,n-1))
    elif(wt[n-1]>w):
        return knapsack_0_1_recursion(wt,val,w,n-1)
n=len(val)
profit=knapsack_0_1_recursion(wt,val,w,n)  
print("profit of knapsack",profit)

print("\n memorization code for knsapsack")
print("\n ")

#2 step to convert recursion + memrization we add matrix or create matrix only for those varianle which is chnaging as per this w and n is getting change
memo = [[-1] * (w + 1) for _ in range(n + 1)]

def knapsack_0_1_memorization(wt,val,w,n):
    if n==0 or w==0:
            return 0
    if memo[n][w]!=-1:
        return memo[n][w]
    # choice diagram
    if wt[n-1] <=w:
        memo[n][w] = max(val[n-1] + knapsack_0_1_recursion(wt,val,w-wt[n-1],n-1),knapsack_0_1_recursion(wt,val,w,n-1))
    elif(wt[n-1]>w):
        memo[n][w]=knapsack_0_1_recursion(wt,val,w,n-1)
    
    return memo[n][w]


profit = knapsack_0_1_memorization(wt, val, w, n)

print("Profit of knapsack memorization:", profit)


#3 bottom up approach approach
print("\nBottom Up DP - Knapsack")
print("\n")

w = 7
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]

n = len(val)
dp = [[0] * (w + 1) for _ in range(n + 1)]


# Create DP matrix


def knapsack_0_1_bottom_up(wt,val,w,n):
    # Build table dp[][] in bottom-up manner
    for i in range(n + 1):
        for j in range(w + 1):

            # If there is no item or the knapsack's capacity is 0
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                pick = 0

                # Pick ith item if it does not exceed the capacity of knapsack
                if wt[i - 1] <= j:
                    pick = val[i - 1] + dp[i - 1][j - wt[i - 1]]

                # Don't pick the ith item
                notPick = dp[i - 1][j]

                dp[i][j] = max(pick, notPick)

    return dp[n][w]

print("Profit of knapsack of bottom up:", profit)


"""
================================================================================
================================================================================
    VARIATION 1: SUBSET SUM (Direct child of 0/1 Knapsack)
================================================================================
================================================================================

PROBLEM: Given an array of positive integers and a target sum S,
         determine if there's a subset whose elements sum to exactly S.

TRICK TO CONVERT FROM KNAPSACK:
    Knapsack has:  items with weight[] and value[], capacity W
    Subset Sum:    items with arr[] (arr IS both weight AND value), target S

    Mapping:
        wt[]  → arr[]
        val[] → arr[]  (same! because we "gain" the number itself)
        W     → target sum S
        "maximize value" → "can we reach exactly S?" (True/False)

================================================================================
THE MENTAL MODEL:
================================================================================

    For each element: INCLUDE it in subset or EXCLUDE it.
    If we can reach sum = 0 remaining → True (we found a valid subset!)
    If no elements left but sum > 0 → False

    dp[i][j] = "Can we make sum j using first i elements?"
    Answer: dp[n][S]

================================================================================
CHOICE DIAGRAM (same structure as knapsack):
================================================================================

                    element arr[i-1]
                   /           \\
                  /             \\
        arr[i-1] <= j?         arr[i-1] > j?
         /       \\                  |
        /         \\                 |
    INCLUDE      EXCLUDE           EXCLUDE
       |            |                |
    dp[i-1]     dp[i-1][j]       dp[i-1][j]
    [j-arr[i-1]]                
       |            |                |
       \\___   ____/                 |
           \\ /                      |
            OR                       |
    (either path → True)            |

================================================================================
TRANSITION:
================================================================================

    if arr[i-1] <= j:
        dp[i][j] = dp[i-1][j - arr[i-1]] OR dp[i-1][j]
                   (include)                 (exclude)
    else:
        dp[i][j] = dp[i-1][j]               (must exclude)

    BASE CASES:
        dp[i][0] = True  for all i  (sum 0 = empty subset = always possible)
        dp[0][j] = False for j > 0  (0 elements can't make positive sum)

================================================================================
DP TABLE TRACE:
================================================================================

    arr = [2, 3, 7, 8, 10], target = 11

         j→  0     1     2     3     4     5     6     7     8     9    10    11
    i=0      T     F     F     F     F     F     F     F     F     F     F     F
    i=1(2)   T     F     T     F     F     F     F     F     F     F     F     F
    i=2(3)   T     F     T     T     F     T     F     F     F     F     F     F
    i=3(7)   T     F     T     T     F     T     F     T     F     T     T     F
    i=4(8)   T     F     T     T     F     T     F     T     T     F     T     T
    i=5(10)  T     F     T     T     F     T     F     T     T     F     T     T

    dp[5][11] = True → subset {3, 8} sums to 11 ✓

================================================================================
CODE:
================================================================================

    def subset_sum(arr, target):
        n = len(arr)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True      # sum 0 always achievable

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][target]

    Time: O(n * target)    Space: O(n * target)

================================================================================
================================================================================
    VARIATION 2: EQUAL SUM PARTITION (LC 416)
================================================================================
================================================================================

PROBLEM: Can the array be partitioned into two subsets with equal sum?

ONE-LINE REDUCTION:
    If totalSum is ODD → impossible (can't split odd number equally).
    If totalSum is EVEN → Subset Sum with target = totalSum / 2.

WHY? If subset S1 sums to totalSum/2, then S2 = remaining also sums to totalSum/2.

    def can_partition(arr):
        total = sum(arr)
        if total % 2 != 0:
            return False
        return subset_sum(arr, total // 2)

================================================================================
================================================================================
    VARIATION 3: COUNT OF SUBSET SUM
================================================================================
================================================================================

PROBLEM: How many subsets sum to exactly target?

ONLY CHANGE FROM SUBSET SUM:
    - dp[i][j] stores COUNT (integer) instead of True/False
    - Use + instead of OR
    - Base case: dp[i][0] = 1 (one way: empty subset)

TRANSITION:
    if arr[i-1] <= j:
        dp[i][j] = dp[i-1][j - arr[i-1]] + dp[i-1][j]
                   (include count)           (exclude count)
    else:
        dp[i][j] = dp[i-1][j]

    def count_subset_sum(arr, target):
        n = len(arr)
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1        # one way to make sum 0

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j - arr[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][target]

================================================================================
================================================================================
    VARIATION 4: MINIMUM SUBSET SUM DIFFERENCE
================================================================================
================================================================================

PROBLEM: Partition array into 2 subsets S1, S2. Minimize |S1 - S2|.

KEY INSIGHT:
    S1 + S2 = totalSum
    We want to minimize |S1 - S2| = |totalSum - 2*S1|
    So minimize |totalSum - 2*S1| → S1 should be as close to totalSum/2 as possible.

APPROACH:
    1. Run subset sum for all possible sums 0..totalSum/2
    2. Find the largest achievable sum S1 <= totalSum/2
    3. Answer = totalSum - 2 * S1

    def min_subset_diff(arr):
        total = sum(arr)
        n = len(arr)
        dp = [[False] * (total + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, total + 1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        # Find largest achievable sum <= total // 2
        for s in range(total // 2, -1, -1):
            if dp[n][s]:
                return total - 2 * s

================================================================================
================================================================================
    VARIATION 5: TARGET SUM (LC 494)
================================================================================
================================================================================

PROBLEM: Assign + or - to each element to reach target. Count the ways.

MATHEMATICAL REDUCTION:
    Let P = set of elements with +, N = set with -
    P - N = target
    P + N = totalSum
    Adding: 2P = target + totalSum
    So: P = (target + totalSum) / 2

    → Count subsets with sum = (target + totalSum) / 2

EDGE CASES:
    - If (target + totalSum) is odd → 0 ways
    - If |target| > totalSum → 0 ways

    def target_sum(arr, target):
        total = sum(arr)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
        new_target = (total + target) // 2
        return count_subset_sum(arr, new_target)

================================================================================
================================================================================
    VARIATION 6: NUMBER OF SUBSETS WITH GIVEN DIFFERENCE
================================================================================
================================================================================

PROBLEM: Count subsets where S1 - S2 = diff (S1 >= S2).

SAME MATH AS TARGET SUM:
    S1 - S2 = diff
    S1 + S2 = totalSum
    → S1 = (totalSum + diff) / 2

    → Count subsets with sum = (totalSum + diff) / 2

    def count_subsets_with_diff(arr, diff):
        total = sum(arr)
        if (total + diff) % 2 != 0:
            return 0
        target = (total + diff) // 2
        return count_subset_sum(arr, target)

================================================================================
MASTER CONVERSION TABLE — How each variation changes the template:
================================================================================

    ┌────────────────────┬───────────┬──────────────┬──────────────────────┐
    │ Problem            │ dp type   │ Operator     │ Target               │
    ├────────────────────┼───────────┼──────────────┼──────────────────────┤
    │ 0/1 Knapsack       │ int (max) │ max(pick,skip)│ capacity W          │
    │ Subset Sum         │ bool      │ OR           │ given target S       │
    │ Equal Partition    │ bool      │ OR           │ totalSum / 2         │
    │ Count Subsets      │ int (cnt) │ +            │ given target S       │
    │ Min Subset Diff    │ bool      │ OR           │ find best S1         │
    │ Target Sum         │ int (cnt) │ +            │ (total+target) / 2   │
    │ #Subsets w/ Diff   │ int (cnt) │ +            │ (total+diff) / 2     │
    └────────────────────┴───────────┴──────────────┴──────────────────────┘

================================================================================
LEETCODE PROBLEMS FOR THIS PHASE:
================================================================================

    LC #  │ Problem                          │ Variation
    ──────┼──────────────────────────────────┼──────────────────────
    416   │ Partition Equal Subset Sum        │ Equal Sum Partition
    494   │ Target Sum                        │ Target Sum
    1049  │ Last Stone Weight II              │ Min Subset Sum Diff
    474   │ Ones and Zeroes                   │ 2D Knapsack (0/1)
    2915  │ Length of Longest Subsequence Sum │ Subset Sum variant
    518   │ Coin Change II                    │ Unbounded Knapsack
    322   │ Coin Change                       │ Unbounded Knapsack
    377   │ Combination Sum IV                │ Unbounded + permutation
    279   │ Perfect Squares                   │ Unbounded Knapsack

================================================================================
"""
'''
knapsack identification .if item is given and you need to choice the item

1.subset sum
2.equal sum partition
3.count of subset sum
4.minimum subset sum off
5.target sum
6.# of subset i given d/f
'''

"""
================================================================================
================================================================================
    KNAPSACK IDENTIFICATION — The Secret to Solving 6 Problems in Interviews
================================================================================
================================================================================

HOW TO SPOT A KNAPSACK PROBLEM IN 5 SECONDS:
================================================================================

    Ask yourself TWO questions:

    Question 1: "Am I making a PICK or SKIP choice for each item?"
    Question 2: "Is there a CONSTRAINT (capacity, sum, limit)?"

    If BOTH are YES → it's a Knapsack problem.

    ┌──────────────────────────────────────────────────────────────────┐
    │                                                                  │
    │   "Pick/Skip choice" + "Constraint" = KNAPSACK FAMILY            │
    │                                                                  │
    └──────────────────────────────────────────────────────────────────┘

================================================================================
THE 6 CHILDREN — How each one is just Knapsack in disguise:
================================================================================

    ALL 6 problems share this skeleton:

        for i in range(1, n+1):        # each item
            for j in range(1, W+1):    # each capacity/sum
                if arr[i-1] <= j:
                    dp[i][j] = __OPERATOR__(include, exclude)
                else:
                    dp[i][j] = exclude

    What changes between problems:

    ┌─────┬──────────────────┬──────────┬──────────┬───────────────────┐
    │  #  │ Problem          │ dp type  │ Operator │ What is "W"?      │
    ├─────┼──────────────────┼──────────┼──────────┼───────────────────┤
    │  0  │ 0/1 Knapsack     │ int      │ max()    │ bag capacity      │
    │  1  │ Subset Sum       │ bool     │ OR       │ target sum        │
    │  2  │ Equal Partition  │ bool     │ OR       │ totalSum / 2      │
    │  3  │ Count Subsets    │ int      │ +        │ target sum        │
    │  4  │ Min Subset Diff  │ bool     │ OR       │ totalSum (all)    │
    │  5  │ Target Sum       │ int      │ +        │ (total+target)/2  │
    │  6  │ #Subsets w/ Diff │ int      │ +        │ (total+diff)/2    │
    └─────┴──────────────────┴──────────┴──────────┴───────────────────┘

    MEMORY TRICK — 3 types of operators:
        "Can we?"    → bool, use OR    (Subset Sum, Equal Partition, Min Diff)
        "How many?"  → int,  use +     (Count Subsets, Target Sum, #Subsets Diff)
        "Best value?"→ int,  use max() (0/1 Knapsack itself)

================================================================================
THE FAMILY TREE — How each problem REDUCES to another:
================================================================================

    ┌─────────────────────────────────────────────────────────────────────┐
    │                                                                     │
    │                        0/1 KNAPSACK                                 │
    │                        (max, capacity)                              │
    │                             │                                       │
    │              ┌──────────────┴──────────────┐                        │
    │              ▼                              ▼                        │
    │         SUBSET SUM                   COUNT OF SUBSET SUM            │
    │         (OR, target)                 (+, target)                    │
    │              │                              │                        │
    │     ┌────────┴────────┐              ┌──────┴──────┐                │
    │     ▼                 ▼              ▼             ▼                │
    │  EQUAL SUM       MIN SUBSET      TARGET SUM   #SUBSETS             │
    │  PARTITION       SUM DIFF        (LC 494)     GIVEN DIFF           │
    │  (LC 416)        (LC 1049)                                          │
    │                                                                     │
    │  target =        scan last row   target =     target =             │
    │  totalSum/2      of subset sum   (T+tgt)/2    (T+diff)/2           │
    │                  for best S1                                        │
    └─────────────────────────────────────────────────────────────────────┘

    Reading the tree:
    → Equal Partition calls Subset Sum with target = totalSum/2
    → Target Sum calls Count of Subset Sum with target = (total+target)/2
    → Min Subset Diff calls Subset Sum for ALL sums, then picks best

================================================================================
INITIALIZATION RULES — THE MOST IMPORTANT PART (where 90% of bugs come from):
================================================================================

    RULE 1: FIRST COLUMN (j = 0, meaning target sum = 0)

        "Can I make sum 0?"  → YES, always. Take nothing (empty subset).
        dp[i][0] = True   (for bool problems)
        dp[i][0] = 1      (for count problems — 1 way: take nothing)
        dp[i][0] = 0      (for knapsack — 0 value if 0 capacity)

    RULE 2: FIRST ROW (i = 0, meaning 0 items available)

        "Can I make sum j > 0 with 0 items?"  → NO.
        dp[0][j] = False  (for bool problems)
        dp[0][j] = 0      (for count and knapsack problems)

    VISUAL:
                    j=0    j=1    j=2    j=3   ...   j=W
        i=0    [  T/1/0    F/0    F/0    F/0   ...   F/0  ]  ← 0 items
        i=1    [  T/1/0    ...    ...    ...   ...   ...   ]
        i=2    [  T/1/0    ...    ...    ...   ...   ...   ]
        ...    [  T/1/0    ...    FILL THESE   ...   ...   ]
        i=n    [  T/1/0    ...    ...    ...   ...  ANSWER ]
                  ↑
                  always True/1/0

================================================================================
================================================================================
    PROBLEM 1: SUBSET SUM — Full Breakdown
================================================================================
================================================================================

PROBLEM STATEMENT:
    Given array arr[] and a target sum S, does any subset of arr sum to S?
    Return True/False.

    Example: arr = [2, 3, 7, 8, 10], sum = 11
    Answer: True (subset {3, 8} = 11)

================================================================================
SIMILARITY TO KNAPSACK:
================================================================================

    Knapsack                         Subset Sum
    ─────────────────────────────    ─────────────────────────────
    wt[] (weight array)          →   arr[] (the given array)
    val[] (value array)          →   arr[] (SAME array! value = weight)
    W (capacity)                 →   S (target sum)
    "maximize value"             →   "can we hit exact sum?" (True/False)
    max(pick, skip)              →   pick OR skip

    The mapping is:
    ┌──────────────────────────────────────────────────────────────────┐
    │  Knapsack:  wt[], val[], W  →  max(val[i] + dp[...], dp[...])  │
    │  Subset Sum: arr[], S       →  dp[...] OR dp[...]               │
    │                                                                  │
    │  wt[] → arr[]                                                    │
    │  val[] → arr[] (same array, not needed separately)               │
    │  W → target sum S                                                │
    │  max() → OR                                                      │
    │  int dp → bool dp                                                │
    └──────────────────────────────────────────────────────────────────┘

================================================================================
CODE VARIATION — Side by side with Knapsack:
================================================================================

    KNAPSACK TRANSITION:                    SUBSET SUM TRANSITION:

    if wt[i-1] <= j:                        if arr[i-1] <= j:
        dp[i][j] = max(                         dp[i][j] = (
            val[i-1] + dp[i-1][j-wt[i-1]],         dp[i-1][j - arr[i-1]]
            dp[i-1][j]                               OR dp[i-1][j]
        )                                       )
    else:                                   else:
        dp[i][j] = dp[i-1][j]                  dp[i][j] = dp[i-1][j]

    3 CHANGES:
        1. max()  →  OR
        2. val[i-1] + ... is gone (we don't add value, just check reachability)
        3. dp stores bool (True/False) instead of int

================================================================================
INITIALIZATION:
================================================================================

    dp = [[False] * (sum + 1) for _ in range(n + 1)]

    First column (sum = 0):
        dp[i][0] = True    for all i
        (empty subset sums to 0)

    First row (0 items):
        dp[0][j] = False   for j > 0
        (can't make positive sum with no items)

    VISUAL:
              j=0   j=1   j=2   j=3  ...  j=S
    i=0    [   T     F     F     F   ...    F  ]
    i=1    [   T     ?     ?     ?   ...    ?  ]
    i=2    [   T     ?     ?     ?   ...    ?  ]
    ...    [   T     ?     ?     ?   ...    ?  ]
    i=n    [   T     ?     ?     ?   ...  ANS  ]

================================================================================
DP TABLE TRACE — arr = [2, 3, 7, 8, 10], sum = 11:
================================================================================

    Row-by-row filling (T = True, F = False):

         j→  0   1   2   3   4   5   6   7   8   9  10  11
    i=0      T   F   F   F   F   F   F   F   F   F   F   F

    ── i=1, arr[0]=2 ──────────────────────────────────────
    j=1: 2 > 1 → exclude → dp[0][1] = F
    j=2: 2 <= 2 → include dp[0][2-2]=dp[0][0]=T OR exclude dp[0][2]=F → T
    j=3..11: only j=2 gets T (only element is 2)

    i=1      T   F   T   F   F   F   F   F   F   F   F   F

    ── i=2, arr[1]=3 ──────────────────────────────────────
    j=1: 3 > 1 → F
    j=2: 3 > 2 → dp[1][2] = T (from above)
    j=3: 3 <= 3 → dp[1][0]=T OR dp[1][3]=F → T
    j=5: 3 <= 5 → dp[1][2]=T OR dp[1][5]=F → T (subset {2,3})
    Others: F

    i=2      T   F   T   T   F   T   F   F   F   F   F   F

    ── i=3, arr[2]=7 ──────────────────────────────────────
    New True cells: j=7 (just 7), j=9 (2+7), j=10 (3+7)

    i=3      T   F   T   T   F   T   F   T   F   T   T   F

    ── i=4, arr[3]=8 ──────────────────────────────────────
    New True cells: j=8 (just 8), j=10 (2+8), j=11 (3+8) ← FOUND!

    i=4      T   F   T   T   F   T   F   T   T   F   T   T

    dp[4][11] = True already! (subset {3, 8} = 11)

    ── i=5, arr[4]=10 ─────────────────────────────────────
    Adds more True cells but answer already found above.

    i=5      T   F   T   T   F   T   F   T   T   F   T   T

    ANSWER: dp[5][11] = True ✓

    Subset that works: {3, 8} → 3 + 8 = 11 ✓

================================================================================
HOW TO TRACE WHICH ELEMENTS FORM THE SUBSET:
================================================================================

    Start at dp[n][S]. If True:
        if dp[i-1][j] is True → arr[i-1] was NOT included (came from above)
            → move to dp[i-1][j]
        else → arr[i-1] WAS included
            → move to dp[i-1][j - arr[i-1]]

    Example trace for dp[5][11]:
        dp[4][11] = T? YES → arr[4]=10 NOT included. Move to dp[4][11].
        dp[3][11] = F, dp[4][11] came from dp[3][11]? → check dp[3][11]=F
        Actually: dp[4][11] is T because dp[3][11-8]=dp[3][3]=T → arr[3]=8 INCLUDED
        Now at dp[3][3]. dp[2][3]=T? YES → arr[2]=7 NOT included.
        dp[1][3]. dp[0][3]=F → arr[1]=3 INCLUDED.
        Remaining sum: 3-3=0. Done.

        Subset: {3, 8} ✓

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(n * sum)  — fill n+1 rows, sum+1 columns
    Space: O(n * sum)  — the 2D dp table

    Space optimized (1D):
        dp = [False] * (sum + 1)
        dp[0] = True
        for i in range(n):
            for j in range(sum, arr[i] - 1, -1):   # RIGHT TO LEFT
                dp[j] = dp[j] or dp[j - arr[i]]

        Time: O(n * sum)   Space: O(sum)

================================================================================
FAANG INTERVIEW TIPS FOR SUBSET SUM:
================================================================================

    TIP 1: "How is this different from knapsack?"
            → "Same structure, but we check REACHABILITY (bool) not MAX VALUE (int).
               OR replaces max(), val[] is gone."

    TIP 2: If arr contains negative numbers → problem changes significantly.
            Standard subset sum assumes positive integers.

    TIP 3: If asked "which elements form the subset?" → trace back through table.

    TIP 4: Space optimization: 1D array, traverse RIGHT TO LEFT.
            Same reason as knapsack (prevent using element twice).

    TIP 5: Edge cases:
            → sum = 0 → always True (empty subset)
            → arr is empty, sum > 0 → False
            → single element equal to sum → True

================================================================================
"""

arr=[2,3,7,8,10]
sum=11 #yes or no so we have a choice which can make the sum 11 or not T/F  so its knapsack


#initialization

'''for i to size of array:
    for j t size of array
        if(i==0):
            t[i][j]==F
        if(j==0):
            t[i][j]=T
'''
#code variation  create matching with knapsack arr[] will match weith weight array and sum will be weight

#initilaization is done
#wt[]--->arr[]
#sum--->w
'''
Knapsack                                                             Subset sum


if(wt[i-1]<=j)                                                       if(arr[i-1]<=j)
    t[i][j] = max(val(i-1)+t[i-1][j-wt[i-1]],t[i-1][j])                  t[i][j]  =t[i][j-arr[i-1]] OR t[i-1][j]      
else:                                                                else:
    t[i][j]=t[i-1][j]                                                    t[i][j]=t[i-1][j]
    
for T/F we will use OR

'''

"""
================================================================================
SUBSET SUM — YOUR CODE (Verified working below)
================================================================================

    Complexity: Time O(n * sum) | Space O(n * sum)

    Your initialization:
        dp[i][0] = True   ← column 0 = sum 0 = always possible
        dp[0][j] = False  ← row 0 (0 items), j > 0 = impossible
        (False is default from the list creation)

    Your transition matches the knapsack-to-subset-sum mapping:
        Knapsack:   max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
        Subset Sum: dp[i-1][j-arr[i-1]] OR dp[i-1][j]

    NOTE: your code has dp[i][j-arr[i-1]] (same row i, not i-1).
    For 0/1 subset sum it should be dp[i-1][j-arr[i-1]] (previous row)
    to avoid using the same element twice. With same row, an element
    could be included multiple times (unbounded behavior).
    The current code still passes for this test case since {3,8}=11
    doesn't need any repeated element.
================================================================================
"""
print("covering all 0-1 knsapsack aptterns \n")

arr=[2,3,7,8,10]
sum=11
def subset_sum(arr,sum):
    
    n = len(arr)

    # Create a 2D list for storing 
    # results of subproblems
    dp = [[False] * (sum + 1) for _ in range(n + 1)]

    # If sum is 0, then answer is 
    # true (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp table in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            # if j < arr[i - 1]:
                
            #     # Exclude the current element
            #     dp[i][j] = dp[i - 1][j]
            # else:
                
            #     # Include or exclude
            #     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            if arr[i-1]<=j: 
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
                

    return dp[n][sum]
            
ans = subset_sum(arr,sum)
print("subset sum ans",ans)         
    


"""
================================================================================
================================================================================
    PROBLEM 2: EQUAL SUM PARTITION (LC 416) — Full Breakdown
================================================================================
================================================================================

PROBLEM STATEMENT:
    Given array arr[], can it be split into 2 subsets with EQUAL sum?
    Return True/False.

    Example 1: arr = [1, 5, 11, 5] → True (subsets {1,5,5} and {11})
    Example 2: arr = [1, 2, 3, 5] → False (total=11, odd, impossible)

================================================================================
THE "AHA" MOMENT — It's just Subset Sum!
================================================================================

    If total sum of array is S:
        Subset 1 = S/2,  Subset 2 = S/2

    So the question becomes:
        "Does a subset exist that sums to S/2?"

    That's EXACTLY Subset Sum with target = S/2!

    TWO EDGE CASES (check BEFORE running DP):
        1. If S is ODD → return False immediately
           (can't split an odd number into two equal halves)
        2. If S is 0 → return True (both subsets are empty)

================================================================================
REDUCTION STEPS (say this in interview):
================================================================================

    Step 1: total = sum(arr)
    Step 2: if total % 2 != 0 → return False
    Step 3: target = total // 2
    Step 4: return subset_sum(arr, target)

    That's it. The ENTIRE problem is 4 lines on top of subset sum.

================================================================================
DP TABLE TRACE — arr = [1, 5, 11, 5], total = 22, target = 11:
================================================================================

         j→  0   1   2   3   4   5   6   7   8   9  10  11
    i=0      T   F   F   F   F   F   F   F   F   F   F   F
    i=1(1)   T   T   F   F   F   F   F   F   F   F   F   F
    i=2(5)   T   T   F   F   F   T   T   F   F   F   F   F
    i=3(11)  T   T   F   F   F   T   T   F   F   F   F   T
    i=4(5)   T   T   F   F   F   T   T   F   F   F   T   T

    dp[4][11] = True ✓
    Subset 1: {11} = 11,  Subset 2: {1, 5, 5} = 11

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(n * sum/2)
    Space: O(n * sum/2) → can optimize to O(sum/2) with 1D array

================================================================================
CODE TEMPLATE:
================================================================================

    def can_partition(arr):
        total = sum(arr)
        if total % 2 != 0:
            return False
        return subset_sum(arr, total // 2)

================================================================================
INTERVIEW TIP:
================================================================================

    When you see "equal partition" → immediately say:
    "This reduces to subset sum with target = totalSum/2."
    Then write subset_sum and call it. Done in 2 minutes.

================================================================================
================================================================================
    PROBLEM 3: COUNT OF SUBSET SUM — Full Breakdown
================================================================================
================================================================================

PROBLEM STATEMENT:
    Given array arr[] and target sum S, count HOW MANY subsets sum to S.
    Return the count.

    Example: arr = [1, 1, 2, 3], target = 3
    Answer: 3 subsets → {1,2}, {1,2}, {3}

================================================================================
THE ONLY CHANGE FROM SUBSET SUM:
================================================================================

    SUBSET SUM:                          COUNT OF SUBSET SUM:
    dp[i][j] = True/False                dp[i][j] = integer count
    OR (include, exclude)                + (include, exclude)
    dp[i][0] = True                      dp[i][0] = 1

    That's it. Replace OR with +. Replace True with 1. Replace False with 0.

================================================================================
TRANSITION:
================================================================================

    if arr[i-1] <= j:
        dp[i][j] = dp[i-1][j - arr[i-1]] + dp[i-1][j]
                   (# ways if include)      (# ways if exclude)
    else:
        dp[i][j] = dp[i-1][j]             (must exclude)

================================================================================
DP TABLE TRACE — arr = [1, 1, 2, 3], target = 3:
================================================================================

         j→  0   1   2   3
    i=0      1   0   0   0
    i=1(1)   1   1   0   0
    i=2(1)   1   2   1   0
    i=3(2)   1   2   3   2
    i=4(3)   1   2   3   3

    dp[4][3] = 3

    The 3 subsets: {1a, 2}, {1b, 2}, {3}
    (two different 1s give two different subsets)

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(n * target)
    Space: O(n * target) → can optimize to O(target) with 1D array

================================================================================
================================================================================
    PROBLEM 4: MINIMUM SUBSET SUM DIFFERENCE — Full Breakdown
================================================================================
================================================================================

PROBLEM STATEMENT:
    Partition array into 2 subsets S1 and S2. Minimize |S1 - S2|.
    Return the minimum difference.

    Example: arr = [1, 6, 11, 5], total = 23
    Best: S1 = {1, 5, 6} = 12, S2 = {11} = 11, diff = 1
    Answer: 1

================================================================================
THE KEY MATHEMATICAL INSIGHT:
================================================================================

    S1 + S2 = total
    S2 = total - S1
    |S1 - S2| = |S1 - (total - S1)| = |2*S1 - total|

    To minimize |2*S1 - total|:
        S1 should be as CLOSE to total/2 as possible.

    APPROACH:
        1. Run subset sum DP for all sums 0 to total
        2. Look at last row dp[n][j] for j = 0 to total/2
        3. Find the LARGEST j where dp[n][j] is True
        4. Answer = total - 2 * j

    WHY only check up to total/2?
        If S1 <= total/2, then S2 >= total/2, and diff = S2 - S1.
        We want S1 as close to total/2 as possible for minimum diff.

================================================================================
DP TABLE TRACE — arr = [1, 6, 11, 5], total = 23:
================================================================================

    Run subset sum for all sums 0..23.
    Last row dp[4][j]:

    j:    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
    dp:   T  T  F  F  F  T  T  T  F  F  F  T  T  F  F  F  T  T  T  F  F  F  T  T

    Achievable sums: {0, 1, 5, 6, 7, 11, 12, 16, 17, 18, 22, 23}

    total/2 = 11.5, so check from j=11 downward:
        j=11: True → S1 = 11, diff = |23 - 2*11| = 1 ✓

    Answer: 1

    Check: S1 = {11} = 11, S2 = {1,6,5} = 12, diff = 1 ✓

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(n * total)    Space: O(n * total)

================================================================================
================================================================================
    PROBLEM 5: TARGET SUM (LC 494) — Full Breakdown
================================================================================
================================================================================

PROBLEM STATEMENT:
    Given array arr[], assign + or - to each element to make total = target.
    Count the number of ways.

    Example: arr = [1, 1, 2, 3], target = 1
    Ways: +1-1+2-3 = -1 (no), +1+1-2+3 = 3 (no), +1+1+2-3 = 1 (yes!), etc.

================================================================================
THE MATHEMATICAL TRICK (derive in interview):
================================================================================

    Let P = sum of elements with +
    Let N = sum of elements with -

    P - N = target     ... (1)
    P + N = totalSum   ... (2)

    Add equations (1) + (2):
        2P = target + totalSum
        P = (target + totalSum) / 2

    So: "count subsets with sum P" = Count of Subset Sum problem!

    EDGE CASES:
        if (target + totalSum) is ODD → 0 ways (P can't be fractional)
        if |target| > totalSum → 0 ways (impossible)

================================================================================
EXAMPLE TRACE:
================================================================================

    arr = [1, 1, 2, 3], target = 1
    total = 7
    P = (1 + 7) / 2 = 4

    Count subsets summing to 4:
    {1, 3} → 1a + 3 = 4 ✓
    {1, 3} → 1b + 3 = 4 ✓
    {2, 1, 1} → hmm, 1+1+2 = 4 ✓

    Answer: 3

    Verify one: assign +1a, -1b, +2, +3 → 1-1+2+3 = no, that's 5
    Actually: P = {1,3} means +1+3 = 4, N = {1,2} means -(1+2) = -3
    Result: 4 - 3 = 1 ✓

================================================================================
COMPLEXITY:
================================================================================

    Time:  O(n * P) where P = (total + target) / 2
    Space: O(n * P) → can optimize to O(P)

================================================================================
================================================================================
    PROBLEM 6: #SUBSETS WITH GIVEN DIFFERENCE — Full Breakdown
================================================================================
================================================================================

PROBLEM STATEMENT:
    Count subsets where S1 - S2 = diff (where S1 >= S2).

    SAME MATH AS TARGET SUM:
        S1 - S2 = diff
        S1 + S2 = totalSum
        → S1 = (totalSum + diff) / 2

    → Count subsets with sum = (totalSum + diff) / 2

    This is literally Target Sum with "diff" replacing "target."

================================================================================
================================================================================
    COMPLETE KNAPSACK IDENTIFICATION SUMMARY
================================================================================
================================================================================

    When you see a DP problem, ask:

    ┌─────────────────────────────────────────────────────────────────────┐
    │  1. "Is there a PICK/SKIP choice?"           → YES → Knapsack     │
    │  2. "What is the CONSTRAINT?"                → capacity/sum/limit │
    │  3. "What am I optimizing?"                                        │
    │      → "Max/Min VALUE"   → use max()/min()   → 0/1 Knapsack      │
    │      → "Can I reach?"    → use OR (bool)     → Subset Sum family  │
    │      → "How many ways?"  → use + (count)     → Count Subsets      │
    │  4. "Can items repeat?"                                            │
    │      → NO  → 0/1 Knapsack  → dp[i-1][...] → right-to-left 1D    │
    │      → YES → Unbounded     → dp[i][...]   → left-to-right 1D    │
    └─────────────────────────────────────────────────────────────────────┘

    COMPLEXITY FOR ALL VARIATIONS:
    ┌──────────────────────┬──────────────────┬──────────────────────────┐
    │ Problem              │ Time             │ Space                    │
    ├──────────────────────┼──────────────────┼──────────────────────────┤
    │ 0/1 Knapsack         │ O(n * W)         │ O(n * W) → O(W)         │
    │ Subset Sum           │ O(n * sum)       │ O(n * sum) → O(sum)     │
    │ Equal Partition      │ O(n * sum/2)     │ O(n * sum/2) → O(sum/2) │
    │ Count Subsets        │ O(n * target)    │ O(n * target) → O(target)│
    │ Min Subset Diff      │ O(n * total)     │ O(n * total) → O(total) │
    │ Target Sum           │ O(n * P)         │ O(n * P) → O(P)         │
    │ #Subsets w/ Diff     │ O(n * P)         │ O(n * P) → O(P)         │
    └──────────────────────┴──────────────────┴──────────────────────────┘
    (P = (total + target) / 2 for Target Sum / Subsets w/ Diff)

    All can be space-optimized from O(n * X) to O(X) using 1D right-to-left.

================================================================================
"""


"""
================================================================================
    EQUAL SUM PARTITION — Tricks, Complexity & Easy to Remember
================================================================================

PROBLEM: Can array be split into 2 subsets with EQUAL sum?
    arr = [1, 5, 5, 11] → total = 22 → target = 11 → {11} and {1,5,5} → True

================================================================================
ONE-LINE TRICK TO NEVER FORGET:
================================================================================

    "Equal partition = Subset Sum(total/2). If total is odd, return False."

    That's it. The ENTIRE problem is just:
        1. total = sum(arr)
        2. if total is odd → False
        3. else → can we make subset summing to total/2?

================================================================================
CHOICE DIAGRAM (same as Subset Sum):
================================================================================

                    arr[n-1]
                   /         \\
        arr[n-1] <= target?   arr[n-1] > target?
         /         \\               |
      INCLUDE    EXCLUDE          EXCLUDE
         |          |               |
    helper(n-1,  helper(n-1,    helper(n-1,
    target -     target)        target)
    arr[n-1])

    Answer = INCLUDE or EXCLUDE (either path works → True)

================================================================================
COMPLEXITY TABLE:
================================================================================

    ┌──────────────────┬──────────────────────┬──────────────────────────┐
    │ Approach         │ Time                 │ Space                    │
    ├──────────────────┼──────────────────────┼──────────────────────────┤
    │ Recursion        │ O(2^n)               │ O(n) stack              │
    │ Memoization      │ O(n * total/2)       │ O(n * total/2) + stack  │
    │ Bottom-Up        │ O(n * total/2)       │ O(n * total/2)          │
    │ Bottom-Up (1D)   │ O(n * total/2)       │ O(total/2)             │
    └──────────────────┴──────────────────────┴──────────────────────────┘

    WHY total/2 and not total?
        Because target = total//2. The DP table columns go from 0 to target.

================================================================================
5 TRICKS TO REMEMBER FOREVER:
================================================================================

    TRICK 1: "ODD = IMPOSSIBLE"
        If total sum is odd → instantly return False. No computation needed.
        (You can't split 11 into 5.5 + 5.5)

    TRICK 2: "EQUAL PARTITION = SUBSET SUM(total/2)"
        Don't think of it as a new problem.
        It's LITERALLY: "can I find a subset that sums to half?"
        If yes → the other half is automatically the remaining elements.

    TRICK 3: "Same template, same code, different target"
        Subset Sum code with target = total//2. That's the ONLY change.

    TRICK 4: "Recursion → Memo → Bottom-Up conversion"
        Recursion: helper(arr, n, target)
        Memo:      add memo[n][target], check before computing
        Bottom-Up: dp[i][j] → i = items, j = 0 to target
                   dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]

    TRICK 5: "Space optimization = 1D right-to-left"
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(n):
            for j in range(target, arr[i]-1, -1):
                dp[j] = dp[j] or dp[j - arr[i]]

================================================================================
INTERVIEW QUICK-FIRE ANSWERS:
================================================================================

    Q: "How did you identify this?"
    A: "Array partition into equal halves = subset sum with target = total/2."

    Q: "What if total is odd?"
    A: "Return False immediately — can't split odd number equally."

    Q: "Time complexity?"
    A: "O(n * total/2) for DP. O(2^n) for brute force recursion."

    Q: "Can you optimize space?"
    A: "Yes, 1D array of size target+1, traverse right to left."

    Q: "What's different from regular subset sum?"
    A: "Nothing in the algorithm. Only the target is derived (total//2)
        and there's an odd-sum early exit."

================================================================================
DP TABLE FOR THIS EXAMPLE — arr = [1, 5, 5, 11], target = 11:
================================================================================

         j→  0   1   2   3   4   5   6   7   8   9  10  11
    i=0      T   F   F   F   F   F   F   F   F   F   F   F
    i=1(1)   T   T   F   F   F   F   F   F   F   F   F   F
    i=2(5)   T   T   F   F   F   T   T   F   F   F   F   F
    i=3(5)   T   T   F   F   F   T   T   F   F   F   T   T
    i=4(11)  T   T   F   F   F   T   T   F   F   F   T   T

    dp[4][11] = True ✓

    HOW? Looking at i=3, j=11:
        arr[2]=5 <= 11 → dp[2][11-5]=dp[2][6]=T → True!
        Subset: {5, 5, 1} = 11 (the other subset: {11} = 11)

================================================================================
COMMON MISTAKES:
================================================================================

    ✗ Forgetting the odd check → wasting time on impossible cases
    ✗ Using dp[i][j-arr[i-1]] (same row) → unbounded behavior
    ✗ Memo table too small → use (n+1) x (target+1), not n x target
    ✗ Confusing target with total → target = total // 2, NOT total

================================================================================
"""

'''
Equal sum partition

'''
arr=[1,5,5,11]

#recursion
#memorization plus top down
# bottom up

def equal_sum_partition_recursion(arr,n):
    total=0
    for i in range(len(arr)):
        total= total+arr[i]
    
    if total%2!=0:
        print("the answer of equal_sum_partion", False)
        return
    
    target = total//2
    
    # this helper is subset_sum recursion with target
    def helper(arr, n, target):
        if target == 0:
            return True
        if n == 0:
            return False
        if arr[n-1] <= target:
            return helper(arr, n-1, target - arr[n-1]) or helper(arr, n-1, target)
        else:
            return helper(arr, n-1, target)
    
    ans = helper(arr, n, target)
    print("the answer of equal_sum_partion", ans)

equal_sum_partition_recursion(arr,len(arr))

#memorization

def equal_sum_partition_memorization(arr,n):
    total=0
    for i in range(len(arr)):
        total= total+arr[i]
    
    if total%2!=0:
        print("the answer of equal_sum_partion memorization", False)
        return
    
    target = total//2
    
    def helper(arr, n, target, memo):
        if target == 0:
            return True
        if n == 0:
            return False
        if memo[n][target] != -1:
            return memo[n][target]
        if arr[n-1] <= target:
            memo[n][target] = helper(arr, n-1, target - arr[n-1], memo) or helper(arr, n-1, target, memo)
        else:
            memo[n][target] = helper(arr, n-1, target, memo)
        return memo[n][target]
    
    memo = [[-1] * (target + 1) for _ in range(n + 1)]
    ans = helper(arr, n, target, memo)
    print("the answer of equal_sum_partion memorization", ans)

equal_sum_partition_memorization(arr,len(arr))

#bottom up

def equal_sum_partition_bottom_up(arr,n):
    total=0
    for i in range(len(arr)):
        total= total+arr[i]
    
    if total%2!=0:
        print("the answer of equal_sum_partion bottom up", False)
        return
    
    target = total//2
    n = len(arr)
    
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # initialization: sum 0 is always achievable (empty subset)
    for i in range(n + 1):
        dp[i][0] = True
    
    # fill dp table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    print("the answer of equal_sum_partion bottom up", dp[n][target])


equal_sum_partition_bottom_up(arr,len(arr))




#Now count for subset sum to a given sum

arr=[2,3,5,6,8,10]
sum=10

def count_of_subset_sum(arr,sum):
    
    n = len(arr)

    # Create a 2D list for storing 
    # results of subproblems
    dp = [[False] * (sum + 1) for _ in range(n + 1)]

    # If sum is 0, then answer is 
    # true (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp table in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            # if j < arr[i - 1]:
                
            #     # Exclude the current element
            #     dp[i][j] = dp[i - 1][j]
            # else:
                
            #     # Include or exclude
            #     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            if arr[i-1]<=j: 
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
                

    return dp[n][sum]
            
ans = count_of_subset_sum(arr,sum)
print("count of subset sum ans",ans)


"""
================================================================================
================================================================================
    MINIMUM SUBSET SUM DIFFERENCE — Complete FAANG Guide
================================================================================
================================================================================

PROBLEM STATEMENT:
    Partition array into 2 subsets S1 and S2.
    Minimize |sum(S1) - sum(S2)|.
    Return the minimum possible difference.

    Example 1: arr = [1, 6, 11, 5]
        Best: S1 = {1,5,6} = 12, S2 = {11} = 11, diff = 1
        Answer: 1

    Example 2: arr = [1, 5, 11, 5]
        Best: S1 = {1,5,5} = 11, S2 = {11} = 11, diff = 0
        Answer: 0

================================================================================
ONE-LINE TRICK TO NEVER FORGET:
================================================================================

    "Run Subset Sum for ALL possible sums, then pick the S1 closest to total/2.
     Answer = total - 2 * S1."

================================================================================
THE MATHEMATICAL KEY (understand this, solve the problem):
================================================================================

    S1 + S2 = total           (always true, all elements used)
    S2 = total - S1           (substitute)
    diff = S2 - S1 = total - 2*S1

    To MINIMIZE diff:
        → S1 should be as CLOSE to total/2 as possible
        → Find the LARGEST achievable sum <= total/2

    VISUAL:
        total = 23
        ├──────────S1──────────┤──────S2──────┤
        0          11        11.5          23
                    ↑
              S1 as close to here as possible

================================================================================
WHY THIS IS JUST SUBSET SUM + ONE EXTRA STEP:
================================================================================

    Step 1: Run subset sum DP for all sums 0 to total
            (dp[i][j] = can first i elements make sum j?)

    Step 2: Look at the LAST ROW dp[n][...]
            Find all j where dp[n][j] = True
            These are ALL achievable subset sums.

    Step 3: Among achievable sums 0 to total//2,
            pick the LARGEST one (call it S1).
            Answer = total - 2 * S1

    ┌──────────────────────────────────────────────────────────────────┐
    │  Subset Sum:         "Can we make sum S?"         → True/False  │
    │  Equal Partition:    "Can we make sum total/2?"    → True/False  │
    │  Min Subset Diff:    "What's the BEST sum <= total/2?" → number │
    │                                                                  │
    │  All three use the SAME dp table. Only the QUESTION differs.     │
    └──────────────────────────────────────────────────────────────────┘

================================================================================
CHOICE DIAGRAM (identical to Subset Sum):
================================================================================

                    arr[i-1]
                   /         \\
        arr[i-1] <= j?       arr[i-1] > j?
         /         \\              |
      INCLUDE    EXCLUDE        EXCLUDE
         |          |              |
    dp[i-1]     dp[i-1][j]    dp[i-1][j]
    [j-arr[i-1]]

    dp[i][j] = include OR exclude

    NO CHANGE from subset sum. The only new part is READING the answer.

================================================================================
DP TABLE TRACE — arr = [1, 6, 11, 5], total = 23:
================================================================================

    dp[i][j] = True/False ("can first i items make sum j?")

         j→  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
    i=0      T  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
    i=1(1)   T  T  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
    i=2(6)   T  T  F  F  F  F  T  T  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
    i=3(11)  T  T  F  F  F  F  T  T  F  F  F  T  T  F  F  F  F  T  T  F  F  F  F  F
    i=4(5)   T  T  F  F  F  T  T  T  F  F  F  T  T  F  F  F  T  T  T  F  F  F  T  T

    LAST ROW (all achievable sums):
    j:  0  1  5  6  7  11  12  16  17  18  22  23
    T:  ✓  ✓  ✓  ✓  ✓   ✓   ✓   ✓   ✓   ✓   ✓   ✓

    total//2 = 11. Scan from j=11 downward:
        j=11: dp[4][11] = True → S1 = 11

    Answer = total - 2*S1 = 23 - 2*11 = 23 - 22 = 1 ✓

    Check: S1 = {11} = 11, S2 = {1,6,5} = 12, diff = |12-11| = 1 ✓

================================================================================
HOW TO READ THE ANSWER FROM THE DP TABLE:
================================================================================

    ┌─────────────────────────────────────────────────────────────────┐
    │  1. Look at LAST ROW of dp table: dp[n][0..total]              │
    │  2. Scan from j = total//2 down to 0                           │
    │  3. FIRST j where dp[n][j] == True → that's S1                 │
    │  4. Answer = total - 2 * S1                                     │
    └─────────────────────────────────────────────────────────────────┘

    WHY scan from total//2 downward?
        We want S1 as close to total/2 as possible.
        The first True we find scanning DOWN from total//2 is the best S1.

    WHY total - 2*S1?
        S1 + S2 = total
        diff = S2 - S1 = (total - S1) - S1 = total - 2*S1

================================================================================
ANOTHER EXAMPLE — arr = [1, 5, 11, 5], total = 22:
================================================================================

    Last row achievable sums: {0, 1, 5, 6, 10, 11, 16, 17, 21, 22}

    total//2 = 11. Scan from j=11:
        j=11: True → S1 = 11

    Answer = 22 - 2*11 = 0 ✓  (perfect partition: {1,5,5} = 11, {11} = 11)

================================================================================
COMPLEXITY:
================================================================================

    ┌──────────────────┬──────────────────────┬──────────────────────────┐
    │ Approach         │ Time                 │ Space                    │
    ├──────────────────┼──────────────────────┼──────────────────────────┤
    │ Recursion        │ O(2^n)               │ O(n) stack              │
    │ Memoization      │ O(n * total)         │ O(n * total) + stack    │
    │ Bottom-Up        │ O(n * total)         │ O(n * total)            │
    │ Bottom-Up (1D)   │ O(n * total)         │ O(total)               │
    └──────────────────┴──────────────────────┴──────────────────────────┘

    NOTE: target is total (not total/2) because we need ALL achievable sums.

================================================================================
5 TRICKS TO REMEMBER FOREVER:
================================================================================

    TRICK 1: "Same DP table as Subset Sum, different question"
        Build the EXACT same subset sum table.
        But instead of checking one cell, scan the LAST ROW.

    TRICK 2: "Answer = total - 2 * best_S1"
        S1 closest to total/2 → smallest difference.
        Formula: total - 2*S1. Memorize this.

    TRICK 3: "Scan last row from total//2 downward"
        First True value = best S1 = answer.

    TRICK 4: "If answer is 0, it's actually Equal Partition"
        Min diff = 0 means the array CAN be split into equal halves.
        Equal Partition is a special case of Min Subset Diff.

    TRICK 5: "1D space optimization works the same"
        dp = [False] * (total + 1), dp[0] = True
        Right-to-left fill, then scan dp[0..total//2] for last True.

================================================================================
RELATIONSHIP TO OTHER KNAPSACK PROBLEMS:
================================================================================

    ┌───────────────────────────────────────────────────────────────────┐
    │  Subset Sum:       "Can we make sum S?"                          │
    │  Equal Partition:  "Can we make sum total/2?" (special case)     │
    │  Min Subset Diff:  "Best achievable sum near total/2?"           │
    │                                                                   │
    │  Same DP table.                                                   │
    │  Subset Sum → checks dp[n][target]                               │
    │  Equal Partition → checks dp[n][total//2]                        │
    │  Min Subset Diff → scans dp[n][0..total//2] for best True        │
    └───────────────────────────────────────────────────────────────────┘

================================================================================
INTERVIEW QUICK-FIRE ANSWERS:
================================================================================

    Q: "How did you identify this?"
    A: "Partition into 2 groups, minimize difference = find S1 closest to total/2
        using subset sum DP."

    Q: "What's the formula?"
    A: "diff = total - 2*S1, where S1 is largest achievable sum <= total/2."

    Q: "How is this different from Equal Partition?"
    A: "Equal Partition asks 'can diff = 0?' This asks 'what's the minimum diff?'
        Same table, different question."

    Q: "Time and space?"
    A: "O(n * total) time, O(n * total) space. Can optimize to O(total) space."

    Q: "Can diff ever be negative?"
    A: "No, we take absolute value. By scanning up to total//2, S1 <= S2 always."

================================================================================
COMMON MISTAKES:
================================================================================

    ✗ Building dp table up to total//2 → WRONG, need ALL sums 0 to total
    ✗ Returning S1 instead of total - 2*S1 → formula matters
    ✗ Scanning from 0 upward → SLOW, scan from total//2 downward for efficiency
    ✗ Forgetting dp[i][0] = True initialization → empty subset always works

================================================================================
THE CODE BELOW IS CORRECT — All 4 approaches (recursion, memo, bottom-up,
space-optimized) from GeeksforGeeks. Verified working.
================================================================================
"""


# Mimimum subset sum diffrence
'''
arr=[1,6,11,5]
op=1

s1=s2=> s1-s2=0
need to take abs as minimum 
like {1+6=5},{11}
12-11=1 is minimum can we do better as per given no so it is the minimum
Partition a set into two subsets such that the difference of subset sums is minimum
Last Updated :
3 Aug, 2026
Given an array arr[] of size n, the task is to divide it into two sets s1 and s2 such that the absolute difference between their sums is minimum. 

Example: 

Input: arr = [1, 6, 11, 5]
Output: 1
Explanation: S1 = [1, 5, 6], sum = 12,  S2 = [11], sum = 11,  Absolute Difference (12 - 11) = 1

Input: arr = [1, 5, 11, 5]
Output: 0
Explanation: S1 = [1, 5, 5], sum = 11, S2 = [11], sum = 11, Absolute Difference (11 - 11) = 0 

Try It Yourself
redirect icon
Table of Content

Using Recursion - O(2^n) Time and O(n) Space
Using Top-Down DP (Memoization) - O(n*sumTotal) Time and O(n*sumTotal) Space
Using Bottom-Up DP (Tabulation) - O(n*sumTotal) Time and O(n*sumTotal) Space
Using Space Optimized DP - O(n*sumTotal) Time and O(sumTotal) Space
Using Recursion - O(2^n) Time and O(n) Space
For the recursive approach, there will be two cases:

Include the last element in the subset: The new sumCalculated becomes sumCalculated + arr[n-1].
Exclude the last element: Keep sumCalculated unchanged.
Mathematically, the recurrence relation is:

minDiff(arr, n, sumCalculated) = min(minDiff(arr, n-1, sumCalculated), minDiff(arr, n-1, sumCalculated + arr[n-1])).

Base Cases:

If n = 0: Return the absolute difference |(sumTotal - sumCalculated) - sumCalculated|.





# Python Code to partition a set into two
# subsets such that the difference
# of subset sums is minimum
​
# Function to calculate the minimum absolute difference
def find_min_difference(arr, n, sum_calculated, sum_total):
    
    # Base case: if we've considered all elements
    if n == 0:
        return abs((sum_total - sum_calculated) 
                            - sum_calculated)
​
    # Include the current element in the subset
    include = find_min_difference(arr, n - 1, 
                    sum_calculated + arr[n - 1], sum_total)
​
    # Exclude the current element from the subset
    exclude = find_min_difference(arr,
                       n - 1, sum_calculated, sum_total)
​
    # Return the minimum of both choices
    return min(include, exclude)
​
# Function to get the minimum difference
def min_difference(arr):
    sum_total = 0
    
    # Calculate total sum of the array
    for num in arr:
        sum_total += num
​
    # Call recursive function to find 
    # the minimum difference
    return find_min_difference(arr, 
                           len(arr), 0, sum_total)
​
if __name__ == "__main__":
​
    arr = [1, 6, 11, 5]
​
    print(min_difference(arr))

Output
1
Using Top-Down DP (Memoization) - O(n*sumTotal) Time and O(n*sumTotal) Space
Many subproblems are solved multiple times during recursion. Using a 2D memoization table of size (n+1) x (sumTotal+1), we store solutions for subproblems to avoid recomputation. Initialize all values to -1. If memo[n][sumCalculated] != -1, use the stored value.





# Python Code to partition a set into two
# subsets such that the difference
# of subset sums is minimum using memoization
​
# Function to calculate the minimum absolute
# difference with memoization
def find_min_difference(arr, n, sum_calculated, sum_total, memo):
    
    # Base case: if we've considered all elements
    if n == 0:
        return abs((sum_total - sum_calculated) 
                            - sum_calculated)
​
    # Check if result is already computed
    if memo[n][sum_calculated] != -1:
        return memo[n][sum_calculated]
​
    # Include the current element in the subset
    include = find_min_difference(arr, n - 1, 
                    sum_calculated + arr[n - 1], sum_total, memo)
​
    # Exclude the current element from the subset
    exclude = find_min_difference(arr, n - 1, 
                                   sum_calculated, sum_total, memo)
​
    # Store the result in memo and return
    memo[n][sum_calculated] = min(include, exclude)
    return memo[n][sum_calculated]
​
# Function to get the minimum difference
def min_difference(arr):
    sum_total = sum(arr) 
    
    # Create a memoization table initialized to -1
    memo = [[-1 for _ in range(sum_total + 1)] for _ in range(len(arr) + 1)]
​
    # Call the recursive function with memoization
    return find_min_difference(arr, len(arr), 0, sum_total, memo)
​
if __name__ == "__main__":
    arr = [1, 6, 11, 5]
    print(min_difference(arr))

Output
1
Using Bottom-Up DP (Tabulation) - O(n*sumTotal) Time and O(n*sumTotal) Space
This approach iteratively builds the solution in a bottom-up manner instead of solving it recursively. We use a 2D DP table of size (n + 1) x (sumTotal + 1) where: dp[i][j] = true if a subset of elements from arr[0...i] has a sum of j.

If the current element (arr[i-1]) is greater than the sum j:

dp[i][j] = dp[i-1][j]
Otherwise, we check:

Include the element: dp[i-1][j - arr[i-1]]
Exclude the element: dp[i-1][j]
Final result: dp[i][j] = dp[i-1][j] || dp[i-1][j - arr[i-1]]





# Python Code to partition a set into two
# subsets such that the difference
# of subset sums is minimum using tabulation
​
# Function to get the minimum difference
# using tabulation
def min_difference(arr):
    sum_total = sum(arr)
​
    n = len(arr)
​
    # Create a DP table where dp[i][j] represents if a subset
    # sum 'j' is achievable using the first 'i' elements
    dp = [[False for _ in range(sum_total + 1)] for _ in range(n + 1)]
​
    # A sum of 0 is always achievable (empty subset)
    dp[0][0] = True
​
    # Fill the DP table
    for i in range(1, n + 1):
        for sum_val in range(0, sum_total + 1):
            # Exclude the current element
            dp[i][sum_val] = dp[i - 1][sum_val]
​
            # Include the current element if sum_val >= arr[i-1]
            if sum_val >= arr[i - 1]:
                dp[i][sum_val] = dp[i][sum_val] \
                        or dp[i - 1][sum_val - arr[i - 1]]
​
    # Find the minimum difference
    min_diff = float('inf')
​
    # Iterate over all possible subset sums and 
    # find the minimum difference
    for sum_val in range(0, sum_total // 2 + 1):
        if dp[n][sum_val]:
            min_diff = min(min_diff, \
                      abs((sum_total - sum_val) - sum_val))
​
    return min_diff
​
​
if __name__ == "__main__":
  
    arr = [1, 6, 11, 5]
    print(min_difference(arr))

Output
1
Using Space Optimized DP - O(n*sumTotal) Time and O(sumTotal) Space
In the previous approach, we derived the relation between states as follows:

if (arr[i-1] > j)

dp[i][j] = dp[i-1][j]

else 

dp[i][j] = dp[i-1][j] || dp[i-1][j-arr[i-1]]

Here, for calculating the current state dp[i][j], we only require values from the previous row: dp[i-1][j] and dp[i-1][j-arr[i-1]]. This observation eliminates the need to store the entire DP table, as only the previous row is needed to compute the current one. Use a single 1D array (dp) of sizesumTotal + 1 to store achievable subset sums.

dp[j] = dp[j] || dp[j - arr[i-1]];





    dp[0] = True  

    # Fill the DP array
    for num in arr:
        for sum_val in range(sum_total, num - 1, -1):
            dp[sum_val] = dp[sum_val] or dp[sum_val - num]

    # Find the minimum difference
    min_diff = sum_total
    for sum_val in range(sum_total // 2 + 1):
        if dp[sum_val]:
            min_diff = min(min_diff, abs((sum_total - sum_val) - sum_val))

    return min_diff

arr = [1, 6, 11, 5]
print(min_difference(arr))
# Python code to partition a set into two subsets
# with min diff with space optimization
def min_difference(arr):
    sum_total = sum(arr)
​
    # Create a 1D DP array to track 
    # achievable subset sums
    dp = [False] * (sum_total + 1)
    dp[0] = True  
​
    # Fill the DP array
    for num in arr:
        for sum_val in range(sum_total, num - 1, -1):
            dp[sum_val] = dp[sum_val] or dp[sum_val - num]
​
    # Find the minimum difference
    min_diff = sum_total
    for sum_val in range(sum_total // 2 + 1):
        if dp[sum_val]:
            min_diff = min(min_diff, abs((sum_total - sum_val) - sum_val))
​
    return min_diff
​
arr = [1, 6, 11, 5]
print(min_difference(arr))

Output


'''

# ══════════════════════════════════════════════════════════════════
# MINIMUM SUBSET SUM DIFFERENCE — Working Code (All 3 approaches)
# ══════════════════════════════════════════════════════════════════

arr = [1, 6, 11, 5]

def _array_sum(a):
    s = 0
    for x in a:
        s += x
    return s

# 1. Recursion — O(2^n) time, O(n) space
def min_subset_diff_recursion(arr):
    total = _array_sum(arr)
    n = len(arr)

    def helper(i, sum_calculated):
        if i == 0:
            return abs(total - 2 * sum_calculated)
        include = helper(i - 1, sum_calculated + arr[i - 1])
        exclude = helper(i - 1, sum_calculated)
        return min(include, exclude)

    return helper(n, 0)

print("\n--- Minimum Subset Sum Difference ---")
print("Recursion:", min_subset_diff_recursion(arr))


# 2. Memoization — O(n * total) time, O(n * total) space
def min_subset_diff_memo(arr):
    total = _array_sum(arr)
    n = len(arr)
    memo = [[-1] * (total + 1) for _ in range(n + 1)]

    def helper(i, sum_calculated):
        if i == 0:
            return abs(total - 2 * sum_calculated)
        if memo[i][sum_calculated] != -1:
            return memo[i][sum_calculated]
        include = helper(i - 1, sum_calculated + arr[i - 1])
        exclude = helper(i - 1, sum_calculated)
        memo[i][sum_calculated] = min(include, exclude)
        return memo[i][sum_calculated]

    return helper(n, 0)

print("Memoization:", min_subset_diff_memo(arr))


# 3. Bottom-Up — O(n * total) time, O(n * total) space
def min_subset_diff_bottom_up(arr):
    total = _array_sum(arr)
    n = len(arr)

    # subset sum dp: dp[i][j] = can first i elements make sum j?
    dp = [[False] * (total + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # scan last row from total//2 downward for best S1
    for s in range(total // 2, -1, -1):
        if dp[n][s]:
            return total - 2 * s

print("Bottom-Up:", min_subset_diff_bottom_up(arr))


# 4. Space Optimized — O(n * total) time, O(total) space
def min_subset_diff_optimized(arr):
    total = _array_sum(arr)
    dp = [False] * (total + 1)
    dp[0] = True

    for num in arr:
        for j in range(total, num - 1, -1):  # right to left
            dp[j] = dp[j] or dp[j - num]

    for s in range(total // 2, -1, -1):
        if dp[s]:
            return total - 2 * s

print("Space Optimized:", min_subset_diff_optimized(arr))


"""
================================================================================
================================================================================
    COUNT OF SUBSETS WITH GIVEN DIFFERENCE — Complete FAANG Guide
================================================================================
================================================================================

PROBLEM STATEMENT:
    Given array arr[] and integer diff, count the number of ways to partition
    the array into two subsets S1 and S2 such that sum(S1) - sum(S2) = diff.

    Example 1: arr = [5, 2, 6, 4], diff = 3
        Partition: S1 = {6,4} = 10, S2 = {5,2} = 7, diff = 10-7 = 3
        Answer: 1

    Example 2: arr = [1, 1, 1, 1], diff = 0
        Answer: 6 (choose any 2 of the four 1's for S1, rest go to S2)

    Example 3: arr = [3, 2, 7, 1], diff = 4
        Answer: 0 (no valid partition)

================================================================================
ONE-LINE TRICK TO NEVER FORGET:
================================================================================

    "S1 - S2 = diff, S1 + S2 = total. So S1 = (total + diff) / 2.
     Count subsets with sum = (total + diff) / 2."

================================================================================
THE MATHEMATICAL DERIVATION (write this in interview):
================================================================================

    S1 - S2 = diff      ... (1)
    S1 + S2 = total     ... (2)  (all elements used)

    Add (1) + (2):
        2 * S1 = diff + total
        S1 = (diff + total) / 2 = target

    So the problem becomes:
        "Count subsets with sum = target"
        Where target = (total + diff) / 2

    This is EXACTLY the "Count of Subset Sum" problem!

    EDGE CASES (check BEFORE running DP):
        1. (total + diff) is ODD → return 0 (can't have fractional target)
        2. total < diff → return 0 (impossible, can't achieve that diff)

================================================================================
HOW THIS CONNECTS TO THE KNAPSACK FAMILY:
================================================================================

    ┌─────────────────────────────────────────────────────────────────┐
    │                                                                 │
    │  "Count subsets with given diff"                                │
    │       ↓ (reduce)                                                │
    │  "Count subsets with sum = (total + diff) / 2"                  │
    │       ↓ (which is)                                              │
    │  "Count of Subset Sum" (Problem 3 in our family)                │
    │       ↓ (which uses)                                            │
    │  dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]                  │
    │  (+ operator, int dp, same knapsack skeleton)                   │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘

    This is IDENTICAL to Target Sum (LC 494)!
        Target Sum:        target = (total + target) / 2
        Subsets with Diff: target = (total + diff)   / 2
        Same formula, same code, different variable name.

================================================================================
EXAMPLE WALKTHROUGH — arr = [5, 2, 6, 4], diff = 3:
================================================================================

    total = 5 + 2 + 6 + 4 = 17
    target = (17 + 3) / 2 = 20 / 2 = 10

    "Count subsets of [5, 2, 6, 4] that sum to 10"

    Possible subsets summing to 10:
        {6, 4} = 10 ✓

    Answer: 1 ✓

    Verify: S1 = {6,4} = 10, S2 = {5,2} = 7, diff = 10 - 7 = 3 ✓

================================================================================
EXAMPLE 2 — arr = [1, 1, 1, 1], diff = 0:
================================================================================

    total = 4
    target = (4 + 0) / 2 = 2

    "Count subsets of [1, 1, 1, 1] that sum to 2"

    Pick any 2 out of 4 ones: C(4,2) = 6 subsets

    Answer: 6 ✓

================================================================================
CHOICE DIAGRAM (same as Count of Subset Sum):
================================================================================

                    arr[i-1]
                   /         \\
        arr[i-1] <= j?       arr[i-1] > j?
         /         \\              |
      INCLUDE    EXCLUDE        EXCLUDE
         |          |              |
    dp[i-1]     dp[i-1][j]    dp[i-1][j]
    [j-arr[i-1]]

    dp[i][j] = INCLUDE + EXCLUDE  (count both paths)

================================================================================
DP TABLE TRACE — arr = [5, 2, 6, 4], target = 10:
================================================================================

    dp[i][j] = number of subsets using first i elements that sum to j

         j→  0   1   2   3   4   5   6   7   8   9  10
    i=0      1   0   0   0   0   0   0   0   0   0   0
    i=1(5)   1   0   0   0   0   1   0   0   0   0   0
    i=2(2)   1   0   1   0   0   1   0   1   0   0   0
    i=3(6)   1   0   1   0   0   1   1   1   1   0   0
    i=4(4)   1   0   1   0   1   1   1   1   1   1   1

    dp[4][10] = 1 ✓

    How to read: there is exactly 1 subset of [5,2,6,4] summing to 10.

================================================================================
DP TABLE TRACE — arr = [1, 1, 1, 1], target = 2:
================================================================================

         j→  0   1   2
    i=0      1   0   0
    i=1(1)   1   1   0
    i=2(1)   1   2   1
    i=3(1)   1   3   3
    i=4(1)   1   4   6

    dp[4][2] = 6 ✓ (C(4,2) = 6 ways to pick 2 ones)

================================================================================
INITIALIZATION:
================================================================================

    dp[0][0] = 1    ← one way to make sum 0 (empty subset)
    dp[0][j] = 0    ← for j > 0, 0 elements can't make positive sum

    IMPORTANT: dp[i][0] is NOT always 1 here!
    dp[i][0] = number of subsets of first i elements that sum to 0.
    If arr has zeros, dp[i][0] could be > 1. But for positive arrays, dp[i][0] = 1.

================================================================================
COMPLEXITY:
================================================================================

    ┌──────────────────┬──────────────────────┬──────────────────────────┐
    │ Approach         │ Time                 │ Space                    │
    ├──────────────────┼──────────────────────┼──────────────────────────┤
    │ Recursion        │ O(2^n)               │ O(n) stack              │
    │ Memoization      │ O(n * target)        │ O(n * target) + stack   │
    │ Bottom-Up        │ O(n * target)        │ O(n * target)           │
    │ Space Optimized  │ O(n * target)        │ O(target)              │
    └──────────────────┴──────────────────────┴──────────────────────────┘

    Where target = (total + diff) / 2

================================================================================
5 TRICKS TO REMEMBER:
================================================================================

    TRICK 1: "Math first, code second"
        S1 = (total + diff) / 2. Derive this FIRST, then it's just Count Subsets.

    TRICK 2: "Two edge cases kill you"
        (total + diff) is odd → 0
        total < diff → 0
        Check both BEFORE creating the dp table.

    TRICK 3: "Same code as Target Sum (LC 494)"
        Target Sum: target = (total + target) / 2
        This problem: target = (total + diff) / 2
        Literally the same formula.

    TRICK 4: "Count = use + operator, not OR"
        Subset Sum uses OR (True/False).
        Count of Subsets uses + (add counts).
        This problem counts → use +.

    TRICK 5: "1D optimization: right-to-left, += instead of ="
        dp[j] += dp[j - arr[i]]  (not dp[j] = ...)
        Because we're COUNTING (adding to existing count).

================================================================================
INTERVIEW QUICK-FIRE:
================================================================================

    Q: "How did you reduce this?"
    A: "S1 - S2 = diff, S1 + S2 = total, solve for S1 = (total+diff)/2,
        then count subsets with that sum."

    Q: "What if diff is negative?"
    A: "Take abs(diff). S1 is always the larger subset by convention."

    Q: "What if array has zeros?"
    A: "Each zero doubles the count (can go in either subset).
        Handle carefully in dp[i][0] initialization."

    Q: "Relation to Target Sum (LC 494)?"
    A: "Identical. Target Sum assigns +/- signs, which is the same as partitioning
        into S1 (positive) and S2 (negative). Same formula."

================================================================================
COMMON MISTAKES:
================================================================================

    ✗ Forgetting (total + diff) % 2 != 0 check → wrong answer
    ✗ Forgetting total < diff check → negative target → crash
    ✗ Using OR instead of + → gives True/False not count
    ✗ dp[0][0] = 0 instead of 1 → misses all valid subsets
    ✗ Left-to-right in 1D → reuses elements (unbounded behavior)

================================================================================
"""

# ══════════════════════════════════════════════════════════════════
# COUNT OF SUBSETS WITH GIVEN DIFFERENCE — Working Code
# ══════════════════════════════════════════════════════════════════

print("\n--- Count of Subsets with Given Difference ---")

# 1. Recursion — O(2^n) time, O(n) space
def count_partitions_recursion(arr, diff):
    total = _array_sum(arr)

    if (total + diff) % 2 != 0 or total < diff:
        return 0

    target = (total + diff) // 2
    n = len(arr)

    def helper(i, curr_sum):
        if i == n:
            return 1 if curr_sum == target else 0
        exclude = helper(i + 1, curr_sum)
        include = 0
        if curr_sum + arr[i] <= target:
            include = helper(i + 1, curr_sum + arr[i])
        return include + exclude

    return helper(0, 0)

print("arr=[5,2,6,4] diff=3 Recursion:", count_partitions_recursion([5, 2, 6, 4], 3))
print("arr=[1,1,1,1] diff=0 Recursion:", count_partitions_recursion([1, 1, 1, 1], 0))


# 2. Memoization — O(n * target) time, O(n * target) space
def count_partitions_memo(arr, diff):
    total = _array_sum(arr)

    if (total + diff) % 2 != 0 or total < diff:
        return 0

    target = (total + diff) // 2
    n = len(arr)
    dp = [[-1] * (target + 1) for _ in range(n + 1)]

    def helper(i, curr_sum):
        if i == n:
            return 1 if curr_sum == target else 0
        if dp[i][curr_sum] != -1:
            return dp[i][curr_sum]
        exclude = helper(i + 1, curr_sum)
        include = 0
        if curr_sum + arr[i] <= target:
            include = helper(i + 1, curr_sum + arr[i])
        dp[i][curr_sum] = include + exclude
        return dp[i][curr_sum]

    return helper(0, 0)

print("arr=[5,2,6,4] diff=3 Memo:", count_partitions_memo([5, 2, 6, 4], 3))
print("arr=[1,1,1,1] diff=0 Memo:", count_partitions_memo([1, 1, 1, 1], 0))


# 3. Bottom-Up — O(n * target) time, O(n * target) space
def count_partitions_bottom_up(arr, diff):
    total = _array_sum(arr)

    if (total + diff) % 2 != 0 or total < diff:
        return 0

    target = (total + diff) // 2
    n = len(arr)

    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # one way to make sum 0 with 0 elements

    for i in range(1, n + 1):
        for j in range(target + 1):
            dp[i][j] = dp[i - 1][j]  # exclude
            if j >= arr[i - 1]:
                dp[i][j] += dp[i - 1][j - arr[i - 1]]  # include

    return dp[n][target]

print("arr=[5,2,6,4] diff=3 Bottom-Up:", count_partitions_bottom_up([5, 2, 6, 4], 3))
print("arr=[1,1,1,1] diff=0 Bottom-Up:", count_partitions_bottom_up([1, 1, 1, 1], 0))


# 4. Space Optimized — O(n * target) time, O(target) space
def count_partitions_optimized(arr, diff):
    total = _array_sum(arr)

    if (total + diff) % 2 != 0 or total < diff:
        return 0

    target = (total + diff) // 2
    n = len(arr)

    dp = [0] * (target + 1)
    dp[0] = 1  # one way to make sum 0

    for i in range(n):
        for j in range(target, arr[i] - 1, -1):  # right to left
            dp[j] += dp[j - arr[i]]

    return dp[target]

print("arr=[5,2,6,4] diff=3 Optimized:", count_partitions_optimized([5, 2, 6, 4], 3))
print("arr=[1,1,1,1] diff=0 Optimized:", count_partitions_optimized([1, 1, 1, 1], 0))
print("arr=[3,2,7,1] diff=4 Optimized:", count_partitions_optimized([3, 2, 7, 1], 4))


"""
================================================================================
================================================================================
    TARGET SUM (LeetCode 494) — Complete FAANG Guide
================================================================================
================================================================================

PROBLEM STATEMENT:
    Given array arr[] and integer target, assign '+' or '-' before each element.
    Count the number of expressions that evaluate to target.

    Example 1: arr = [1, 1, 1, 1, 1], target = 3
        -1+1+1+1+1 = 3, +1-1+1+1+1 = 3, +1+1-1+1+1 = 3,
        +1+1+1-1+1 = 3, +1+1+1+1-1 = 3
        Answer: 5

    Example 2: arr = [1, 2, 2, 1], target = 2
        +1-2+2+1 = 2, +1+2-2+1 = 2
        Answer: 2

    Example 3: arr = [1], target = 1
        Answer: 1 (+1 = 1)

================================================================================
ONE-LINE TRICK TO NEVER FORGET:
================================================================================

    "Assign + or - = partition into P (plus) and N (minus).
     P = (total + target) / 2. Count subsets with that sum."

================================================================================
THE MATHEMATICAL DERIVATION (same as #Subsets with Diff):
================================================================================

    Let P = sum of elements with '+'
    Let N = sum of elements with '-'

    P - N = target       ... (1)  (the expression evaluates to target)
    P + N = total        ... (2)  (all elements used, just with +/- signs)

    Add (1) + (2):
        2P = target + total
        P = (target + total) / 2

    PROBLEM REDUCES TO:
        "Count subsets with sum = (target + total) / 2"

    This is EXACTLY "Count of Subset Sum" problem!

    EDGE CASES (return 0 immediately):
        1. (total + target) is ODD → impossible (can't have fractional sum)
        2. |target| > total → impossible (even all + or all - can't reach it)

================================================================================
WHY THIS IS THE SAME AS "COUNT SUBSETS WITH GIVEN DIFFERENCE":
================================================================================

    Target Sum:           target = "diff between + set and - set"
    #Subsets with Diff:   diff = "difference between S1 and S2"

    They are LITERALLY the same problem with different names:
        Target Sum formula:        P = (total + target) / 2
        Subsets with Diff formula:  S1 = (total + diff) / 2

    Same formula. Same code. Only variable names differ.

================================================================================
TWO APPROACHES TO SOLVE:
================================================================================

    APPROACH A: Subset Sum Reduction (PREFERRED in interviews)
        → Reduce to "count subsets with sum = (total + target) / 2"
        → Standard 0/1 knapsack counting DP
        → Time: O(n * target'), Space: O(target')
        → Where target' = (total + target) / 2

    APPROACH B: Direct +/- simulation
        → Track all possible sums at each step
        → Sums can be negative → need offset or range [-total, +total]
        → Time: O(n * total), Space: O(total)
        → Useful when array has zeros or you can't reduce easily

    APPROACH A is cleaner, shorter, and preferred. Approach B is shown below
    for completeness (GeeksforGeeks style).

================================================================================
EXAMPLE WALKTHROUGH — arr = [1, 1, 1, 1, 1], target = 3:
================================================================================

    total = 5
    P = (5 + 3) / 2 = 4

    "Count subsets of [1, 1, 1, 1, 1] that sum to 4"

    Pick any 4 out of 5 ones: C(5,4) = 5 subsets

    Answer: 5 ✓

    Verify one: P = {1,1,1,1} (indices 1,2,3,4) = +4
                N = {1} (index 0) = -1
                Expression: -1+1+1+1+1 = 3 ✓

================================================================================
EXAMPLE 2 — arr = [1, 2, 2, 1], target = 2:
================================================================================

    total = 6
    P = (6 + 2) / 2 = 4

    "Count subsets of [1, 2, 2, 1] that sum to 4"

    Subsets: {1, 2, 1} (indices 0,1,3) = 4 ✓
             {1, 2, 1} (indices 0,2,3) = 4 ✓

    Answer: 2 ✓

================================================================================
DP TABLE TRACE (Subset Sum Approach) — arr = [1,1,1,1,1], target' = 4:
================================================================================

    dp[i][j] = number of subsets using first i elements summing to j

         j→  0   1   2   3   4
    i=0      1   0   0   0   0
    i=1(1)   1   1   0   0   0
    i=2(1)   1   2   1   0   0
    i=3(1)   1   3   3   1   0
    i=4(1)   1   4   6   4   1
    i=5(1)   1   5  10  10   5

    dp[5][4] = 5 ✓  (C(5,4) = 5)

================================================================================
DP TABLE (Direct Approach) — arr = [1,1,1,1,1], offset = 5:
================================================================================

    Sum range: [-5, +5]. Use offset = 5. Index = sum + 5.

    After processing all elements, dp[target + offset] = dp[3 + 5] = dp[8] = 5

    This approach tracks EVERY possible sum (including negatives).
    Columns represent sums from -5 to +5 (indices 0 to 10).

================================================================================
COMPLEXITY:
================================================================================

    ┌──────────────────────┬──────────────────────┬──────────────────────┐
    │ Approach             │ Time                 │ Space                │
    ├──────────────────────┼──────────────────────┼──────────────────────┤
    │ Recursion            │ O(2^n)               │ O(n) stack          │
    │ Memo (offset-based)  │ O(n * 2*total)       │ O(n * 2*total)      │
    │ Bottom-Up (offset)   │ O(n * 2*total)       │ O(n * 2*total)      │
    │ Space Opt (offset)   │ O(n * 2*total)       │ O(2*total)          │
    │ Subset Sum Reduction │ O(n * P)             │ O(P)                │
    └──────────────────────┴──────────────────────┴──────────────────────┘

    P = (total + target) / 2. Subset Sum Reduction is FASTER when P < total.

================================================================================
5 TRICKS TO REMEMBER:
================================================================================

    TRICK 1: "Assign +/- = partition into P and N"
        Don't think of it as 2^n expressions.
        Think: split array into "positive group" P and "negative group" N.
        P - N = target → P = (total + target) / 2.

    TRICK 2: "Same as Subsets with Given Difference"
        target (here) = diff (there). Literally same formula, same code.

    TRICK 3: "Subset Sum Reduction is ALWAYS preferred"
        Shorter code, often faster (P might be << total).
        Only use direct +/- approach if interviewer insists or array has zeros.

    TRICK 4: "Two edge cases before DP"
        (total + target) is odd → return 0
        abs(target) > total → return 0
        Forgetting these = wrong answer on edge cases.

    TRICK 5: "Direct approach needs OFFSET for negative sums"
        Sums range from -total to +total = 2*total+1 states.
        Map sum s to index s + total (offset).
        dp[0][total] = 1 (sum 0 at index offset).

================================================================================
WHICH APPROACH TO USE IN INTERVIEW:
================================================================================

    "I'll reduce this to Count Subset Sum.
     P - N = target, P + N = total, so P = (total + target)/2.
     Then count subsets summing to P using the standard 0/1 knapsack DP."

    → 4 lines of math + standard template = done.

    If interviewer asks "what about zeros in array?"
    → The direct +/- approach handles zeros better.
    → With subset sum reduction, zeros make dp[i][0] tricky.

================================================================================
COMMON MISTAKES:
================================================================================

    ✗ Using target directly as dp column size (need P = (total+target)/2)
    ✗ Forgetting abs(target) > total check → negative array size
    ✗ Forgetting (total + target) odd check → fractional target
    ✗ In direct approach: forgetting offset → negative index crash
    ✗ In direct approach: checking j+val <= 2*total but missing j-val >= 0

================================================================================
"""

# ══════════════════════════════════════════════════════════════════
# TARGET SUM (LC 494) — Working Code (Both approaches)
# ══════════════════════════════════════════════════════════════════

print("\n--- Target Sum (LC 494) ---")

# ─── APPROACH A: Subset Sum Reduction (Preferred) ───

# 1. Recursion — O(2^n) time
def target_sum_recursion(arr, target):
    total = _array_sum(arr)
    if (total + target) % 2 != 0 or abs(target) > total:
        return 0
    P = (total + target) // 2
    n = len(arr)

    def helper(i, curr_sum):
        if i == n:
            return 1 if curr_sum == P else 0
        exclude = helper(i + 1, curr_sum)
        include = 0
        if curr_sum + arr[i] <= P:
            include = helper(i + 1, curr_sum + arr[i])
        return include + exclude

    return helper(0, 0)

print("Subset Sum Reduction:")
print("  [1,1,1,1,1] target=3:", target_sum_recursion([1,1,1,1,1], 3))
print("  [1,2,2,1] target=2:", target_sum_recursion([1,2,2,1], 2))


# 2. Bottom-Up (Subset Sum Reduction) — O(n * P) time, O(n * P) space
def target_sum_bottom_up(arr, target):
    total = _array_sum(arr)
    if (total + target) % 2 != 0 or abs(target) > total:
        return 0
    P = (total + target) // 2
    n = len(arr)

    dp = [[0] * (P + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(P + 1):
            dp[i][j] = dp[i - 1][j]  # exclude
            if j >= arr[i - 1]:
                dp[i][j] += dp[i - 1][j - arr[i - 1]]  # include

    return dp[n][P]

print("  [1,1,1,1,1] target=3 BottomUp:", target_sum_bottom_up([1,1,1,1,1], 3))
print("  [1,2,2,1] target=2 BottomUp:", target_sum_bottom_up([1,2,2,1], 2))


# 3. Space Optimized (Subset Sum Reduction) — O(n * P) time, O(P) space
def target_sum_optimized(arr, target):
    total = _array_sum(arr)
    if (total + target) % 2 != 0 or abs(target) > total:
        return 0
    P = (total + target) // 2
    n = len(arr)

    dp = [0] * (P + 1)
    dp[0] = 1

    for i in range(n):
        for j in range(P, arr[i] - 1, -1):  # right to left
            dp[j] += dp[j - arr[i]]

    return dp[P]

print("  [1,1,1,1,1] target=3 Optimized:", target_sum_optimized([1,1,1,1,1], 3))
print("  [1,2,2,1] target=2 Optimized:", target_sum_optimized([1,2,2,1], 2))
print("  [1] target=1 Optimized:", target_sum_optimized([1], 1))


# ─── APPROACH B: Direct +/- simulation (offset-based) ───

print("\nDirect +/- Approach:")

# 4. Recursion (direct) — O(2^n) time
def target_sum_direct_recursion(arr, target):
    n = len(arr)

    def helper(i, s):
        if i == n:
            return 1 if s == target else 0
        return helper(i + 1, s + arr[i]) + helper(i + 1, s - arr[i])

    return helper(0, 0)

print("  [1,1,1,1,1] target=3:", target_sum_direct_recursion([1,1,1,1,1], 3))


# 5. Bottom-Up (offset-based) — O(n * 2*total) time, O(n * 2*total) space
def target_sum_direct_bottom_up(arr, target):
    total = _array_sum(arr)
    if abs(target) > total:
        return 0
    n = len(arr)
    size = 2 * total + 1  # sums range from -total to +total
    offset = total          # map sum s to index s + offset

    dp = [[0] * size for _ in range(n + 1)]
    dp[0][offset] = 1  # sum 0 → index offset

    for i in range(1, n + 1):
        val = arr[i - 1]
        for j in range(size):
            if dp[i - 1][j] != 0:
                if j + val < size:
                    dp[i][j + val] += dp[i - 1][j]
                if j - val >= 0:
                    dp[i][j - val] += dp[i - 1][j]

    return dp[n][target + offset]

print("  [1,1,1,1,1] target=3 BottomUp:", target_sum_direct_bottom_up([1,1,1,1,1], 3))
print("  [1,2,2,1] target=2 BottomUp:", target_sum_direct_bottom_up([1,2,2,1], 2))


# 6. Space Optimized (offset-based) — O(n * 2*total) time, O(total) space
def target_sum_direct_optimized(arr, target):
    total = _array_sum(arr)
    if abs(target) > total:
        return 0
    n = len(arr)
    size = 2 * total + 1
    offset = total

    prev = [0] * size
    prev[offset] = 1

    for i in range(n):
        curr = [0] * size
        val = arr[i]
        for s in range(size):
            if prev[s] != 0:
                if s + val < size:
                    curr[s + val] += prev[s]
                if s - val >= 0:
                    curr[s - val] += prev[s]
        prev = curr

    return prev[target + offset]

print("  [1,1,1,1,1] target=3 Optimized:", target_sum_direct_optimized([1,1,1,1,1], 3))
print("  [1,2,2,1] target=2 Optimized:", target_sum_direct_optimized([1,2,2,1], 2))
print("  [1] target=1 Optimized:", target_sum_direct_optimized([1], 1))
