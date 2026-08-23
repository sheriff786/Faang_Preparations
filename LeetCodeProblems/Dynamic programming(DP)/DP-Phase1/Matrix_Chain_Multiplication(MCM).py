"""
================================================================================
================================================================================
    MCM (MATRIX CHAIN MULTIPLICATION) — COMPLETE FAANG INTERVIEW GUIDE
================================================================================
================================================================================

PATTERN: MCM / Partition DP (the MOTHER of all "split the range" problems)
DIFFICULTY: Medium-Hard
FREQUENCY: Very High (Google, Amazon, Microsoft, Meta, Apple)

================================================================================
WHY MCM IS THE #1 PARTITION DP PATTERN:
================================================================================

    MCM is the foundation for 8+ other DP problems:

    ┌─────────────────────────────────────────────────────────────────────┐
    │                          MCM                                       │
    │                           │                                        │
    │    ┌────────┬─────────┬───┼────┬──────────┬──────────┬──────────┐  │
    │    ▼        ▼         ▼   ▼    ▼          ▼          ▼          ▼  │
    │ Palindrome Boolean  Scramble Egg     Burst     Min Cost   Optimal  │
    │ Partition  Parenth- String   Drop    Balloons  to Merge   Binary   │
    │ (LC 132)   esization(LC 87) (LC 887)(LC 312)  Stones     Search   │
    │            (GFG)                     (LC 1000) Tree               │
    └─────────────────────────────────────────────────────────────────────┘

    Learn MCM ONCE → solve 8+ problems automatically.

================================================================================
HOW TO IDENTIFY MCM PATTERN (THE GOLDEN RULE):
================================================================================

    Ask these 3 questions:

    1. Is there a STRING or ARRAY?                           → YES
    2. Do I need to SPLIT/PARTITION it at every possible k?  → YES
    3. Does left part + right part give me the answer?       → YES = MCM!

    KEYWORD SPOTTERS in problem statement:
    ┌────────────────────────────────────────────────────────────────┐
    │ "partition"              → MCM pattern                        │
    │ "split", "break", "cut"  → MCM pattern                        │
    │ "merge", "combine"       → MCM pattern (reverse direction)    │
    │ "parenthesize"           → MCM pattern                        │
    │ "minimum/maximum cost"   → MCM with min/max optimization      │
    │ "number of ways"         → MCM with counting                  │
    │ "range [i, j]"           → MCM (2 pointers on range)          │
    └────────────────────────────────────────────────────────────────┘

================================================================================
THE MCM UNIVERSAL TEMPLATE (MEMORIZE THIS — it solves EVERYTHING):
================================================================================

    ┌─────────────────────────────────────────────────────────────────┐
    │                                                                 │
    │  def solve(arr, i, j):                                          │
    │                                                                 │
    │      # Step 1: BASE CASE (smallest invalid input)               │
    │      if i >= j:                                                 │
    │          return 0                                                │
    │                                                                 │
    │      # Step 2: INITIALIZE answer                                │
    │      ans = float('inf')   # or float('-inf') for MAX problems   │
    │                                                                 │
    │      # Step 3: TRY ALL PARTITIONS (k loop)                      │
    │      for k in range(i, j):   # k goes from i to j-1             │
    │                                                                 │
    │          # Step 4: SOLVE left + right + MERGE COST               │
    │          temp = solve(arr, i, k) + solve(arr, k+1, j) + cost    │
    │                                                                 │
    │          # Step 5: OPTIMIZE (min/max/count)                      │
    │          ans = min(ans, temp)  # or max, or +=                   │
    │                                                                 │
    │      return ans                                                  │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘

    WHAT CHANGES PER PROBLEM:
    ┌──────────────────────┬──────────────┬──────────────┬─────────────┐
    │ Problem              │ Base Case    │ k range      │ Merge Cost  │
    ├──────────────────────┼──────────────┼──────────────┼─────────────┤
    │ MCM                  │ i >= j       │ i to j-1     │ a[i-1]*a[k]*a[j] │
    │ Palindrome Partition │ i >= j       │ i to j-1     │ +1 if palindrome │
    │ Boolean Parenth.     │ i == j       │ i+1 to j-1   │ operator logic│
    │ Scramble String      │ len == 0     │ 1 to len-1   │ substring check│
    │ Egg Dropping         │ e==1 or f==0 │ 1 to f       │ 1 + max(up,down)│
    │ Burst Balloons       │ i > j        │ i to j       │ a[i-1]*a[k]*a[j+1]│
    └──────────────────────┴──────────────┴──────────────┴─────────────┘

================================================================================
RECURSION → MEMOIZATION → BOTTOM-UP CONVERSION (3 Steps):
================================================================================

    ┌─────────────────────────────────────────────────────────────────┐
    │                                                                 │
    │  STEP 1: RECURSION → MEMOIZATION (add 3 lines)                 │
    │    1. Create memo[n][n] = -1                                    │
    │    2. Before computing: if memo[i][j] != -1: return memo[i][j]  │
    │    3. Before returning: memo[i][j] = ans                        │
    │                                                                 │
    │  STEP 2: MEMOIZATION → BOTTOM-UP                               │
    │    1. Identify what i,j represent (range endpoints)             │
    │    2. Build from SMALL gaps to LARGE gaps                       │
    │       (gap = j - i, from gap=0 to gap=n-1)                     │
    │    3. Answer = dp[start][end] (full range)                      │
    │                                                                 │
    │  BOTTOM-UP KEY INSIGHT:                                         │
    │    In MCM, we iterate by GAP SIZE (diagonal filling)            │
    │    NOT row-by-row like knapsack!                                │
    │                                                                 │
    │    for gap in range(0, n):        # gap = j - i                 │
    │        for i in range(0, n-gap):                                │
    │            j = i + gap                                          │
    │            # fill dp[i][j]                                      │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘

    WHY DIAGONAL FILLING?
    ─────────────────────
    dp[i][j] depends on dp[i][k] and dp[k+1][j]  where i <= k < j
    So smaller ranges must be solved BEFORE larger ranges.
    gap=0 (single elements) → gap=1 (pairs) → gap=2 (triples) → ...

    VISUALIZATION (4x4 table, fill order shown by numbers):
    
         j→  0    1    2    3
    i=0      [1]  [2]  [4]  [7]    ← gap 0, 1, 2, 3
    i=1       .   [1]  [3]  [6]    ← gap 0, 1, 2
    i=2       .    .   [1]  [5]    ← gap 0, 1
    i=3       .    .    .   [1]    ← gap 0
    
    Fill diagonals: main diagonal first, then upper diagonals


================================================================================
================================================================================
    PROBLEM 1: MATRIX CHAIN MULTIPLICATION (THE BASE PROBLEM)
    (Google, Amazon, Microsoft)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given dimensions of n matrices in array arr[] of size n+1,
    find MINIMUM number of multiplications to multiply all matrices.

    arr = [40, 20, 30, 10, 30]
    Matrices: A1(40×20), A2(20×30), A3(30×10), A4(10×30)
    Different parenthesizations give different costs. Find minimum.

ONE-LINE TRICK:
    "Try every split point k. Left part cost + right part cost + merge cost.
     Merge cost = arr[i-1] * arr[k] * arr[j]"

DIMENSION FORMULA:
    If array has n elements → we have n-1 matrices
    Matrix Ai has dimensions arr[i-1] × arr[i]
    
    arr = [40, 20, 30, 10, 30]
    A1 → 40×20  (arr[0] × arr[1])
    A2 → 20×30  (arr[1] × arr[2])
    A3 → 30×10  (arr[2] × arr[3])
    A4 → 10×30  (arr[3] × arr[4])

WHY SPLITTING MATTERS:
    ((A1×A2)×A3)×A4 vs A1×((A2×A3)×A4) give VERY different costs!
    
    Example:
    A1(10×30) × A2(30×5) × A3(5×60)
    
    (A1×A2)×A3 = 10*30*5 + 10*5*60 = 1500 + 3000 = 4500
    A1×(A2×A3) = 30*5*60 + 10*30*60 = 9000 + 18000 = 27000
    
    Same matrices, 6x difference! That's why we need DP.

K-LOOP SCHEMES (TWO valid ways to partition):
    Scheme 1: k = i to j-1    → left = (i, k)    right = (k+1, j)
    Scheme 2: k = i+1 to j    → left = (i, k-1)  right = (k, j)
    
    Both are correct! Scheme 1 is more common.

================================================================================
APPROACH 1: RECURSION
================================================================================
"""

def mcm_recursion(arr, i, j):
    """
    Matrix Chain Multiplication — Pure Recursion
    arr = dimensions array, i = start, j = end
    Call: mcm_recursion(arr, 1, n-1) where n = len(arr)
    
    Time: O(2^n) — exponential (trying all partitions)
    Space: O(n) — recursion stack
    """
    # Base: single matrix, no multiplication needed
    if i >= j:
        return 0
    
    mn = float('inf')
    
    # Try every split point k between i and j-1
    for k in range(i, j):
        # Cost = left part + right part + merge cost
        cost = (mcm_recursion(arr, i, k) + 
                mcm_recursion(arr, k + 1, j) + 
                arr[i - 1] * arr[k] * arr[j])
        mn = min(mn, cost)
    
    return mn


# Test Recursion
print("=" * 60)
print("PROBLEM 1: MATRIX CHAIN MULTIPLICATION")
print("=" * 60)
arr = [40, 20, 30, 10, 30]
n = len(arr)
print(f"Recursion: {mcm_recursion(arr, 1, n - 1)}")  # Output: 26000


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down) — Add 3 lines to recursion
================================================================================

    WHAT CHANGES? → i and j  (they define the subproblem range)
    So memo table is: memo[n][n] initialized to -1

    CONVERSION (3 lines added to recursion):
        1. Create memo[n][n] = -1
        2. if memo[i][j] != -1: return memo[i][j]    ← before computing
        3. memo[i][j] = mn; return memo[i][j]         ← before returning
"""

def mcm_memo(arr, i, j, memo):
    """
    MCM with Memoization — O(n^3) time, O(n^2) space
    """
    if i >= j:
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    mn = float('inf')
    
    for k in range(i, j):
        cost = (mcm_memo(arr, i, k, memo) + 
                mcm_memo(arr, k + 1, j, memo) + 
                arr[i - 1] * arr[k] * arr[j])
        mn = min(mn, cost)
    
    memo[i][j] = mn
    return memo[i][j]


# Test Memoization
arr = [40, 20, 30, 10, 30]
n = len(arr)
memo = [[-1] * n for _ in range(n)]
print(f"Memoization: {mcm_memo(arr, 1, n - 1, memo)}")  # Output: 26000


"""
================================================================================
APPROACH 3: BOTTOM-UP (Tabulation) — Diagonal Filling
================================================================================

    KEY INSIGHT: Fill by GAP SIZE, not row by row!
    gap = 0 → single matrix (cost = 0)
    gap = 1 → two matrices
    gap = 2 → three matrices
    ...
    gap = n-2 → all matrices

    dp[i][j] = minimum cost to multiply matrices from i to j
    Answer: dp[1][n-1]
