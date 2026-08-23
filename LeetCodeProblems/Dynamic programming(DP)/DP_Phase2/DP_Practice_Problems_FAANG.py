"""
================================================================================
================================================================================
    DP PRACTICE PROBLEMS — FAANG INTERVIEW GUIDE
    (Problems that DON'T fit Knapsack/LCS/MCM patterns)
================================================================================
================================================================================

These are STANDALONE DP problems that appear frequently in FAANG interviews.
They don't belong to the big 3 families (Knapsack, LCS, MCM) but are
equally important.

    ┌─────────────────────────────────────────────────────────────────────┐
    │                      STANDALONE DP                                  │
    │                          │                                          │
    │  ┌──────────┬────────┬───┼───┬──────────┬──────────┬──────────┐    │
    │  ▼          ▼        ▼   ▼   ▼          ▼          ▼          ▼    │
    │ Count    Jump      House  Knight's  Largest   Word       1D/2D    │
    │ Ways     Game      Robber Tour On   Square    Wrap       Grid     │
    │ (LC 70)  (LC 55)   (LC198)Phone     Submatrix (GFG)      DP       │
    │                    (LC213)(LC 935)  (LC 221)                      │
    └─────────────────────────────────────────────────────────────────────┘

HOW TO IDENTIFY STANDALONE DP:
    - No "pick/skip with capacity" → NOT Knapsack
    - No "two strings comparison" → NOT LCS
    - No "split range [i,j] at k" → NOT MCM
    - But has OPTIMAL SUBSTRUCTURE + OVERLAPPING SUBPROBLEMS → DP!

================================================================================
================================================================================
    PROBLEM 1: COUNT WAYS TO REACH THE NTH STEP (LC 70 — Easy)
    (Amazon, Google, Microsoft, Meta, Apple — THE most asked DP problem)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can climb 1 or 2 steps. How many distinct ways
    can you reach the top?

    Example: n = 4
    Answer: 5 ways → {1111, 112, 121, 211, 22}

WHY IS THIS DP?
    To reach step n, you came from step n-1 (1 step) or step n-2 (2 steps).
    So: ways(n) = ways(n-1) + ways(n-2)
    This is literally FIBONACCI!

IDENTIFICATION TRICK:
    "count ways" + "1 or 2 steps" → Fibonacci DP
    "how many paths" + "choices at each step" → recursive counting DP

ONE-LINE TRICK:
    "dp[i] = dp[i-1] + dp[i-2]  (Fibonacci with dp[0]=1, dp[1]=1)"

GENERALIZATION:
    If you can take 1, 2, or 3 steps: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    If you can take steps from set S:  dp[i] = sum(dp[i-s] for s in S)
    → This becomes Coin Change Count (Unbounded Knapsack)!

================================================================================
APPROACH 1: RECURSION
================================================================================
"""


def count_ways_recursion(n):
    """
    Count Ways to Nth Step — Pure Recursion
    Time: O(2^n) — exponential (FIBONACCI tree)
    Space: O(n) — recursion stack
    """
    if n <= 1:
        return 1
    return count_ways_recursion(n - 1) + count_ways_recursion(n - 2)


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================
"""


def count_ways_memo(n, memo):
    """
    Count Ways — Memoization
    Time: O(n), Space: O(n)
    """
    if n <= 1:
        return 1
    if memo[n] != -1:
        return memo[n]
    memo[n] = count_ways_memo(n - 1, memo) + count_ways_memo(n - 2, memo)
    return memo[n]


"""
================================================================================
APPROACH 3: BOTTOM-UP (Tabulation)
================================================================================

    dp[i] = number of ways to reach step i
    dp[0] = 1 (1 way to stay at ground)
    dp[1] = 1 (1 way to reach step 1)
    dp[i] = dp[i-1] + dp[i-2]
