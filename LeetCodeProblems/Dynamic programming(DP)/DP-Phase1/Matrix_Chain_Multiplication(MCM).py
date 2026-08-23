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