"""

def mcm_bottom_up(arr):
    """
    MCM Bottom-Up — O(n^3) time, O(n^2) space
    INTERVIEW PREFERRED VERSION
    """
    n = len(arr)
    # dp[i][j] = min cost to multiply chain from matrix i to matrix j
    dp = [[0] * n for _ in range(n)]
    
    # gap = 0: single matrix, cost = 0 (already initialized)
    # gap = 1: two matrices, gap = 2: three matrices, ...
    for gap in range(1, n - 1):  # gap from 1 to n-2
        for i in range(1, n - gap):
            j = i + gap
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[1][n - 1]


# Test Bottom-Up
arr = [40, 20, 30, 10, 30]
print(f"Bottom-Up: {mcm_bottom_up(arr)}")  # Output: 26000


"""
DP TABLE TRACE for arr = [40, 20, 30, 10, 30]:

    Matrices: A1(40×20), A2(20×30), A3(30×10), A4(10×30)
    
    dp[i][j] = min cost to multiply matrices i through j

         j→  1       2       3       4
    i=1      0     24000   14000   26000
    i=2      .       0      6000   12000
    i=3      .       .        0     9000
    i=4      .       .        .       0

    Gap=1: dp[1][2] = 40*20*30 = 24000   (A1×A2)
           dp[2][3] = 20*30*10 = 6000    (A2×A3)
           dp[3][4] = 30*10*30 = 9000    (A3×A4)

    Gap=2: dp[1][3] = min(dp[1][1]+dp[2][3]+40*20*10,  = 0+6000+8000 = 14000 ✓
                          dp[1][2]+dp[3][3]+40*30*10)   = 24000+0+12000 = 36000
           dp[2][4] = min(dp[2][2]+dp[3][4]+20*30*30,  = 0+9000+18000 = 27000
                          dp[2][3]+dp[4][4]+20*10*30)   = 6000+0+6000 = 12000 ✓

    Gap=3: dp[1][4] = min(k=1: dp[1][1]+dp[2][4]+40*20*30 = 0+12000+24000 = 36000
                          k=2: dp[1][2]+dp[3][4]+40*30*30 = 24000+9000+36000 = 69000
                          k=3: dp[1][3]+dp[4][4]+40*10*30 = 14000+0+12000 = 26000 ✓)

    Answer: dp[1][4] = 26000

================================================================================
PRINTING THE OPTIMAL PARENTHESIZATION (Follow-up question):
================================================================================

    Track which k gave the minimum at each dp[i][j].
    bracket[i][j] = best k for range [i, j]
    Then recursively print: (left_part)(right_part)
"""

def mcm_print_parenthesization(arr):
    """
    MCM with printing optimal bracket placement
    """
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    bracket = [[0] * n for _ in range(n)]
    
    for gap in range(1, n - 1):
        for i in range(1, n - gap):
            j = i + gap
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    bracket[i][j] = k  # remember best split
    
    def print_brackets(i, j):
        if i == j:
            return f"A{i}"
        k = bracket[i][j]
        left = print_brackets(i, k)
        right = print_brackets(k + 1, j)
        return f"({left} × {right})"
    
    result = print_brackets(1, n - 1)
    return dp[1][n - 1], result


cost, brackets = mcm_print_parenthesization([40, 20, 30, 10, 30])
print(f"Cost: {cost}, Parenthesization: {brackets}")


"""
================================================================================
▶▶▶  WALKTHROUGH — MCM STEP-BY-STEP WITH EXAMPLE  ◀◀◀
================================================================================

    EXAMPLE: arr = [10, 30, 5, 60]
    Matrices: A1(10×30), A2(30×5), A3(5×60)
    Goal: Minimize total scalar multiplications for A1 × A2 × A3
    Call: solve(arr, i=1, j=3)

    RECURSION TREE:
    ┌──────────────────────────────────────────────────────────────────┐
    │                      solve(1, 3)                                │
    │                    ┌──────┴──────┐                              │
    │                  k=1            k=2                              │
    │          (A1 | A2·A3)      (A1·A2 | A3)                        │
    └──────────────────────────────────────────────────────────────────┘

    STEP 1 — k=1: Split as (A1) × (A2 · A3)
    ─────────────────────────────────────────
        left  = solve(1, 1) = 0              ← A1 alone, 0 cost
        right = solve(2, 3)                  ← must solve A2 × A3
        merge = arr[0] * arr[1] * arr[3]     ← multiply results: (10×30) × (30×60)
              = 10 * 30 * 60 = 18000

        ► Solving solve(2, 3) — only k=2 possible:
          left  = solve(2, 2) = 0            ← A2 alone
          right = solve(3, 3) = 0            ← A3 alone
          merge = arr[1] * arr[2] * arr[3]   ← A2(30×5) × A3(5×60)
                = 30 * 5 * 60 = 9000
          return 9000

        Total cost(k=1) = 0 + 9000 + 18000 = 27000
        Physical meaning: A2×A3 costs 9000 → gives 30×60 matrix
                          A1 × (30×60) costs 18000

    STEP 2 — k=2: Split as (A1 · A2) × (A3)
    ─────────────────────────────────────────
        left  = solve(1, 2)                  ← must solve A1 × A2
        right = solve(3, 3) = 0              ← A3 alone
        merge = arr[0] * arr[2] * arr[3]     ← multiply results: (10×5) × (5×60)
              = 10 * 5 * 60 = 3000

        ► Solving solve(1, 2) — only k=1 possible:
          left  = solve(1, 1) = 0
          right = solve(2, 2) = 0
          merge = arr[0] * arr[1] * arr[2]   ← A1(10×30) × A2(30×5)
                = 10 * 30 * 5 = 1500
          return 1500

        Total cost(k=2) = 1500 + 0 + 3000 = 4500
        Physical meaning: A1×A2 costs 1500 → gives 10×5 matrix (SMALL!)
                          (10×5) × A3(5×60) costs 3000

    STEP 3 — Pick minimum:
    ─────────────────────
        min(27000, 4500) = 4500  ✓
        Best parenthesization: (A1 × A2) × A3

    WHY IS k=2 BETTER?
    ┌──────────────────────────────────────────────────────────────────┐
    │  k=1: A2×A3 → big 30×60 matrix → expensive to multiply with A1 │
    │  k=2: A1×A2 → small 10×5 matrix → cheap to multiply with A3    │
    │  Lesson: Intermediate matrix SIZE determines the cost!          │
    └──────────────────────────────────────────────────────────────────┘

    MERGE COST FORMULA — WHY arr[i-1] * arr[k] * arr[j]?
    ────────────────────────────────────────────────────
    After solving left (i..k) → result matrix has dims arr[i-1] × arr[k]
    After solving right (k+1..j) → result matrix has dims arr[k] × arr[j]
    Multiplying these two matrices costs: arr[i-1] × arr[k] × arr[j]

    Example at k=2:
        Left result (A1·A2):  arr[0]×arr[2] = 10×5
        Right result (A3):    arr[2]×arr[3] = 5×60
        Merge cost:           10 × 5 × 60 = 3000  ✓


================================================================================
================================================================================
    PROBLEM 2: PALINDROME PARTITIONING (LC 132 — Hard)
    (Google, Amazon, Microsoft, Meta)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given string s, find the MINIMUM number of CUTS needed so that
    every partition is a palindrome.
    
    "nitin"  → 0 cuts (already palindrome)
    "nitik"  → 2 cuts ("n|iti|k")

WHY IS THIS MCM?
    String from index i to j → try every split point k
    Left part (i to k) + right part (k+1 to j)
    If entire [i,j] is palindrome → 0 cuts needed (base case optimization)

IDENTIFICATION TRICK:
    "minimum cuts" + "string" + "partition into valid parts" → MCM

ONE-LINE TRICK:
    "If s[i..j] is already palindrome → 0 cuts.
     Otherwise try every k, ans = 1 + solve(i,k) + solve(k+1,j)"

CRITICAL OPTIMIZATION (without this → TLE):
    Before trying all k values, check: is s[i..j] already a palindrome?
    If yes → return 0 immediately. This prunes MASSIVE branches.

================================================================================
APPROACH 1: RECURSION
================================================================================
"""

def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def palindrome_partition_recursion(s, i, j):
    """
    Palindrome Partitioning — Pure Recursion
    Returns minimum cuts for s[i..j] to be all palindromes
    
    Time: O(2^n) — exponential
    Space: O(n) — recursion stack
    """
    # Base: single char or empty → already palindrome
    if i >= j:
        return 0
    
    # CRITICAL OPTIMIZATION: if already palindrome, 0 cuts
    if is_palindrome(s, i, j):
        return 0
    
    mn = float('inf')
    
    for k in range(i, j):
        # 1 cut at position k, then solve both halves
        cost = 1 + palindrome_partition_recursion(s, i, k) + palindrome_partition_recursion(s, k + 1, j)
        mn = min(mn, cost)
    
    return mn


# Test
print("\n" + "=" * 60)
print("PROBLEM 2: PALINDROME PARTITIONING")
print("=" * 60)
s = "nitik"
print(f"Recursion '{s}': {palindrome_partition_recursion(s, 0, len(s) - 1)}")  # 2
s = "nitin"
print(f"Recursion '{s}': {palindrome_partition_recursion(s, 0, len(s) - 1)}")  # 0


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================

    Same as recursion + memo[n][n] for (i, j) pairs.
    EXTRA OPTIMIZATION: also memoize is_palindrome checks!
"""

def palindrome_partition_memo(s, i, j, memo):
    """
    Palindrome Partitioning with Memoization
    Time: O(n^3), Space: O(n^2)
    """
    if i >= j:
        return 0
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    if is_palindrome(s, i, j):
        memo[i][j] = 0
        return 0
    
    mn = float('inf')
    
    for k in range(i, j):
        # FURTHER OPTIMIZATION: cache left and right separately
        left = palindrome_partition_memo(s, i, k, memo)
        right = palindrome_partition_memo(s, k + 1, j, memo)
        cost = 1 + left + right
        mn = min(mn, cost)
    
    memo[i][j] = mn
    return memo[i][j]


# Test Memoization
s = "nitik"
n = len(s)
memo = [[-1] * n for _ in range(n)]
print(f"Memo '{s}': {palindrome_partition_memo(s, 0, n - 1, memo)}")  # 2

s = "ababbbabbababa"
n = len(s)
memo = [[-1] * n for _ in range(n)]
print(f"Memo '{s}': {palindrome_partition_memo(s, 0, n - 1, memo)}")  # 3


"""
================================================================================
APPROACH 3: BOTTOM-UP (Optimized O(n^2) approach)
================================================================================

    The O(n^3) MCM-style bottom-up works but there's a cleaner O(n^2) approach.
    
    IDEA: dp[i] = minimum cuts for s[0..i]
    For each position j from 0 to i:
        if s[j..i] is palindrome → dp[i] = min(dp[i], dp[j-1] + 1)
    
    Pre-compute palindrome table: pal[i][j] = is s[i..j] palindrome?
"""