"""


def count_ways_bottom_up(n):
    """
    Count Ways — Bottom-Up DP
    Time: O(n), Space: O(n)
    """
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def count_ways_optimized(n):
    """
    Count Ways — Space Optimized O(1)
    INTERVIEW PREFERRED
    """
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Test
print("=" * 60)
print("PROBLEM 1: COUNT WAYS TO REACH NTH STEP")
print("=" * 60)
n = 4
print(f"Recursion n={n}: {count_ways_recursion(n)}")  # 5
memo = [-1] * (n + 1)
print(f"Memo n={n}: {count_ways_memo(n, memo)}")  # 5
print(f"Bottom-Up n={n}: {count_ways_bottom_up(n)}")  # 5
print(f"Optimized n={n}: {count_ways_optimized(n)}")  # 5
print(f"Optimized n=10: {count_ways_optimized(10)}")  # 89


"""
================================================================================
COUNT WAYS — INTERVIEW TRICKS:
================================================================================

    TRICK 1: This is Fibonacci. dp[0]=1, dp[1]=1, dp[i]=dp[i-1]+dp[i-2]
    
    TRICK 2: For k steps allowed: dp[i] = sum(dp[i-s] for s in steps)
             This generalizes to Coin Change Count!
    
    TRICK 3: Space O(1) — only need previous 2 values
    
    TRICK 4: For VERY large n, use Matrix Exponentiation for O(log n)
    
    TRICK 5: Common follow-up: "What if you can't step on certain stairs?"
             → Set dp[blocked] = 0

    COMPANIES: Amazon, Google, Microsoft, Meta, Apple, Goldman Sachs


================================================================================
================================================================================
    PROBLEM 2: JUMP GAME (LC 55 — Medium)
    (Amazon, Google, Microsoft, Meta)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given array nums where nums[i] = max jump length from position i,
    determine if you can reach the last index.

    Example: [2,3,1,1,4] → True (jump 1→2→3→5 or 1→3→5)
    Example: [3,2,1,0,4] → False (stuck at index 3)

WHY IS THIS DP (and also Greedy)?
    DP: dp[i] = can I reach index i?
    Greedy: track the farthest reachable position (MUCH faster!)

IDENTIFICATION TRICK:
    "can you reach" + "jump lengths" → Jump Game
    Greedy is preferred but know the DP approach too.

================================================================================
APPROACH 1: RECURSION
================================================================================
"""


def jump_game_recursion(nums, pos):
    """
    Jump Game — Pure Recursion
    Time: O(2^n) — exponential
    """
    if pos >= len(nums) - 1:
        return True
    
    max_jump = nums[pos]
    for jump in range(1, max_jump + 1):
        if jump_game_recursion(nums, pos + jump):
            return True
    
    return False


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================
"""


def jump_game_memo(nums, pos, memo):
    """
    Jump Game — Memoization
    Time: O(n^2), Space: O(n)
    """
    if pos >= len(nums) - 1:
        return True
    
    if memo[pos] != -1:
        return memo[pos] == 1
    
    max_jump = nums[pos]
    for jump in range(1, max_jump + 1):
        if jump_game_memo(nums, pos + jump, memo):
            memo[pos] = 1
            return True
    
    memo[pos] = 0
    return False


"""
================================================================================
APPROACH 3: BOTTOM-UP DP
================================================================================
"""


def jump_game_bottom_up(nums):
    """
    Jump Game — Bottom-Up DP
    Time: O(n^2), Space: O(n)
    """
    n = len(nums)
    dp = [False] * n
    dp[0] = True
    
    for i in range(1, n):
        for j in range(i):
            if dp[j] and j + nums[j] >= i:
                dp[i] = True
                break
    
    return dp[n - 1]


"""
================================================================================
APPROACH 4: GREEDY (OPTIMAL — Interviewers want this!)
================================================================================

    Track farthest reachable position.
    If current position > farthest → stuck, return False.
    If farthest >= last index → return True.
"""


def jump_game_greedy(nums):
    """
    Jump Game — Greedy
    Time: O(n), Space: O(1)
    THE INTERVIEW ANSWER — always present this!
    """
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False  # can't reach this position
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:
            return True
    return True


# Test
print("\n" + "=" * 60)
print("PROBLEM 2: JUMP GAME")
print("=" * 60)
nums = [2, 3, 1, 1, 4]
print(f"Recursion {nums}: {jump_game_recursion(nums, 0)}")  # True
memo = [-1] * len(nums)
print(f"Memo {nums}: {jump_game_memo(nums, 0, memo)}")  # True
print(f"Bottom-Up {nums}: {jump_game_bottom_up(nums)}")  # True
print(f"Greedy {nums}: {jump_game_greedy(nums)}")  # True

nums = [3, 2, 1, 0, 4]
print(f"Greedy {nums}: {jump_game_greedy(nums)}")  # False
print(f"Bottom-Up {nums}: {jump_game_bottom_up(nums)}")  # False


"""
================================================================================
JUMP GAME — INTERVIEW TRICKS:
================================================================================

    TRICK 1: Start with DP approach, then OPTIMIZE to Greedy.
             Shows you can think both ways.
    
    TRICK 2: Greedy = track farthest reachable. If i > farthest → stuck.
    
    TRICK 3: Follow-up "Jump Game II" (LC 45) = MIN jumps to reach end.
             Use BFS-like greedy: track current level end + farthest.
    
    TRICK 4: nums[i] = 0 is the trap. You get stuck only if
             no previous position can jump OVER this 0.

    COMPANIES: Amazon, Google, Microsoft, Meta, Apple, Goldman Sachs


================================================================================
================================================================================
    PROBLEM 3: ROBBERY / HOUSE ROBBER (LC 198 — Medium)
    (Amazon, Google, Microsoft, Goldman Sachs, Meta)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given array nums representing money in each house, find MAXIMUM
    money you can rob without robbing two ADJACENT houses.

    Example: [2, 7, 9, 3, 1] → 12 (rob houses 0, 2, 4 → 2+9+1=12)
    Example: [1, 2, 3, 1] → 4 (rob houses 0, 2 → 1+3=4)

WHY IS THIS DP?
    At each house i: ROB it (skip i-1, add to i-2's result) or SKIP it (keep i-1's result)
    dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    
    This is a LINEAR DP with pick/skip decision (NOT knapsack — no capacity constraint)

IDENTIFICATION TRICK:
    "can't pick adjacent" + "maximize" → House Robber pattern
    "non-adjacent selection" → House Robber

ONE-LINE TRICK:
    "At each house: max(rob_this + best_two_back, skip_and_keep_prev)"

CHOICE DIAGRAM:
                    house i
                   /        \\
                  /          \\
              ROB it         SKIP it
                |               |
         nums[i] +          dp[i-1]
         dp[i-2]            (keep previous best)
                \\          /
                 \\        /
               dp[i] = MAX

================================================================================
APPROACH 1: RECURSION
================================================================================
"""


def robbery_recursion(nums, i):
    """
    House Robber — Pure Recursion
    Time: O(2^n) — exponential
    """
    if i < 0:
        return 0
    return max(nums[i] + robbery_recursion(nums, i - 2),  # rob this house
               robbery_recursion(nums, i - 1))             # skip this house


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================
"""


def robbery_memo(nums, i, memo):
    """
    House Robber — Memoization
    Time: O(n), Space: O(n)
    """
    if i < 0:
        return 0
    if memo[i] != -1:
        return memo[i]
    memo[i] = max(nums[i] + robbery_memo(nums, i - 2, memo),
                  robbery_memo(nums, i - 1, memo))
    return memo[i]


"""
================================================================================
APPROACH 3: BOTTOM-UP DP
================================================================================

    dp[i] = max money robbing houses 0..i
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    dp[i] = max(nums[i] + dp[i-2], dp[i-1])
"""


def robbery_bottom_up(nums):
    """
    House Robber — Bottom-Up DP
    Time: O(n), Space: O(n)
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    
    return dp[n - 1]


def robbery_optimized(nums):
    """
    House Robber — Space Optimized O(1)
    INTERVIEW PREFERRED
    """
    if not nums:
        return 0
    
    prev2 = 0  # dp[i-2]
    prev1 = 0  # dp[i-1]
    
    for num in nums:
        curr = max(num + prev2, prev1)
        prev2 = prev1
        prev1 = curr
    
    return prev1