def palindrome_partition_bottom_up(s):
    """
    Palindrome Partitioning — Optimized Bottom-Up O(n^2)
    FAANG INTERVIEW PREFERRED
    """
    n = len(s)
    if n <= 1:
        return 0
    
    # Step 1: Pre-compute palindrome table O(n^2)
    pal = [[False] * n for _ in range(n)]
    for i in range(n):
        pal[i][i] = True  # single char
    for i in range(n - 1):
        pal[i][i + 1] = (s[i] == s[i + 1])  # two chars
    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            pal[i][j] = (s[i] == s[j]) and pal[i + 1][j - 1]
    
    # Step 2: dp[i] = min cuts for s[0..i]
    dp = list(range(n))  # worst case: cut after every char
    
    for i in range(n):
        if pal[0][i]:
            dp[i] = 0  # entire s[0..i] is palindrome
        else:
            for j in range(1, i + 1):
                if pal[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
    
    return dp[n - 1]


# Also the classic MCM-style bottom-up for understanding
def palindrome_partition_bottom_up_mcm_style(s):
    """
    MCM-style diagonal filling — helps understand the pattern
    O(n^3) time, O(n^2) space
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            if is_palindrome(s, i, j):
                dp[i][j] = 0
            else:
                dp[i][j] = float('inf')
                for k in range(i, j):
                    cost = 1 + dp[i][k] + dp[k + 1][j]
                    dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]


# Test Bottom-Up
print(f"Bottom-Up 'nitik': {palindrome_partition_bottom_up('nitik')}")  # 2
print(f"MCM-style 'nitik': {palindrome_partition_bottom_up_mcm_style('nitik')}")  # 2
print(f"Bottom-Up 'nitin': {palindrome_partition_bottom_up('nitin')}")  # 0
print(f"Bottom-Up 'aab': {palindrome_partition_bottom_up('aab')}")  # 1


"""
================================================================================
PALINDROME PARTITIONING — INTERVIEW TRICKS:
================================================================================

    TRICK 1: "Palindrome check → MCM with if-palindrome-return-0 optimization"
    
    TRICK 2: The O(n^2) 1D DP is preferred over O(n^3) MCM-style.
             But EXPLAIN the MCM approach first, then optimize.
    
    TRICK 3: Pre-compute palindrome table to avoid repeated O(n) checks.
             pal[i][j] = (s[i] == s[j]) and pal[i+1][j-1]
    
    TRICK 4: Common follow-up: "Print all partitions" → use backtracking (LC 131)


================================================================================
▶▶▶  WALKTHROUGH — PALINDROME PARTITIONING STEP-BY-STEP  ◀◀◀
================================================================================

    EXAMPLE: s = "aab"
    Goal: Minimum cuts so every part is a palindrome.
    Call: solve(s, i=0, j=2)

    RECURSION TREE:
    ┌──────────────────────────────────────────────────────────────────┐
    │                    solve(0, 2)  ["aab"]                         │
    │                 is_palindrome? NO                               │
    │                  ┌──────┴──────┐                                │
    │                k=0            k=1                                │
    │          ["a"|"ab"]      ["aa"|"b"]                            │
    └──────────────────────────────────────────────────────────────────┘

    STEP 1 — k=0: Cut after index 0 → "a" | "ab"
    ─────────────────────────────────────────────
        cost = 1 + solve(0, 0) + solve(1, 2)

        solve(0, 0) = 0                      ← "a" single char, base case

        ► solve(1, 2): s[1..2] = "ab"
          is_palindrome("ab")? NO
          k=1: 1 + solve(1,1) + solve(2,2)
               = 1 + 0 + 0 = 1              ← cut "a" | "b"
          return 1

        cost(k=0) = 1 + 0 + 1 = 2
        Cuts: "a" | "a" | "b"  → 2 cuts

    STEP 2 — k=1: Cut after index 1 → "aa" | "b"
    ─────────────────────────────────────────────
        cost = 1 + solve(0, 1) + solve(2, 2)

        ► solve(0, 1): s[0..1] = "aa"
          is_palindrome("aa")? YES → return 0  ← CRITICAL OPTIMIZATION!

        solve(2, 2) = 0                      ← "b" single char

        cost(k=1) = 1 + 0 + 0 = 1
        Cuts: "aa" | "b"  → 1 cut

    STEP 3 — Pick minimum:
    ─────────────────────
        min(2, 1) = 1  ✓
        Best: "aa" | "b" → 1 cut

    KEY OBSERVATION:
    ┌──────────────────────────────────────────────────────────────────┐
    │  The "is_palindrome → return 0" check PRUNES the tree hugely.  │
    │  Without it: solve(0,1) would try k=0: 1+solve(0,0)+solve(1,1) │
    │  = 1+0+0 = 1. With the check: we skip that entirely → return 0 │
    │  This optimization turns TLE into AC on large inputs!           │
    └──────────────────────────────────────────────────────────────────┘

    ANOTHER EXAMPLE: s = "nitin"
    solve(0, 4): is_palindrome("nitin")? YES → return 0 immediately!
    No recursion needed at all. That's the power of the palindrome check.

    BOTTOM-UP TRACE for s = "aab" (O(n²) version):
    ─────────────────────────────────────────────────
    Palindrome table:     dp (min cuts for s[0..i]):
        a  a  b                i=0: pal[0][0]=T → dp[0]=0
    a  [T  T  F]              i=1: pal[0][1]=T → dp[1]=0  ("aa" is palindrome)
    a  [.  T  F]              i=2: pal[0][2]=F, check j=1..2:
    b  [.  .  T]                   pal[1][2]=F ("ab"), pal[2][2]=T ("b")
                                   dp[2] = min(dp[2], dp[1]+1) = min(2, 0+1) = 1
    Answer: dp[2] = 1  ✓


================================================================================
================================================================================
    PROBLEM 3: EVALUATE EXPRESSION TO TRUE / BOOLEAN PARENTHESIZATION
    (Google, Amazon, Microsoft — Classic FAANG)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given a boolean expression with symbols T, F and operators &, |, ^
    Count the number of ways to parenthesize it so result is TRUE.

    Example: "T|F&T^F"
    Symbols: T, F, T, F
    Operators: |, &, ^
    How many ways to parenthesize to get TRUE?

WHY IS THIS MCM?
    Expression from index i to j → try every OPERATOR position as k
    Left part gives some True/False counts, right part gives some True/False counts
    Combine using the operator at position k

IDENTIFICATION TRICK:
    "boolean expression" + "parenthesize" + "count ways" → MCM

KEY INSIGHT:
    For each split at operator k:
        - left part can give  leftTrue  ways to be True,  leftFalse  ways to be False
        - right part can give rightTrue ways to be True, rightFalse ways to be False
    
    Then combine based on operator:
        AND (&): True only when both True  → leftTrue * rightTrue
        OR  (|): True when at least one True → total - bothFalse
        XOR (^): True when exactly one True → LT*RF + LF*RT

OPERATOR TRUTH TABLES:
    ┌────────┬─────────────────────────────────────────────────────────┐
    │ AND &  │ TrueWays  = LT * RT                                    │
    │        │ FalseWays = LF*RF + LF*RT + LT*RF                     │
    │        │                                                         │
    │ OR  |  │ TrueWays  = LT*RT + LT*RF + LF*RT                     │
    │        │ FalseWays = LF * RF                                    │
    │        │                                                         │
    │ XOR ^  │ TrueWays  = LT*RF + LF*RT                              │
    │        │ FalseWays = LT*RT + LF*RF                              │
    └────────┴─────────────────────────────────────────────────────────┘

    MEMORY TRICK: 
        AND = both must be true  → LT * RT
        OR  = at least one true  → total - (both false)
        XOR = exactly one true   → LT*RF + LF*RT

NOTE ON INDEXING:
    Expression: T | F & T ^ F
    Indices:    0 1 2 3 4 5 6
    
    Symbols are at EVEN indices: 0, 2, 4, 6
    Operators are at ODD indices: 1, 3, 5
    
    k iterates over OPERATOR positions only (odd indices from i+1 to j-1)

================================================================================
APPROACH 1: RECURSION
================================================================================
"""

def boolean_parenthesization_recursion(expr, i, j, is_true):
    """
    Boolean Parenthesization — Pure Recursion
    expr = expression string like "T|F&T^F"
    i, j = start and end indices (only even indices = symbols)
    is_true = whether we want True or False result
    
    Time: O(4^n) — exponential
    """
    # Base: single symbol
    if i == j:
        if is_true:
            return 1 if expr[i] == 'T' else 0
        else:
            return 1 if expr[i] == 'F' else 0
    
    ans = 0
    
    # k iterates over OPERATOR positions (odd indices between i and j)
    for k in range(i + 1, j, 2):
        # Left part gives true/false counts
        left_true = boolean_parenthesization_recursion(expr, i, k - 1, True)
        left_false = boolean_parenthesization_recursion(expr, i, k - 1, False)
        # Right part gives true/false counts
        right_true = boolean_parenthesization_recursion(expr, k + 1, j, True)
        right_false = boolean_parenthesization_recursion(expr, k + 1, j, False)
        
        op = expr[k]
        
        if op == '&':
            true_ways = left_true * right_true
            false_ways = (left_false * right_false + 
                         left_true * right_false + 
                         left_false * right_true)
        elif op == '|':
            true_ways = (left_true * right_true + 
                        left_true * right_false + 
                        left_false * right_true)
            false_ways = left_false * right_false
        elif op == '^':
            true_ways = (left_true * right_false + 
                        left_false * right_true)
            false_ways = (left_true * right_true + 
                         left_false * right_false)
        
        if is_true:
            ans += true_ways
        else:
            ans += false_ways
    
    return ans


# Test
print("\n" + "=" * 60)
print("PROBLEM 3: BOOLEAN PARENTHESIZATION")
print("=" * 60)
expr = "T|F&T^F"
n = len(expr)
print(f"Recursion '{expr}' → True ways: {boolean_parenthesization_recursion(expr, 0, n - 1, True)}")


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================

    WHAT CHANGES? → i, j, and is_true (3 variables!)
    Memo key: (i, j, is_true) or use memo[i][j][2]
    
    TRICK: Use a dictionary for clean code since is_true is boolean
"""

def boolean_parenthesization_memo(expr, i, j, is_true, memo):
    """
    Boolean Parenthesization with Memoization
    Time: O(n^3), Space: O(n^2)
    """
    key = (i, j, is_true)
    
    if key in memo:
        return memo[key]
    
    if i == j:
        if is_true:
            return 1 if expr[i] == 'T' else 0
        else:
            return 1 if expr[i] == 'F' else 0
    
    ans = 0
    
    for k in range(i + 1, j, 2):  # operators at odd positions
        lt = boolean_parenthesization_memo(expr, i, k - 1, True, memo)
        lf = boolean_parenthesization_memo(expr, i, k - 1, False, memo)
        rt = boolean_parenthesization_memo(expr, k + 1, j, True, memo)
        rf = boolean_parenthesization_memo(expr, k + 1, j, False, memo)
        
        op = expr[k]
        if op == '&':
            true_ways = lt * rt
            false_ways = lf * rf + lt * rf + lf * rt
        elif op == '|':
            true_ways = lt * rt + lt * rf + lf * rt
            false_ways = lf * rf
        elif op == '^':
            true_ways = lt * rf + lf * rt
            false_ways = lt * rt + lf * rf
        
        ans += true_ways if is_true else false_ways
    
    memo[key] = ans
    return ans


# Test Memo
expr = "T|F&T^F"
n = len(expr)
memo = {}
print(f"Memo '{expr}' → True ways: {boolean_parenthesization_memo(expr, 0, n - 1, True, memo)}")

expr = "T^F|F"
n = len(expr)
memo = {}
print(f"Memo '{expr}' → True ways: {boolean_parenthesization_memo(expr, 0, n - 1, True, memo)}")  # 2


"""
================================================================================
APPROACH 3: BOTTOM-UP (Tabulation)
================================================================================

    Use TWO tables: dpT[i][j] = ways to get True, dpF[i][j] = ways to get False
    Fill diagonally by gap size.
"""

def boolean_parenthesization_bottom_up(expr):
    """
    Boolean Parenthesization — Bottom-Up
    Time: O(n^3), Space: O(n^2)
    """
    # Extract symbols and operators
    symbols = [expr[i] for i in range(0, len(expr), 2)]
    operators = [expr[i] for i in range(1, len(expr), 2)]
    
    n = len(symbols)
    dpT = [[0] * n for _ in range(n)]  # ways to get True
    dpF = [[0] * n for _ in range(n)]  # ways to get False
    
    # Base: single symbols
    for i in range(n):
        dpT[i][i] = 1 if symbols[i] == 'T' else 0
        dpF[i][i] = 1 if symbols[i] == 'F' else 0
    
    # Fill by gap (diagonal)
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            dpT[i][j] = 0
            dpF[i][j] = 0
            
            for k in range(i, j):  # k is the operator index
                lt, lf = dpT[i][k], dpF[i][k]
                rt, rf = dpT[k + 1][j], dpF[k + 1][j]
                
                op = operators[k]
                if op == '&':
                    dpT[i][j] += lt * rt
                    dpF[i][j] += lf * rf + lt * rf + lf * rt
                elif op == '|':
                    dpT[i][j] += lt * rt + lt * rf + lf * rt
                    dpF[i][j] += lf * rf
                elif op == '^':
                    dpT[i][j] += lt * rf + lf * rt
                    dpF[i][j] += lt * rt + lf * rf
    
    return dpT[0][n - 1]


# Test
expr = "T|F&T^F"
print(f"Bottom-Up '{expr}' → True ways: {boolean_parenthesization_bottom_up(expr)}")
expr = "T^F|F"
print(f"Bottom-Up '{expr}' → True ways: {boolean_parenthesization_bottom_up(expr)}")  # 2


"""
================================================================================
▶▶▶  WALKTHROUGH — BOOLEAN PARENTHESIZATION STEP-BY-STEP  ◀◀◀
================================================================================

    EXAMPLE: expr = "T^F|F"
    Symbols:   T(pos 0), F(pos 2), F(pos 4)
    Operators: ^(pos 1), |(pos 3)
    Goal: How many ways to parenthesize so result = TRUE?

    CALL: solve(0, 4, is_true=True)

    RECURSION TREE:
    ┌──────────────────────────────────────────────────────────────────┐
    │                  solve(0, 4, True)                              │
    │                ┌───────┴───────┐                                │
    │          k=1 (op: ^)      k=3 (op: |)                          │
    │       [T] ^ [F|F]        [T^F] | [F]                           │
    └──────────────────────────────────────────────────────────────────┘

    STEP 1 — k=1 (operator ^): Split as [T] ^ [F|F]
    ─────────────────────────────────────────────────
        LEFT = solve(0, 0):   symbol is T
            left_true  = 1   (T is True)
            left_false = 0

        RIGHT = solve(2, 4):  expression is "F|F"
            Only operator at k=3 (|):
            lt=0(F), lf=1, rt=0(F), rf=1
            OR truth table:  true_ways = lt*rt + lt*rf + lf*rt
                                       = 0*0  + 0*1  + 1*0 = 0
            right_true  = 0
            right_false = 1   (F|F = F, only 1 way)

        XOR truth table:  true_ways = LT*RF + LF*RT
                                    = 1*1  + 0*0  = 1
        k=1 contributes 1 way
        Meaning: T ^ (F|F) = T ^ F = True  ✓

    STEP 2 — k=3 (operator |): Split as [T^F] | [F]
    ─────────────────────────────────────────────────
        LEFT = solve(0, 2):  expression is "T^F"
            Only operator at k=1 (^):
            lt=1(T), lf=0, rt=0(F), rf=1
            XOR: true_ways = lt*rf + lf*rt = 1*1 + 0*0 = 1
            left_true  = 1    (T^F = True)
            left_false = 0

        RIGHT = solve(4, 4): symbol is F
            right_true  = 0
            right_false = 1

        OR truth table:  true_ways = LT*RT + LT*RF + LF*RT
                                   = 1*0  + 1*1  + 0*0  = 1
        k=3 contributes 1 way
        Meaning: (T^F) | F = T | F = True  ✓

    STEP 3 — Total:
    ─────────────────
        ans = 1 + 1 = 2  ✓
        The 2 ways:
          Way 1: T ^ (F|F) = T ^ F = True
          Way 2: (T^F) | F = T | F = True

    WHY WE TRACK BOTH TRUE AND FALSE COUNTS:
    ┌──────────────────────────────────────────────────────────────────┐
    │  At each split, we need ALL 4 values: LT, LF, RT, RF           │
    │  Because operators combine them differently:                    │
    │    XOR needs LT*RF (left true, right false) for a true result  │
    │    AND needs LT*RT (both true) for a true result               │
    │    OR  needs LF*RF (both false) for a false result             │
    │  You can't compute true_ways without knowing false_ways too!   │
    └──────────────────────────────────────────────────────────────────┘


================================================================================
================================================================================
    PROBLEM 4: SCRAMBLE STRING (LC 87 — Hard)
    (Google, Amazon, Microsoft)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given two strings s1 and s2 of same length, determine if s2 is a 
    "scrambled" version of s1.
    
    Scramble = recursively split string into two parts, optionally swap them,
    then recursively scramble each part.

WHY IS THIS MCM?
    String of length n → try every split point k (1 to n-1)
    Two possibilities at each split:
        1. NO SWAP:  left1 matches left2  AND right1 matches right2
        2. SWAP:     left1 matches right2 AND right1 matches left2

IDENTIFICATION TRICK:
    "Two strings" + "split recursively" + "swap or not" → MCM variant

KEY INSIGHT (TWO CASES AT EACH SPLIT k):
    
    Case 1 — NO SWAP:
        s1[0..k-1] scrambles to s2[0..k-1]     (left↔left)
        s1[k..n-1] scrambles to s2[k..n-1]     (right↔right)
    
    Case 2 — SWAP:
        s1[0..k-1] scrambles to s2[n-k..n-1]   (left↔right)
        s1[k..n-1] scrambles to s2[0..n-k-1]   (right↔left)

EARLY TERMINATION TRICKS (saves MASSIVE time):
    1. If s1 == s2 → return True immediately
    2. If sorted(s1) != sorted(s2) → return False immediately
       (if characters don't match, impossible to scramble)
    3. If len(s1) <= 1 → return s1 == s2

================================================================================
APPROACH 1: RECURSION
================================================================================
"""

def scramble_string_recursion(s1, s2):
    """
    Scramble String — Pure Recursion
    Time: O(4^n) worst case — exponential
    """
    if len(s1) != len(s2):
        return False
    
    if s1 == s2:
        return True
    
    if sorted(s1) != sorted(s2):
        return False
    
    n = len(s1)
    
    for k in range(1, n):  # split at position k
        # Case 1: No swap — left matches left, right matches right
        no_swap = (scramble_string_recursion(s1[:k], s2[:k]) and 
                   scramble_string_recursion(s1[k:], s2[k:]))
        
        # Case 2: Swap — left matches right end, right matches left end
        swap = (scramble_string_recursion(s1[:k], s2[n - k:]) and 
                scramble_string_recursion(s1[k:], s2[:n - k]))
        
        if no_swap or swap:
            return True
    
    return False


# Test
print("\n" + "=" * 60)
print("PROBLEM 4: SCRAMBLE STRING")
print("=" * 60)
print(f"Recursion ('great','rgeat'): {scramble_string_recursion('great', 'rgeat')}")  # True
print(f"Recursion ('abcde','caebd'): {scramble_string_recursion('abcde', 'caebd')}")  # False


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================

    WHAT CHANGES? → s1 and s2 (the substrings we're comparing)
    Memo key: (s1, s2) — use the strings themselves as keys
"""

def scramble_string_memo(s1, s2, memo):
    """
    Scramble String with Memoization
    Time: O(n^4), Space: O(n^4)
    """
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    
    if len(s1) != len(s2):
        return False
    
    if s1 == s2:
        return True
    
    if sorted(s1) != sorted(s2):
        memo[(s1, s2)] = False
        return False
    
    n = len(s1)
    
    for k in range(1, n):
        no_swap = (scramble_string_memo(s1[:k], s2[:k], memo) and 
                   scramble_string_memo(s1[k:], s2[k:], memo))
        
        swap = (scramble_string_memo(s1[:k], s2[n - k:], memo) and 
                scramble_string_memo(s1[k:], s2[:n - k], memo))
        
        if no_swap or swap:
            memo[(s1, s2)] = True
            return True
    
    memo[(s1, s2)] = False
    return False


# Test Memo
memo = {}
print(f"Memo ('great','rgeat'): {scramble_string_memo('great', 'rgeat', memo)}")  # True
memo = {}
print(f"Memo ('abcde','caebd'): {scramble_string_memo('abcde', 'caebd', memo)}")  # False


"""
================================================================================
APPROACH 3: BOTTOM-UP (3D DP)
================================================================================

    dp[length][i][j] = can s1[i..i+length-1] scramble to s2[j..j+length-1]?
    
    Build from length=1 up to length=n
    For each length, try all split points k (1 to length-1)
"""

def scramble_string_bottom_up(s1, s2):
    """
    Scramble String — Bottom-Up 3D DP
    Time: O(n^4), Space: O(n^3)
    INTERVIEW PREFERRED
    """
    n = len(s1)
    if n != len(s2):
        return False
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False
    
    # dp[length][i][j] = can s1[i..i+len-1] scramble to s2[j..j+len-1]?
    dp = [[[False] * n for _ in range(n)] for _ in range(n + 1)]
    
    # Base: length = 1, single characters
    for i in range(n):
        for j in range(n):
            dp[1][i][j] = (s1[i] == s2[j])
    
    # Fill for length 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            for j in range(n - length + 1):
                for k in range(1, length):  # split point
                    # No swap
                    if dp[k][i][j] and dp[length - k][i + k][j + k]:
                        dp[length][i][j] = True
                        break
                    # Swap
                    if dp[k][i][j + length - k] and dp[length - k][i + k][j]:
                        dp[length][i][j] = True
                        break
    
    return dp[n][0][0]


# Test Bottom-Up
print(f"Bottom-Up ('great','rgeat'): {scramble_string_bottom_up('great', 'rgeat')}")  # True
print(f"Bottom-Up ('abcde','caebd'): {scramble_string_bottom_up('abcde', 'caebd')}")  # False


"""
================================================================================
▶▶▶  WALKTHROUGH — SCRAMBLE STRING STEP-BY-STEP  ◀◀◀
================================================================================

    EXAMPLE: s1 = "great", s2 = "rgeat"
    Goal: Is s2 a scrambled version of s1?

    HOW SCRAMBLING WORKS (visual):
    ┌──────────────────────────────────────────────────────────────────┐
    │     "great"                                                     │
    │     ┌──┴───┐                                                    │
    │    "gr"  "eat"    ← split at k=2                               │
    │    ┌┴┐                                                          │
    │   "g""r"          ← split at k=1                               │
    │    SWAP!          ← swap "g" and "r"                           │
    │   "r""g"                                                        │
    │    └┬┘                                                          │
    │    "rg"  "eat"    ← recombine                                  │
    │     └──┬───┘                                                    │
    │     "rgeat"       ← result!                                    │
    └──────────────────────────────────────────────────────────────────┘

    CALL: scramble("great", "rgeat")

    s1 ≠ s2, sorted(s1) == sorted(s2) ✓, proceed to try splits.

    k=1: NO SWAP: scramble("g","r") → sorted differ → False
         SWAP:    scramble("g","t") → sorted differ → False
         → False

    k=2: NO SWAP: scramble("gr","rg") AND scramble("eat","eat")
    ──────────────────────────────────────────────────────────
         ► scramble("eat","eat"): s1 == s2 → True  ✓

         ► scramble("gr","rg"): s1 ≠ s2, sorted match ✓
           k=1: NO SWAP: scramble("g","r") → False
                SWAP:    scramble("g","g") → True  ✓
                         scramble("r","r") → True  ✓
                True AND True → True!
           → True  ✓

         True AND True → True!  ✓  (we can stop here)

    ANSWER: True
    Split "great" at k=2 → "gr" + "eat"
    Swap "gr" → "rg" (by splitting "gr" at k=1 and swapping)
    Result: "rg" + "eat" = "rgeat"  ✓

    THE TWO CASES AT EACH SPLIT (visual):
    ┌──────────────────────────────────────────────────────────────────┐
    │  s1 = [  LEFT1  |  RIGHT1  ]     (split at position k)         │
    │                                                                 │
    │  NO SWAP:  s2 = [ LEFT2 | RIGHT2 ]                             │
    │            LEFT1↔LEFT2  and  RIGHT1↔RIGHT2                     │
    │            scramble(s1[:k], s2[:k]) AND scramble(s1[k:], s2[k:])│
    │                                                                 │
    │  SWAP:     s2 = [ RIGHT2 | LEFT2 ]                             │
    │            LEFT1↔RIGHT_END  and  RIGHT1↔LEFT_START             │
    │            scramble(s1[:k], s2[n-k:]) AND scramble(s1[k:],s2[:n-k])│
    └──────────────────────────────────────────────────────────────────┘

    COUNTER-EXAMPLE: s1 = "abcde", s2 = "caebd" → False
    sorted(s1) = "abcde" == sorted(s2) ✓, but NO split sequence works.
    All k values for all sub-problems eventually return False.


================================================================================
================================================================================
    PROBLEM 5: EGG DROPPING PROBLEM (LC 887 — Hard)
    (Google, Amazon, Goldman Sachs, Microsoft)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given e eggs and f floors, find the MINIMUM number of TRIALS
    needed to find the CRITICAL FLOOR (floor from which egg breaks)
    in the WORST CASE.

WHY IS THIS MCM?
    Range of floors [1..f] → try dropping egg from every floor k
    If egg BREAKS at k    → search below: solve(e-1, k-1) (one less egg, lower floors)
    If egg SURVIVES at k  → search above: solve(e, f-k)   (same eggs, upper floors)
    
    Worst case → take MAX of break/survive (pessimistic)
    Over all k → take MIN (optimal strategy)

IDENTIFICATION TRICK:
    "minimum trials" + "worst case" + "two outcomes at each step" → MCM variant

ONE-LINE TRICK:
    "Drop from floor k. Worst case = 1 + max(breaks, survives).
     Best strategy = min over all k."

KEY FORMULA:
    solve(e, f) = 1 + min over k from 1..f of:
                      max(solve(e-1, k-1),   ← egg breaks (go down)
                          solve(e, f-k))      ← egg survives (go up)

BASE CASES:
    e == 1 → must try every floor linearly → return f
    f == 0 → no floors to check → return 0
    f == 1 → only 1 floor → return 1

================================================================================
APPROACH 1: RECURSION
================================================================================
"""

def egg_drop_recursion(e, f):
    """
    Egg Dropping — Pure Recursion
    e = eggs, f = floors
    Returns minimum trials in worst case
    
    Time: O(2^f) — exponential
    Space: O(f) — recursion stack
    """
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f  # linear search
    
    mn = float('inf')
    
    for k in range(1, f + 1):  # try dropping from floor k
        worst = 1 + max(egg_drop_recursion(e - 1, k - 1),    # breaks → go down
                        egg_drop_recursion(e, f - k))          # survives → go up
        mn = min(mn, worst)
    
    return mn


# Test (small input — recursion is VERY slow)
print("\n" + "=" * 60)
print("PROBLEM 5: EGG DROPPING PROBLEM")
print("=" * 60)
print(f"Recursion (2 eggs, 10 floors): {egg_drop_recursion(2, 10)}")  # 4


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================

    WHAT CHANGES? → e (eggs) and f (floors)
    Memo: dp[e+1][f+1] initialized to -1
"""

def egg_drop_memo(e, f, memo):
    """
    Egg Dropping with Memoization
    Time: O(e * f^2), Space: O(e * f)
    """
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f
    
    if memo[e][f] != -1:
        return memo[e][f]
    
    mn = float('inf')
    
    for k in range(1, f + 1):
        worst = 1 + max(egg_drop_memo(e - 1, k - 1, memo),
                        egg_drop_memo(e, f - k, memo))
        mn = min(mn, worst)
    
    memo[e][f] = mn
    return memo[e][f]


# Test Memo
e, f = 2, 36
memo = [[-1] * (f + 1) for _ in range(e + 1)]
print(f"Memo ({e} eggs, {f} floors): {egg_drop_memo(e, f, memo)}")  # 8


"""
================================================================================
APPROACH 2.5: MEMOIZATION + BINARY SEARCH OPTIMIZATION (O(e*f*log f))
================================================================================

    KEY OBSERVATION for the k-loop:
        As k increases from 1 to f:
            solve(e-1, k-1) INCREASES (more floors below, egg breaks)
            solve(e, f-k) DECREASES   (fewer floors above, egg survives)
        
        The max(break, survive) forms a V-shape or crossover point.
        → Use BINARY SEARCH to find optimal k!
        
    This reduces O(e * f^2) → O(e * f * log f)
"""

def egg_drop_memo_binary(e, f, memo):
    """
    Egg Drop with Memo + Binary Search — FAANG OPTIMAL
    Time: O(e * f * log f), Space: O(e * f)
    """
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f
    
    if memo[e][f] != -1:
        return memo[e][f]
    
    mn = float('inf')
    lo, hi = 1, f
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        breaks = egg_drop_memo_binary(e - 1, mid - 1, memo)     # egg breaks
        survives = egg_drop_memo_binary(e, f - mid, memo)        # egg survives
        
        worst = 1 + max(breaks, survives)
        mn = min(mn, worst)
        
        if breaks < survives:
            lo = mid + 1  # go higher (breaks side is smaller)
        elif breaks > survives:
            hi = mid - 1  # go lower (survives side is smaller)
        else:
            break  # perfect crossover found
    
    memo[e][f] = mn
    return memo[e][f]


# Test Binary Search version
e, f = 2, 100
memo = [[-1] * (f + 1) for _ in range(e + 1)]
print(f"Memo+BinSearch ({e} eggs, {f} floors): {egg_drop_memo_binary(e, f, memo)}")  # 14


"""
================================================================================
APPROACH 3: BOTTOM-UP 
================================================================================
"""

def egg_drop_bottom_up(e, f):
    """
    Egg Drop — Bottom-Up DP
    Time: O(e * f^2), Space: O(e * f)
    """
    # dp[i][j] = min trials with i eggs and j floors
    dp = [[0] * (f + 1) for _ in range(e + 1)]
    
    # Base: 1 egg → linear search
    for j in range(f + 1):
        dp[1][j] = j
    
    # Base: 0 or 1 floor
    for i in range(e + 1):
        dp[i][0] = 0
        if f >= 1:
            dp[i][1] = 1
    
    # Fill table
    for i in range(2, e + 1):
        for j in range(2, f + 1):
            dp[i][j] = float('inf')
            for k in range(1, j + 1):
                worst = 1 + max(dp[i - 1][k - 1], dp[i][j - k])
                dp[i][j] = min(dp[i][j], worst)
    
    return dp[e][f]


"""
APPROACH 3.5: BOTTOM-UP INVERTED (OPTIMAL O(e * log f))
================================================================================

    INVERTED THINKING: Instead of "given e eggs and f floors, find min trials",
    ask "given e eggs and t trials, what's the MAX floors we can check?"
    
    dp[t][e] = max floors checkable with t trials and e eggs
    
    dp[t][e] = dp[t-1][e-1] + 1 + dp[t-1][e]
               (breaks)     (this floor) (survives)
    
    Answer: smallest t where dp[t][e] >= f
    
    This runs in O(e * log f) — the FASTEST approach!
"""

def egg_drop_optimal(e, f):
    """
    Egg Drop — Inverted DP (FASTEST)
    Time: O(e * log f), Space: O(e)
    THE ULTIMATE FAANG VERSION
    """
    # dp[i] = max floors with current trial count and i eggs
    dp = [0] * (e + 1)
    trials = 0
    
    while dp[e] < f:
        trials += 1
        # Update right to left to use previous trial's values
        for i in range(e, 0, -1):
            dp[i] = dp[i - 1] + 1 + dp[i]
    
    return trials


# Test all versions
print(f"Bottom-Up (2 eggs, 36 floors): {egg_drop_bottom_up(2, 36)}")  # 8
print(f"Optimal (2 eggs, 100 floors): {egg_drop_optimal(2, 100)}")    # 14
print(f"Optimal (3 eggs, 100 floors): {egg_drop_optimal(3, 100)}")    # 9
print(f"Optimal (2 eggs, 36 floors): {egg_drop_optimal(2, 36)}")      # 8


"""
================================================================================
EGG DROP — INTERVIEW TRICKS:
================================================================================

    TRICK 1: Start with O(e*f^2) recursive → memo → mention binary search O(e*f*logf)
    
    TRICK 2: If interviewer asks for OPTIMAL → inverted DP O(e*logf)
             "Instead of finding min trials, find max floors given trials"
    
    TRICK 3: With 1 egg → always linear search (try floor 1, then 2, ...)
             With infinite eggs → binary search (log f trials)
             With 2 eggs → optimal is roughly √f trials
    
    TRICK 4: The binary search optimization works because:
             - As k increases, break_cost increases, survive_cost decreases
             - max(break, survive) has a single crossover point
             - Binary search finds that crossover


================================================================================
▶▶▶  WALKTHROUGH — EGG DROPPING STEP-BY-STEP  ◀◀◀
================================================================================

    EXAMPLE: 2 eggs, 6 floors
    Goal: Minimum trials in the WORST CASE to find the critical floor.

    BUILDING THE DP TABLE:
    ─────────────────────
    Base cases:
        dp[1][f] = f  (1 egg → must try every floor linearly)
        dp[e][0] = 0  (0 floors → no trials needed)
        dp[e][1] = 1  (1 floor → just try it)

              floors →  0   1   2   3   4   5   6
    1 egg (dp[1]):      [0] [1] [2] [3] [4] [5] [6]   ← linear search
    2 eggs (dp[2]):     [0] [1] [?] [?] [?] [?] [?]   ← need to fill

    FILLING dp[2][2]  (2 eggs, 2 floors):
    ─────────────────────────────────────
    Try dropping from each floor k:
        k=1: 1 + max(dp[1][0], dp[2][1]) = 1 + max(0, 1) = 2
             ↑ egg breaks → 1 egg, 0 floors below
                            ↑ egg survives → 2 eggs, 1 floor above
        k=2: 1 + max(dp[1][1], dp[2][0]) = 1 + max(1, 0) = 2
    dp[2][2] = min(2, 2) = 2

    FILLING dp[2][3]  (2 eggs, 3 floors):
    ─────────────────────────────────────
        k=1: 1 + max(dp[1][0], dp[2][2]) = 1 + max(0, 2) = 3
        k=2: 1 + max(dp[1][1], dp[2][1]) = 1 + max(1, 1) = 2  ✓
        k=3: 1 + max(dp[1][2], dp[2][0]) = 1 + max(2, 0) = 3
    dp[2][3] = min(3, 2, 3) = 2
    Strategy: Start at floor 2.

    FILLING dp[2][4]  (2 eggs, 4 floors):
    ─────────────────────────────────────
        k=1: 1 + max(0, dp[2][3]) = 1 + 2 = 3
        k=2: 1 + max(1, dp[2][2]) = 1 + 2 = 3
        k=3: 1 + max(2, dp[2][1]) = 1 + 2 = 3
        k=4: 1 + max(3, 0) = 4
    dp[2][4] = 3

    FILLING dp[2][5]  (2 eggs, 5 floors):
    ─────────────────────────────────────
        k=1: 1 + max(0, dp[2][4]) = 1 + 3 = 4
        k=2: 1 + max(1, dp[2][3]) = 1 + 2 = 3  ✓
        k=3: 1 + max(2, dp[2][2]) = 1 + 2 = 3  ✓
        k=4: 1 + max(3, dp[2][1]) = 1 + 3 = 4
        k=5: 1 + max(4, 0) = 5
    dp[2][5] = 3

    FILLING dp[2][6]  (2 eggs, 6 floors):
    ─────────────────────────────────────
        k=1: 1 + max(0, dp[2][5]) = 1 + 3 = 4
        k=2: 1 + max(1, dp[2][4]) = 1 + 3 = 4
        k=3: 1 + max(2, dp[2][3]) = 1 + 2 = 3  ✓ (BEST!)
        k=4: 1 + max(3, dp[2][2]) = 1 + 3 = 4
        k=5: 1 + max(4, dp[2][1]) = 1 + 4 = 5
        k=6: 1 + max(5, 0) = 6
    dp[2][6] = 3  ✓

    FINAL TABLE:
              floors →  0   1   2   3   4   5   6
    1 egg (dp[1]):      [0] [1] [2] [3] [4] [5] [6]
    2 eggs (dp[2]):     [0] [1] [2] [2] [3] [3] [3]

    ANSWER: dp[2][6] = 3 trials

    OPTIMAL STRATEGY (for 2 eggs, 6 floors):
    ┌──────────────────────────────────────────────────────────────────┐
    │  Trial 1: Drop from floor 3                                    │
    │    If BREAKS → egg1 gone, search floors 1-2 with 1 egg         │
    │              → at most 2 more trials (linear: floor 1, floor 2)│
    │              → total: 1 + 2 = 3 trials                         │
    │    If SURVIVES → 2 eggs left, search floors 4-6 (3 floors)     │
    │              → dp[2][3] = 2 more trials                        │
    │              → total: 1 + 2 = 3 trials                         │
    │  Worst case: max(3, 3) = 3  ✓                                  │
    └──────────────────────────────────────────────────────────────────┘

    WHY min(max(break, survive)) — THE INTUITION:
    ─ max() because we plan for the WORST case (we don't know the answer)
    ─ min() because we pick the BEST strategy (optimal floor to drop from)


================================================================================
================================================================================
    PROBLEM 6: BURST BALLOONS (LC 312 — Hard)
    (Google, Amazon, Goldman Sachs, Meta)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given n balloons with values, burst all to maximize total coins.
    When you burst balloon i, you get: nums[left] * nums[i] * nums[right]
    where left and right are adjacent non-burst balloons.
    
    After bursting, left and right become adjacent.

WHY IS THIS MCM?
    Range [i..j] → try bursting every balloon k LAST in that range
    If k is burst LAST in [i..j]:
        - Left part [i..k-1] was already burst (cost = solve(i, k-1))
        - Right part [k+1..j] was already burst (cost = solve(k+1, j))
        - Bursting k last means its neighbors are now i-1 and j+1
        - Cost of bursting k = nums[i-1] * nums[k] * nums[j+1]

CRITICAL INSIGHT (THIS IS THE HARD PART):
    In normal MCM, we think "which k to split FIRST?"
    In Burst Balloons, think "which balloon to burst LAST?"
    
    WHY? When k is burst LAST in range [i..j], we KNOW its neighbors
    are the boundaries: nums[i-1] and nums[j+1] (everything else is gone).
    
    If we thought about "burst first" → neighbors keep changing → impossible!

TRICK:
    Add dummy balloons with value 1 at both ends:
    nums = [1] + nums + [1]
    Now solve for range [1, n] (excluding the dummies)

================================================================================
APPROACH 1: RECURSION
================================================================================
"""

def burst_balloons_recursion(nums):
    """
    Burst Balloons — Pure Recursion
    Time: O(2^n), Space: O(n)
    """
    nums = [1] + nums + [1]  # add dummy boundaries
    n = len(nums)
    
    def solve(i, j):
        if i > j:
            return 0
        
        mx = 0
        for k in range(i, j + 1):  # k is the LAST balloon to burst in [i,j]
            cost = (solve(i, k - 1) + 
                    solve(k + 1, j) + 
                    nums[i - 1] * nums[k] * nums[j + 1])
            mx = max(mx, cost)
        
        return mx
    
    return solve(1, n - 2)


# Test
print("\n" + "=" * 60)
print("PROBLEM 6: BURST BALLOONS")
print("=" * 60)
nums = [3, 1, 5, 8]
print(f"Recursion {nums}: {burst_balloons_recursion(nums)}")  # 167


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================
"""

def burst_balloons_memo(nums):
    """
    Burst Balloons with Memoization
    Time: O(n^3), Space: O(n^2)
    """
    nums = [1] + nums + [1]
    n = len(nums)
    memo = {}
    
    def solve(i, j):
        if i > j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        
        mx = 0
        for k in range(i, j + 1):
            cost = (solve(i, k - 1) + 
                    solve(k + 1, j) + 
                    nums[i - 1] * nums[k] * nums[j + 1])
            mx = max(mx, cost)
        
        memo[(i, j)] = mx
        return mx
    
    return solve(1, n - 2)


# Test Memo
nums = [3, 1, 5, 8]
print(f"Memo {nums}: {burst_balloons_memo(nums)}")  # 167


"""
================================================================================
APPROACH 3: BOTTOM-UP (Diagonal Filling)
================================================================================

    dp[i][j] = max coins from bursting all balloons in [i, j]
    Fill by gap size (just like MCM!)
    Answer: dp[1][n-2] (original range, excluding dummies)
"""

def burst_balloons_bottom_up(nums):
    """
    Burst Balloons — Bottom-Up DP
    Time: O(n^3), Space: O(n^2)
    INTERVIEW PREFERRED
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    
    # gap = 0: single balloons, gap = 1: pairs, etc.
    for gap in range(0, n - 2):  # gap from 0 to n-3
        for i in range(1, n - 1 - gap):
            j = i + gap
            for k in range(i, j + 1):  # k = last to burst
                cost = (dp[i][k - 1] + 
                        dp[k + 1][j] + 
                        nums[i - 1] * nums[k] * nums[j + 1])
                dp[i][j] = max(dp[i][j], cost)
    
    return dp[1][n - 2]


# Test Bottom-Up
nums = [3, 1, 5, 8]
print(f"Bottom-Up {nums}: {burst_balloons_bottom_up(nums)}")  # 167


"""
DP TABLE TRACE for nums = [3, 1, 5, 8] → padded: [1, 3, 1, 5, 8, 1]

    dp[i][j] = max coins bursting balloons i to j (k = LAST burst)

         j→  1     2     3     4
    i=1      3    30    159   167
    i=2      .     15    135   159
    i=3      .      .     40   48
    i=4      .      .      .    40

    Gap=0 (single): dp[1][1]=1*3*1=3, dp[2][2]=3*1*5=15,
                    dp[3][3]=1*5*8=40, dp[4][4]=5*8*1=40
    
    Gap=1: dp[1][2] = max(k=1: dp[1][0]+dp[2][2]+1*3*5 = 0+15+15 = 30,
                          k=2: dp[1][1]+dp[3][2]+1*1*5 = 3+0+5 = 8)
                     = 30
    
    Answer: dp[1][4] = 167


================================================================================
BURST BALLOONS — INTERVIEW TRICKS:
================================================================================

    TRICK 1: Think "LAST to burst" not "FIRST to burst"
             This fixes the neighbor dependency problem.
    
    TRICK 2: Add dummy 1s at both ends: nums = [1] + nums + [1]
             Now boundaries are always well-defined.
    
    TRICK 3: This is MCM with MAX instead of MIN, and k is within [i,j] not [i,j-1]
    
    TRICK 4: Cost formula: nums[i-1] * nums[k] * nums[j+1]
             The boundaries i-1 and j+1 (NOT i and j!) because k is LAST.


================================================================================
▶▶▶  WALKTHROUGH — BURST BALLOONS STEP-BY-STEP  ◀◀◀
================================================================================

    EXAMPLE: nums = [3, 1, 5]
    Padded: [1, 3, 1, 5, 1]   (add 1 at both ends)
    Indices: 0  1  2  3  4
    Goal: Burst all balloons (indices 1-3) to MAXIMIZE coins.
    Call: solve(1, 3)

    KEY INSIGHT — "LAST TO BURST" THINKING:
    ┌──────────────────────────────────────────────────────────────────┐
    │  If we think "burst first" → neighbors change unpredictably.   │
    │  If we think "burst LAST" → when balloon k is the last one     │
    │  in range [i,j], everything else is already gone!              │
    │  So its neighbors are the BOUNDARIES: nums[i-1] and nums[j+1] │
    └──────────────────────────────────────────────────────────────────┘

    RECURSION TREE:
    ┌──────────────────────────────────────────────────────────────────┐
    │                    solve(1, 3)                                  │
    │              ┌────────┼────────┐                                │
    │            k=1       k=2      k=3                               │
    │          (3 last)  (1 last)  (5 last)                          │
    └──────────────────────────────────────────────────────────────────┘

    STEP 1 — k=1: Balloon 3 is LAST to burst in [1,3]
    ─────────────────────────────────────────────────
        left  = solve(1, 0) = 0               ← empty range
        right = solve(2, 3)                   ← burst balloons 1,5 first
        cost of bursting 3 LAST: nums[0]*nums[1]*nums[4] = 1*3*1 = 3

        ► solve(2, 3):  balloons with values [1, 5]
          k=2 (1 is last): solve(2,1)=0, solve(3,3), cost=nums[1]*nums[2]*nums[4]=3*1*1=3
            solve(3,3): k=3: cost=nums[2]*nums[3]*nums[4]=1*5*1=5, return 5
            total = 0 + 5 + 3 = 8
          k=3 (5 is last): solve(2,2), solve(4,3)=0, cost=nums[1]*nums[3]*nums[4]=3*5*1=15
            solve(2,2): k=2: cost=nums[1]*nums[2]*nums[3]=3*1*5=15, return 15
            total = 15 + 0 + 15 = 30
          solve(2,3) = max(8, 30) = 30

        Total(k=1) = 0 + 30 + 3 = 33

    STEP 2 — k=2: Balloon 1 is LAST to burst in [1,3]
    ─────────────────────────────────────────────────
        left  = solve(1, 1):  k=1: cost=nums[0]*nums[1]*nums[2]=1*3*1=3, return 3
        right = solve(3, 3):  k=3: cost=nums[2]*nums[3]*nums[4]=1*5*1=5, return 5
        cost of bursting 1 LAST: nums[0]*nums[2]*nums[4] = 1*1*1 = 1

        Total(k=2) = 3 + 5 + 1 = 9

    STEP 3 — k=3: Balloon 5 is LAST to burst in [1,3]
    ─────────────────────────────────────────────────
        left  = solve(1, 2)                   ← burst balloons 3,1 first
        right = solve(4, 3) = 0               ← empty range
        cost of bursting 5 LAST: nums[0]*nums[3]*nums[4] = 1*5*1 = 5

        ► solve(1, 2):  balloons with values [3, 1]
          k=1 (3 last): solve(1,0)=0, solve(2,2)=15, cost=nums[0]*nums[1]*nums[3]=1*3*5=15
            total = 0 + 15 + 15 = 30
          k=2 (1 last): solve(1,1)=3, solve(3,2)=0, cost=nums[0]*nums[2]*nums[3]=1*1*5=5
            total = 3 + 0 + 5 = 8
          solve(1,2) = max(30, 8) = 30

        Total(k=3) = 30 + 0 + 5 = 35

    STEP 4 — Pick maximum:
    ─────────────────────
        max(33, 9, 35) = 35  ✓
        Best: Burst 5 LAST in the range.

    WHAT DOES "35" MEAN PHYSICALLY?
    ┌──────────────────────────────────────────────────────────────────┐
    │  Optimal burst order: 1 first, then 3, then 5                  │
    │                                                                 │
    │  Burst 1 (val=1): neighbors are 3,5 → 3*1*5 = 15 coins        │
    │  Burst 3 (val=3): neighbors are 1,5 → 1*3*5 = 15 coins        │
    │       (boundary 1 is dummy, 5 is the remaining balloon)         │
    │  Burst 5 (val=5): neighbors are 1,1 → 1*5*1 = 5 coins         │
    │       (both neighbors are dummies)                              │
    │  Total: 15 + 15 + 5 = 35  ✓                                    │
    └──────────────────────────────────────────────────────────────────┘


================================================================================
================================================================================
    PROBLEM 7: MINIMUM COST TO MERGE STONES (LC 1000 — Hard)
    (Google, Amazon)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given n piles of stones, merge exactly K consecutive piles into one.
    Cost of merge = sum of stones in those K piles.
    Find minimum total cost to merge all into one pile.
    
    Return -1 if impossible.

WHY IS THIS MCM?
    Range [i..j] → partition into K groups → merge those K groups
    Each group is recursively merged first, then the K results merge.

WHEN IS IT IMPOSSIBLE?
    Each merge reduces pile count by K-1 (K piles → 1 pile).
    Starting with n piles, after each merge: n → n-(K-1) → n-2(K-1) → ...
    We need: n - m*(K-1) = 1  →  (n-1) % (K-1) == 0
    If (n-1) % (K-1) != 0 → IMPOSSIBLE, return -1.

KEY INSIGHT:
    dp[i][j] = min cost to merge piles i..j into AS FEW PILES as possible
    Piles i..j can be merged into 1 pile only if (j-i) % (K-1) == 0
    
    k jumps by K-1 (not by 1!) because each sub-group needs (K-1) reductions

================================================================================
ALL APPROACHES
================================================================================
"""

def merge_stones(stones, K):
    """
    Minimum Cost to Merge Stones — Bottom-Up
    Time: O(n^3 / K), Space: O(n^2)
    LC 1000
    """
    n = len(stones)
    if (n - 1) % (K - 1) != 0:
        return -1
    
    # Prefix sums for range sum queries
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + stones[i]
    
    def range_sum(i, j):
        return prefix[j + 1] - prefix[i]
    
    # dp[i][j] = min cost to merge piles i..j optimally
    INF = float('inf')
    dp = [[0] * n for _ in range(n)]
    
    # Fill by gap
    for gap in range(K - 1, n):  # need at least K piles to merge
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = INF
            
            # k steps by K-1 (each sub-partition must be mergeable)
            for k in range(i, j, K - 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
            
            # If this range can be merged into 1 pile, add the merge cost
            if (j - i) % (K - 1) == 0:
                dp[i][j] += range_sum(i, j)
    
    return dp[0][n - 1]


# Memoization version
def merge_stones_memo(stones, K):
    """
    Minimum Cost to Merge Stones — Memoization
    """
    n = len(stones)
    if (n - 1) % (K - 1) != 0:
        return -1
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + stones[i]
    
    memo = {}
    
    def solve(i, j):
        if i == j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        
        result = float('inf')
        for k in range(i, j, K - 1):
            result = min(result, solve(i, k) + solve(k + 1, j))
        
        if (j - i) % (K - 1) == 0:
            result += prefix[j + 1] - prefix[i]
        
        memo[(i, j)] = result
        return result
    
    return solve(0, n - 1)


# Test
print("\n" + "=" * 60)
print("PROBLEM 7: MINIMUM COST TO MERGE STONES")
print("=" * 60)
stones = [3, 2, 4, 1]
print(f"Bottom-Up K=2: {merge_stones(stones, 2)}")  # 20
print(f"Memo K=2: {merge_stones_memo(stones, 2)}")   # 20

stones = [3, 2, 4, 1]
print(f"Bottom-Up K=3: {merge_stones(stones, 3)}")  # -1 (impossible)

stones = [3, 5, 1, 2, 6]
print(f"Bottom-Up K=3: {merge_stones(stones, 3)}")  # 25
print(f"Memo K=3: {merge_stones_memo(stones, 3)}")   # 25


"""
================================================================================
▶▶▶  WALKTHROUGH — MERGE STONES STEP-BY-STEP  ◀◀◀
================================================================================

    EXAMPLE: stones = [3, 2, 4, 1], K = 2
    Goal: Merge consecutive K=2 piles at a time, minimize total cost.
    Check: (n-1) % (K-1) = (4-1) % (2-1) = 3 % 1 = 0 → possible ✓

    HOW MERGING WORKS:
    ┌──────────────────────────────────────────────────────────────────┐
    │  [3, 2, 4, 1]                                                   │
    │   Merge any 2 consecutive piles → cost = sum of those piles    │
    │   Repeat until 1 pile remains                                  │
    └──────────────────────────────────────────────────────────────────┘

    PREFIX SUMS: prefix = [0, 3, 5, 9, 10]
    range_sum(i, j) = prefix[j+1] - prefix[i]
    e.g. range_sum(1, 3) = prefix[4] - prefix[1] = 10 - 3 = 7

    CALL: solve(0, 3)

    STEP-BY-STEP DP TABLE (gap-based filling):
    ─────────────────────────────────────────

    Gap=0 (single piles): dp[i][i] = 0 for all i
        dp[0][0]=0, dp[1][1]=0, dp[2][2]=0, dp[3][3]=0

    Gap=1 (K=2, merge 2 piles — this is the minimum mergeable gap):
        dp[0][1]: k=0: dp[0][0]+dp[1][1] = 0
                  (1-0)%(K-1)=1%1=0 → can merge! add range_sum(0,1)=5
                  dp[0][1] = 0 + 5 = 5
                  Meaning: merge [3,2] → cost 5, result pile = [5]

        dp[1][2]: k=1: dp[1][1]+dp[2][2] = 0
                  (2-1)%1=0 → add range_sum(1,2)=6
                  dp[1][2] = 0 + 6 = 6
                  Meaning: merge [2,4] → cost 6, result pile = [6]

        dp[2][3]: k=2: dp[2][2]+dp[3][3] = 0
                  (3-2)%1=0 → add range_sum(2,3)=5
                  dp[2][3] = 0 + 5 = 5
                  Meaning: merge [4,1] → cost 5, result pile = [5]

    Gap=2 (3 piles):
        dp[0][2]: k=0: dp[0][0]+dp[1][2] = 0+6 = 6
                  k=1: dp[0][1]+dp[2][2] = 5+0 = 5  ← better!
                  (2-0)%1=0 → add range_sum(0,2)=9
                  dp[0][2] = 5 + 9 = 14
                  Meaning: merge [3,2]→5 first, then merge [5,4]→9, total=14

        dp[1][3]: k=1: dp[1][1]+dp[2][3] = 0+5 = 5
                  k=2: dp[1][2]+dp[3][3] = 6+0 = 6
                  (3-1)%1=0 → add range_sum(1,3)=7
                  dp[1][3] = 5 + 7 = 12
                  Meaning: merge [4,1]→5 first, then merge [2,5]→7, total=12

    Gap=3 (all 4 piles):
        dp[0][3]: k=0: dp[0][0]+dp[1][3] = 0+12 = 12
                  k=1: dp[0][1]+dp[2][3] = 5+5 = 10  ← better!
                  k=2: dp[0][2]+dp[3][3] = 14+0 = 14
                  (3-0)%1=0 → add range_sum(0,3)=10
                  dp[0][3] = 10 + 10 = 20  ✓

    ANSWER: dp[0][3] = 20

    OPTIMAL MERGE SEQUENCE (for k=1 split):
    ┌──────────────────────────────────────────────────────────────────┐
    │  [3, 2, 4, 1]                                                   │
    │  Step 1: merge [3,2] → [5, 4, 1]     cost = 5                  │
    │  Step 2: merge [4,1] → [5, 5]         cost = 5                  │
    │  Step 3: merge [5,5] → [10]           cost = 10                 │
    │  Total: 5 + 5 + 10 = 20  ✓                                     │
    └──────────────────────────────────────────────────────────────────┘

    WHY K-1 STEP SIZE IN THE K-LOOP:
    With K=3 (merge 3 at a time), each sub-partition must be reducible
    to a single pile. That requires (size-1) % (K-1) == 0.
    Stepping by K-1 ensures each partition boundary is valid.


================================================================================
================================================================================
    PROBLEM 8: MINIMUM SCORE TRIANGULATION OF POLYGON (LC 1039 — Medium)
    (Google, Amazon)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given polygon with n vertices (values at each vertex), triangulate it
    to minimize the sum of (product of 3 vertices) of all triangles.

WHY IS THIS MCM?
    Range [i..j] → for each triangle, pick vertex k between i and j
    Triangle (i, k, j) has cost = values[i] * values[k] * values[j]
    Left part [i..k] and right part [k..j] are sub-polygons

THIS IS LITERALLY MCM with different cost formula!
    MCM cost: arr[i-1] * arr[k] * arr[j]
    Polygon:  values[i] * values[k] * values[j]
"""

def min_score_triangulation_memo(values):
    """
    Minimum Score Triangulation — Memoization
    Time: O(n^3), Space: O(n^2)
    """
    n = len(values)
    memo = {}
    
    def solve(i, j):
        if j - i < 2:  # need at least 3 vertices for a triangle
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        
        result = float('inf')
        for k in range(i + 1, j):  # k between i and j
            cost = (values[i] * values[k] * values[j] + 
                    solve(i, k) + solve(k, j))
            result = min(result, cost)
        
        memo[(i, j)] = result
        return result
    
    return solve(0, n - 1)


def min_score_triangulation_bottom_up(values):
    """
    Minimum Score Triangulation — Bottom-Up
    Time: O(n^3), Space: O(n^2)
    """
    n = len(values)
    dp = [[0] * n for _ in range(n)]
    
    for gap in range(2, n):  # need at least 3 vertices
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                cost = values[i] * values[k] * values[j] + dp[i][k] + dp[k][j]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]


# Test
print("\n" + "=" * 60)
print("PROBLEM 8: MINIMUM SCORE TRIANGULATION")
print("=" * 60)
values = [1, 2, 3]
print(f"Memo {values}: {min_score_triangulation_memo(values)}")  # 6
print(f"Bottom-Up {values}: {min_score_triangulation_bottom_up(values)}")  # 6

values = [3, 7, 4, 5]
print(f"Memo {values}: {min_score_triangulation_memo(values)}")  # 144
print(f"Bottom-Up {values}: {min_score_triangulation_bottom_up(values)}")  # 144

values = [1, 3, 1, 4, 1, 5]
print(f"Memo {values}: {min_score_triangulation_memo(values)}")  # 13
print(f"Bottom-Up {values}: {min_score_triangulation_bottom_up(values)}")  # 13


"""
================================================================================
▶▶▶  WALKTHROUGH — POLYGON TRIANGULATION STEP-BY-STEP  ◀◀◀
================================================================================

    EXAMPLE: values = [3, 7, 4, 5]  (4-sided polygon, a quadrilateral)
    Goal: Split polygon into triangles, minimize sum of (v[i]*v[k]*v[j])
    Call: solve(0, 3)

    VISUALIZING THE POLYGON:
    ┌──────────────────────────────────────────────────────────────────┐
    │        3 (vertex 0)                                             │
    │       / \                                                       │
    │      /   \                                                      │
    │   5 /     \ 7                                                   │
    │  (3)\     /(1)                                                  │
    │      \   /                                                      │
    │       \ /                                                       │
    │        4 (vertex 2)                                             │
    │                                                                 │
    │  A quadrilateral needs exactly 2 triangles (n-2 = 4-2 = 2)     │
    │  We draw ONE diagonal to split it into 2 triangles.            │
    └──────────────────────────────────────────────────────────────────┘

    CALL: solve(i=0, j=3)
    The edge (0,3) is fixed. We pick a third vertex k between 0 and 3.

    STEP 1 — k=1: Triangle is (0, 1, 3) = vertices 3, 7, 5
    ─────────────────────────────────────────────────────────
        Triangle cost = values[0]*values[1]*values[3] = 3*7*5 = 105
        Remaining: solve(0,1) + solve(1,3)

        solve(0, 1): j-i = 1 < 2 → return 0  (only an edge, no triangle)

        ► solve(1, 3): edge (1,3) fixed, try k=2
          k=2: Triangle (1,2,3) = 7*4*5 = 140
               solve(1,2)=0, solve(2,3)=0
          return 140

        Total(k=1) = 105 + 0 + 140 = 245
        Diagonal: (1,3). Triangles: (3,7,5) and (7,4,5)

    STEP 2 — k=2: Triangle is (0, 2, 3) = vertices 3, 4, 5
    ─────────────────────────────────────────────────────────
        Triangle cost = values[0]*values[2]*values[3] = 3*4*5 = 60
        Remaining: solve(0,2) + solve(2,3)

        ► solve(0, 2): edge (0,2) fixed, try k=1
          k=1: Triangle (0,1,2) = 3*7*4 = 84
               solve(0,1)=0, solve(1,2)=0
          return 84

        solve(2, 3): j-i = 1 < 2 → return 0

        Total(k=2) = 60 + 84 + 0 = 144
        Diagonal: (0,2). Triangles: (3,4,5) and (3,7,4)

    STEP 3 — Pick minimum:
    ─────────────────────
        min(245, 144) = 144  ✓
        Best diagonal: (0,2), creating triangles (3,4,5) and (3,7,4)

    WHY THIS IS LITERALLY MCM:
    ┌──────────────────────────────────────────────────────────────────┐
    │  MCM:      cost = arr[i-1] * arr[k] * arr[j]                   │
    │  Polygon:  cost = values[i] * values[k] * values[j]            │
    │                                                                 │
    │  MCM:      solve(i, k) + solve(k+1, j) + merge_cost            │
    │  Polygon:  solve(i, k) + solve(k, j)   + triangle_cost         │
    │            ↑ note: k, not k+1! (vertex k is shared by both     │
    │              sub-polygons, it's not "consumed")                 │
    └──────────────────────────────────────────────────────────────────┘

    SIMPLER EXAMPLE: values = [1, 2, 3]  (triangle)
    solve(0, 2): k=1: cost = 1*2*3 = 6, solve(0,1)=0, solve(1,2)=0
    Answer: 6  (only one possible triangle, no choice to make)


================================================================================
================================================================================
                    MASTER COMPARISON TABLE — ALL MCM PROBLEMS
================================================================================
================================================================================

┌────────────────────┬──────────────┬──────────────┬───────────────┬──────────┐
│ Problem            │ Base Case    │ k Range      │ Cost Formula  │ Optimize │
├────────────────────┼──────────────┼──────────────┼───────────────┼──────────┤
│ MCM                │ i >= j → 0   │ k: i to j-1  │ a[i-1]*a[k]*  │ MIN      │
│                    │              │              │ a[j]          │          │
├────────────────────┼──────────────┼──────────────┼───────────────┼──────────┤
│ Palindrome Part.   │ i >= j → 0   │ k: i to j-1  │ 1 (per cut)   │ MIN      │
│                    │ isPalin → 0  │              │               │          │
├────────────────────┼──────────────┼──────────────┼───────────────┼──────────┤
│ Boolean Parenth.   │ i == j →     │ k: operators │ operator      │ COUNT    │
│                    │ T/F count    │ (odd indices)│ truth table   │ (SUM)    │
├────────────────────┼──────────────┼──────────────┼───────────────┼──────────┤
│ Scramble String    │ s1==s2 →True │ k: 1 to n-1  │ swap/no-swap  │ OR       │
│                    │ sort≠ →False │              │ both halves   │ (any)    │
├────────────────────┼──────────────┼──────────────┼───────────────┼──────────┤
│ Egg Dropping       │ e==1 → f    │ k: 1 to f    │ 1+max(break,  │ MIN of   │
│                    │ f≤1 → f     │              │ survive)      │ worst    │
├────────────────────┼──────────────┼──────────────┼───────────────┼──────────┤
│ Burst Balloons     │ i > j → 0   │ k: i to j    │ a[i-1]*a[k]*  │ MAX      │
│                    │              │ (LAST burst) │ a[j+1]        │          │
├────────────────────┼──────────────┼──────────────┼───────────────┼──────────┤
│ Merge Stones       │ i == j → 0  │ k: i to j    │ rangeSum if   │ MIN      │
│                    │              │ step K-1     │ mergeable     │          │
├────────────────────┼──────────────┼──────────────┼───────────────┼──────────┤
│ Polygon Triang.    │ j-i < 2 → 0 │ k: i+1 to    │ v[i]*v[k]*    │ MIN      │
│                    │              │ j-1          │ v[j]          │          │
└────────────────────┴──────────────┴──────────────┴───────────────┴──────────┘

================================================================================
QUICK REVISION — THE MCM RECIPE (5 Steps for ANY problem):
================================================================================

    ┌─────────────────────────────────────────────────────────────────┐
    │                                                                 │
    │  1. IDENTIFY:  "Is there a range [i,j] being split at k?"      │
    │                                                                 │
    │  2. BASE CASE: What's the smallest valid input?                 │
    │     Usually: i >= j → 0  OR  i == j → base value               │
    │                                                                 │
    │  3. K-LOOP:    How does k iterate?                              │
    │     Usually: i to j-1  (or i to j, or operators only)           │
    │                                                                 │
    │  4. COST:      What's the merge/split cost?                     │
    │     Usually: some multiplication of boundary elements           │
    │                                                                 │
    │  5. OPTIMIZE:  MIN, MAX, COUNT, or OR?                          │
    │     Depends on what the problem asks for                        │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘

================================================================================
RECURSION → MEMOIZATION → BOTTOM-UP CHEAT SHEET:
================================================================================

    RECURSION:
        def solve(i, j):
            if base_case: return base_value
            ans = initial_value
            for k in range(i, j):
                temp = solve(i, k) + solve(k+1, j) + cost(i, k, j)
                ans = optimize(ans, temp)
            return ans

    MEMOIZATION (add 3 lines):
        memo = {}
        def solve(i, j):
            if (i,j) in memo: return memo[(i,j)]     ← LINE 1
            ... same as recursion ...
            memo[(i,j)] = ans                          ← LINE 2
            return memo[(i,j)]                         ← LINE 3

    BOTTOM-UP (diagonal filling):
        for gap in range(1, n):         ← outer: gap size
            for i in range(n - gap):    ← inner: starting index
                j = i + gap
                dp[i][j] = initial_value
                for k in range(i, j):   ← innermost: split point
                    cost = dp[i][k] + dp[k+1][j] + merge_cost(i, k, j)
                    dp[i][j] = optimize(dp[i][j], cost)
        answer = dp[0][n-1]

================================================================================
FAANG INTERVIEW TIPS — MCM PATTERN:
================================================================================

    TIP 1: ALWAYS draw the recursion tree for small input.
            Shows interviewer you understand the overlapping subproblems.

    TIP 2: "How did you identify MCM?"
            → "I see a range [i,j] that needs to be split at every k.
               Left and right parts combine to give the answer."

    TIP 3: Bottom-up fills DIAGONALLY (by gap), not row-by-row.
            This is THE key difference from knapsack.

    TIP 4: Time for MCM-style problems is usually O(n^3):
            O(n^2) subproblems × O(n) choices for k at each.

    TIP 5: For Burst Balloons, think "LAST to burst" not "FIRST."
            For everything else, think "where to SPLIT."

    TIP 6: Memoization is usually easier to code in interviews.
            Bottom-up is harder (diagonal filling) but shows mastery.

    TIP 7: Common optimizations:
            - Binary search on k (Egg Drop)
            - Palindrome pre-computation (Palindrome Partition)
            - Sorted character check (Scramble String)
            - Inverted DP (Egg Drop optimal)

    TIP 8: Space is always O(n^2) for MCM (2D table for ranges).
            Can't easily reduce like knapsack's 1D trick because
            dp[i][j] depends on MANY cells, not just previous row.

================================================================================
COMPLEXITY SUMMARY:
================================================================================

    ┌────────────────────┬──────────────┬──────────────┬──────────────┐
    │ Problem            │ Recursion    │ Memo/BU      │ Optimal      │
    ├────────────────────┼──────────────┼──────────────┼──────────────┤
    │ MCM                │ O(2^n)       │ O(n^3)       │ O(n^3)       │
    │ Palindrome Part.   │ O(2^n)       │ O(n^3)       │ O(n^2)       │
    │ Boolean Parenth.   │ O(4^n)       │ O(n^3)       │ O(n^3)       │
    │ Scramble String    │ O(4^n)       │ O(n^4)       │ O(n^4)       │
    │ Egg Dropping       │ O(2^f)       │ O(e*f^2)     │ O(e*log f)   │
    │ Burst Balloons     │ O(2^n)       │ O(n^3)       │ O(n^3)       │
    │ Merge Stones       │ O(K^n)       │ O(n^3/K)     │ O(n^3/K)    │
    │ Polygon Triang.    │ O(2^n)       │ O(n^3)       │ O(n^3)       │
    └────────────────────┴──────────────┴──────────────┴──────────────┘

================================================================================
"""