# Test
print("\n" + "=" * 60)
print("PROBLEM 3: ROBBERY (HOUSE ROBBER)")
print("=" * 60)
nums = [2, 7, 9, 3, 1]
print(f"Recursion {nums}: {robbery_recursion(nums, len(nums) - 1)}")  # 12
memo = [-1] * len(nums)
print(f"Memo {nums}: {robbery_memo(nums, len(nums) - 1, memo)}")  # 12
print(f"Bottom-Up {nums}: {robbery_bottom_up(nums)}")  # 12
print(f"Optimized {nums}: {robbery_optimized(nums)}")  # 12

nums = [1, 2, 3, 1]
print(f"Optimized {nums}: {robbery_optimized(nums)}")  # 4


"""
================================================================================
ROBBERY — INTERVIEW TRICKS:
================================================================================

    TRICK 1: dp[i] = max(rob + dp[i-2], skip + dp[i-1])
             Only need previous 2 values → O(1) space
    
    TRICK 2: House Robber II (LC 213) — houses in a CIRCLE:
             Run House Robber twice: once on nums[0..n-2], once on nums[1..n-1]
             Answer = max of both (can't rob both first and last)
    
    TRICK 3: House Robber III (LC 337) — houses form a TREE:
             For each node: max(rob_node + grandchildren, skip_node + children)
             Use DFS returning (rob, skip) pair for each node
    
    TRICK 4: This is NOT knapsack! No capacity constraint.
             It's LINEAR DP with adjacency constraint.

    COMPANIES: Amazon, Google, Microsoft, Meta, Goldman Sachs, Apple


================================================================================
================================================================================
    PROBLEM 4: KNIGHT'S TOUR ON A PHONE KEYPAD (LC 935 — Medium)
    (Google, Amazon, Microsoft, Meta)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Phone keypad:
        1 2 3
        4 5 6
        7 8 9
        * 0 #
    
    A chess knight starts on ANY numeric key, makes exactly n-1 hops.
    Each hop must be a valid L-shaped knight move.
    Count the number of distinct phone numbers of length n.

    Example: n = 1 → 10 (any single digit)
    Example: n = 2 → 20

WHY IS THIS DP?
    From each digit, knight can move to specific other digits.
    dp[digit][steps] = # of numbers starting from digit with steps remaining
    Total = sum over all digits of dp[digit][n]

IDENTIFICATION TRICK:
    "chess knight" + "phone keypad" + "count paths/numbers" → DP on graph

KEY INSIGHT — THE JUMP MAP (memorize this!):
    From 0 → [4, 6]
    From 1 → [6, 8]
    From 2 → [7, 9]
    From 3 → [4, 8]
    From 4 → [0, 3, 9]
    From 5 → []           ← knight can't go anywhere from 5!
    From 6 → [0, 1, 7]
    From 7 → [2, 6]
    From 8 → [1, 3]
    From 9 → [2, 4]

    MEMORY TRICK: 
        Corners (1,3,7,9) each have 2 neighbors
        Sides (2,4,6,8) — 4 has 3, 6 has 3, 2 has 2, 8 has 2
        0 has 2 neighbors, 5 has NONE
        Total moves from all digits = 20 (that's why n=2 gives 20!)

================================================================================
APPROACH 1: RECURSION
================================================================================
"""

KNIGHT_MOVES = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}


def knight_dialer_recursion(n):
    """
    Knight Dialer — Pure Recursion
    Time: O(3^n) — exponential
    """
    MOD = 10**9 + 7
    
    def count(digit, remaining):
        if remaining == 0:
            return 1
        total = 0
        for next_digit in KNIGHT_MOVES[digit]:
            total += count(next_digit, remaining - 1)
        return total % MOD
    
    result = 0
    for digit in range(10):
        result = (result + count(digit, n - 1)) % MOD
    return result


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================

    WHAT CHANGES? → digit (0-9) and remaining steps
    Memo: dp[10][n] or dictionary
"""


def knight_dialer_memo(n):
    """
    Knight Dialer — Memoization
    Time: O(10 * n), Space: O(10 * n)
    """
    MOD = 10**9 + 7
    memo = {}
    
    def count(digit, remaining):
        if remaining == 0:
            return 1
        if (digit, remaining) in memo:
            return memo[(digit, remaining)]
        
        total = 0
        for next_digit in KNIGHT_MOVES[digit]:
            total = (total + count(next_digit, remaining - 1)) % MOD
        
        memo[(digit, remaining)] = total
        return total
    
    result = 0
    for digit in range(10):
        result = (result + count(digit, n - 1)) % MOD
    return result


"""
================================================================================
APPROACH 3: BOTTOM-UP DP
================================================================================

    dp[step][digit] = # of numbers of length (step+1) ending at digit
    Start: dp[0][d] = 1 for all digits
    Transition: dp[step][digit] = sum(dp[step-1][prev] for prev in KNIGHT_MOVES[digit])
    Answer: sum(dp[n-1][d] for d in 0..9)
"""


def knight_dialer_bottom_up(n):
    """
    Knight Dialer — Bottom-Up DP
    Time: O(10 * n), Space: O(10)
    INTERVIEW PREFERRED
    """
    MOD = 10**9 + 7
    
    # dp[digit] = count of numbers ending at this digit
    dp = [1] * 10  # step 0: each digit alone = 1 number
    
    for _ in range(n - 1):
        new_dp = [0] * 10
        for digit in range(10):
            for prev in KNIGHT_MOVES[digit]:
                new_dp[digit] = (new_dp[digit] + dp[prev]) % MOD
        dp = new_dp
    
    return sum(dp) % MOD


# Test
print("\n" + "=" * 60)
print("PROBLEM 4: KNIGHT'S TOUR ON A PHONE KEYPAD")
print("=" * 60)
print(f"Recursion n=1: {knight_dialer_recursion(1)}")  # 10
print(f"Recursion n=2: {knight_dialer_recursion(2)}")  # 20
print(f"Memo n=3: {knight_dialer_memo(3)}")  # 46
print(f"Bottom-Up n=1: {knight_dialer_bottom_up(1)}")  # 10
print(f"Bottom-Up n=2: {knight_dialer_bottom_up(2)}")  # 20
print(f"Bottom-Up n=3: {knight_dialer_bottom_up(3)}")  # 46
print(f"Bottom-Up n=4: {knight_dialer_bottom_up(4)}")  # 104


"""
================================================================================
KNIGHT DIALER — INTERVIEW TRICKS:
================================================================================

    TRICK 1: Pre-compute the jump map. Draw the keypad and trace L-moves.
    
    TRICK 2: Only 10 states (digits 0-9) → dp is just array of 10.
             Space is O(10) = O(1) with rolling array!
    
    TRICK 3: 5 is a dead end (no valid knight moves). It only contributes
             to n=1 (single digit "5").
    
    TRICK 4: For very large n, use MATRIX EXPONENTIATION:
             Build 10×10 transition matrix M where M[i][j] = 1 if knight
             can jump from j to i. Answer = sum of (M^(n-1) × [1,1,...,1])
             Time: O(10^3 * log n) = O(log n)
    
    TRICK 5: Don't forget MOD = 10^9 + 7 !

    COMPANIES: Google, Amazon, Microsoft, Meta, Goldman Sachs


================================================================================
================================================================================
    PROBLEM 5: LARGEST SQUARE SUBMATRIX WITH ALL 1s (LC 221 — Medium)
    (Amazon, Google, Microsoft, Goldman Sachs, Apple)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given a binary matrix, find the LARGEST square containing only 1s
    and return its area.

    Example:
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0
    → Largest square = 2×2 = area 4

WHY IS THIS DP?
    At each cell (i,j), if it's a 1, the largest square ending at (i,j)
    depends on the squares ending at (i-1,j), (i,j-1), and (i-1,j-1).

IDENTIFICATION TRICK:
    "largest square" + "matrix" + "all 1s" → Matrix DP

ONE-LINE TRICK:
    "dp[i][j] = 1 + min(left, top, top-left diagonal) if matrix[i][j] == 1"

KEY INSIGHT (THE BOTTLENECK PRINCIPLE):
    A square of side k at (i,j) needs:
        - Square of side k-1 at (i-1,j)    ← top
        - Square of side k-1 at (i,j-1)    ← left
        - Square of side k-1 at (i-1,j-1)  ← diagonal
    
    If ANY of them is smaller → the square at (i,j) is limited.
    Hence: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

VISUAL:
    dp[i-1][j-1]  dp[i-1][j]
    dp[i][j-1]    dp[i][j] = ?
    
    dp[i][j] = 1 + min(all three neighbors) if matrix[i][j] == '1'

================================================================================
APPROACH 1: RECURSION
================================================================================
"""


def largest_square_recursion(matrix):
    """
    Largest Square — Recursion (checks all squares, brute force)
    Time: O(m*n*min(m,n)) 
    """
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    max_side = 0
    
    def check(r, c, size):
        for i in range(r, r + size):
            for j in range(c, c + size):
                if i >= rows or j >= cols or matrix[i][j] == '0':
                    return False
        return True
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                side = 1
                while check(i, j, side + 1):
                    side += 1
                max_side = max(max_side, side)
    
    return max_side * max_side


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================
"""


def largest_square_memo(matrix):
    """
    Largest Square — Memoization
    Time: O(m*n), Space: O(m*n)
    """
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    memo = {}
    max_side = [0]
    
    def solve(i, j):
        if i < 0 or j < 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        
        if matrix[i][j] == '0':
            memo[(i, j)] = 0
        else:
            memo[(i, j)] = 1 + min(solve(i - 1, j),
                                    solve(i, j - 1),
                                    solve(i - 1, j - 1))
        max_side[0] = max(max_side[0], memo[(i, j)])
        return memo[(i, j)]
    
    for i in range(rows):
        for j in range(cols):
            solve(i, j)
    
    return max_side[0] ** 2


"""
================================================================================
APPROACH 3: BOTTOM-UP DP
================================================================================

    dp[i][j] = side length of largest square with bottom-right corner at (i,j)
    
DP TABLE TRACE:
    Matrix:            dp:
    1 0 1 0 0          1 0 1 0 0
    1 0 1 1 1          1 0 1 1 1
    1 1 1 1 1    →     1 1 1 2 2
    1 0 0 1 0          1 0 0 1 0

    max dp value = 2, area = 2² = 4
"""


def largest_square_bottom_up(matrix):
    """
    Largest Square — Bottom-Up DP
    Time: O(m*n), Space: O(m*n)
    INTERVIEW PREFERRED
    """
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1  # first row/col: can only be 1
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],
                                       dp[i][j - 1],
                                       dp[i - 1][j - 1])
                max_side = max(max_side, dp[i][j])
    
    return max_side * max_side


def largest_square_space_optimized(matrix):
    """
    Space Optimized — O(n) using 1 row
    """
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    dp = [0] * cols
    max_side = 0
    prev_diag = 0  # dp[i-1][j-1]
    
    for i in range(rows):
        for j in range(cols):
            temp = dp[j]  # save before overwrite (this becomes next prev_diag)
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = 1 + min(dp[j],         # top (old dp[j])
                                    dp[j - 1],      # left
                                    prev_diag)       # diagonal
            else:
                dp[j] = 0
            prev_diag = temp
            max_side = max(max_side, dp[j])
    
    return max_side * max_side


# Test
print("\n" + "=" * 60)
print("PROBLEM 5: LARGEST SQUARE SUBMATRIX WITH ALL 1s")
print("=" * 60)
matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]
print(f"Bottom-Up: {largest_square_bottom_up(matrix)}")  # 4
print(f"Space-Opt: {largest_square_space_optimized(matrix)}")  # 4
print(f"Memo: {largest_square_memo(matrix)}")  # 4

matrix2 = [
    ['1', '1', '1'],
    ['1', '1', '1'],
    ['1', '1', '1']
]
print(f"Bottom-Up 3x3 all 1s: {largest_square_bottom_up(matrix2)}")  # 9


"""
================================================================================
LARGEST SQUARE — INTERVIEW TRICKS:
================================================================================

    TRICK 1: dp[i][j] = 1 + min(top, left, diagonal) — the MIN is the bottleneck!
    
    TRICK 2: First row and first column can only have dp = 0 or 1 (no room for square)
    
    TRICK 3: Follow-up "Maximal Rectangle" (LC 85 — Hard):
             Use histogram approach — for each row, compute largest rectangle.
    
    TRICK 4: Space optimize: only need previous row + one diagonal variable
    
    TRICK 5: Return AREA not side length! area = side * side

    COMPANIES: Amazon, Google, Microsoft, Meta, Goldman Sachs, Apple


================================================================================
================================================================================
    PROBLEM 6: WORD WRAP (GFG — Medium-Hard)
    (Google, Amazon, Microsoft)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given array of word lengths and line width M, arrange words on lines
    to MINIMIZE the total cost of extra spaces.
    
    Cost = sum of (extra spaces)^3 for each line (penalizes uneven distribution)
    Last line's cost is typically 0 (or ignored).

    Example:
    words = [3, 2, 2, 5], M = 6
    Line 1: word1(3) + space + word2(2) = 6 → 0 extra spaces → cost 0
    Line 2: word3(2) → 4 extra spaces → cost 64
    Line 3: word4(5) → 1 extra space → cost 0 (last line)
    Total cost = 0 + 64 = 64
    
    But better: 
    Line 1: word1(3) → 3 extra → cost 27
    Line 2: word2(2) + space + word3(2) = 5 → 1 extra → cost 1
    Line 3: word4(5) → cost 0 (last line)
    Total cost = 27 + 1 = 28  ← better!

WHY IS THIS DP?
    For each word i, try placing words i..j on one line.
    Cost of that line = (M - total_width)^3
    Find the partition that minimizes total cost.

IDENTIFICATION TRICK:
    "arrange words on lines" + "minimize cost of spaces" → Word Wrap DP

KEY INSIGHT:
    dp[i] = min cost to arrange words i..n-1
    For each i, try ending the line at word j (i <= j < n):
        If words i..j fit on one line:
            dp[i] = min(line_cost(i, j) + dp[j+1])

================================================================================
APPROACH 1: RECURSION
================================================================================
"""


def word_wrap_recursion(words, M):
    """
    Word Wrap — Pure Recursion
    Time: O(2^n) — exponential
    """
    n = len(words)
    
    def solve(i):
        if i >= n:
            return 0
        
        mn = float('inf')
        curr_len = 0
        
        for j in range(i, n):
            # Add word j to current line
            curr_len += words[j]
            if j > i:
                curr_len += 1  # space between words
            
            if curr_len > M:
                break  # line overflow
            
            extra = M - curr_len
            # Last line has 0 cost
            if j == n - 1:
                cost = 0
            else:
                cost = extra ** 3
            
            mn = min(mn, cost + solve(j + 1))
        
        return mn
    
    return solve(0)


"""
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================
"""


def word_wrap_memo(words, M):
    """
    Word Wrap — Memoization
    Time: O(n * M), Space: O(n)
    """
    n = len(words)
    memo = {}
    
    def solve(i):
        if i >= n:
            return 0
        if i in memo:
            return memo[i]
        
        mn = float('inf')
        curr_len = 0
        
        for j in range(i, n):
            curr_len += words[j]
            if j > i:
                curr_len += 1
            
            if curr_len > M:
                break
            
            extra = M - curr_len
            cost = 0 if j == n - 1 else extra ** 3
            mn = min(mn, cost + solve(j + 1))
        
        memo[i] = mn
        return mn
    
    return solve(0)


"""
================================================================================
APPROACH 3: BOTTOM-UP DP
================================================================================

    dp[i] = min cost to arrange words i..n-1
    Fill from right to left (i = n-1 down to 0)
    Answer: dp[0]
"""


def word_wrap_bottom_up(words, M):
    """
    Word Wrap — Bottom-Up DP
    Time: O(n * M), Space: O(n)
    INTERVIEW PREFERRED
    """
    n = len(words)
    dp = [float('inf')] * (n + 1)
    dp[n] = 0  # no words left = 0 cost
    
    for i in range(n - 1, -1, -1):
        curr_len = 0
        for j in range(i, n):
            curr_len += words[j]
            if j > i:
                curr_len += 1  # space between words
            
            if curr_len > M:
                break
            
            extra = M - curr_len
            cost = 0 if j == n - 1 else extra ** 3
            dp[i] = min(dp[i], cost + dp[j + 1])
    
    return dp[0]


# Test
print("\n" + "=" * 60)
print("PROBLEM 6: WORD WRAP")
print("=" * 60)
words = [3, 2, 2, 5]
M = 6
print(f"Recursion {words}, M={M}: {word_wrap_recursion(words, M)}")
print(f"Memo {words}, M={M}: {word_wrap_memo(words, M)}")
print(f"Bottom-Up {words}, M={M}: {word_wrap_bottom_up(words, M)}")

words = [3, 2, 2]
M = 6
print(f"Bottom-Up {words}, M={M}: {word_wrap_bottom_up(words, M)}")


"""
================================================================================
WORD WRAP — INTERVIEW TRICKS:
================================================================================

    TRICK 1: Cost function matters! (extra_spaces)^2 or (extra_spaces)^3
             Ask the interviewer which cost function to use.
    
    TRICK 2: LAST line cost = 0 (no penalty for trailing spaces)
    
    TRICK 3: Don't forget to add 1 for spaces BETWEEN words on same line
    
    TRICK 4: This is similar to MCM — we're partitioning words into groups (lines)
             But simpler because partitions must be CONTIGUOUS.
    
    TRICK 5: Greedy (just pack as many words as possible per line) is NOT optimal.
             That's why we need DP.

    COMPANIES: Google, Amazon, Microsoft, Adobe


================================================================================
================================================================================
                    MASTER PROBLEM MAPPING — WHERE EACH PROBLEM BELONGS
================================================================================
================================================================================

    ┌────────────────────────────────┬──────────────────────────┬───────────────┐
    │ Problem                        │ DP Pattern               │ File          │
    ├────────────────────────────────┼──────────────────────────┼───────────────┤
    │ Count Ways To Reach Nth Step   │ Fibonacci / Linear DP    │ THIS FILE     │
    │ Minimum Coins                  │ Unbounded Knapsack       │ Unbounded_KS  │
    │ Jump Game                      │ Greedy / Linear DP       │ THIS FILE     │
    │ Robbery (House Robber)         │ Linear DP                │ THIS FILE     │
    │ Knight's Tour On Phone Keypad  │ DP on Graph              │ THIS FILE     │
    │ Levenshtein Distance           │ LCS variant              │ LCS file      │
    │ Word Break Count               │ Unbounded Knapsack       │ Unbounded_KS  │
    │ Equal Subset Partition         │ 0/1 Knapsack             │ Knapsack file │
    │ Cut Rod To Maximize Profit     │ Unbounded Knapsack       │ Unbounded_KS  │
    │ Number Of Ways To Make Change  │ Unbounded Knapsack       │ Unbounded_KS  │
    │ Largest Square Submatrix       │ Matrix DP                │ THIS FILE     │
    │ Word Wrap                      │ Partitioning DP          │ THIS FILE     │
    │ Strings Interleave             │ LCS variant              │ LCS file      │
    │ Longest Common Subsequence     │ LCS                      │ LCS file      │
    │ Matrix Chain Multiplication    │ MCM / Partition DP       │ MCM file      │
    └────────────────────────────────┴──────────────────────────┴───────────────┘

================================================================================
QUICK REVISION — STANDALONE DP PATTERNS:
================================================================================

    ┌─────────────────────┬────────────────────────────────────────────────────┐
    │ Pattern             │ Formula                                            │
    ├─────────────────────┼────────────────────────────────────────────────────┤
    │ Fibonacci/Stairs    │ dp[i] = dp[i-1] + dp[i-2]                         │
    │ House Robber        │ dp[i] = max(nums[i]+dp[i-2], dp[i-1])             │
    │ Jump Game           │ Greedy: track farthest reachable                  │
    │ Knight Dialer       │ dp[digit] = sum(dp[prev] for prev in moves)       │
    │ Largest Square      │ dp[i][j] = 1 + min(top, left, diag) if cell='1'  │
    │ Word Wrap           │ dp[i] = min(cost(i,j) + dp[j+1]) for valid j     │
    └─────────────────────┴────────────────────────────────────────────────────┘

================================================================================
"""
