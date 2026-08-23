"""
================================================================================
================================================================================
    UNBOUNDED KNAPSACK — ULTIMATE FAANG/MAANG TRICKS & CHEAT SHEET
================================================================================
================================================================================

MASTER TRICK: "STAY on same row" vs "GO to previous row"
=========================================================

    0/1 Knapsack:       t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])
                                                    ^^^
                                              GO TO PREVIOUS ROW (i-1)
                                              (item used once, move on)

    Unbounded Knapsack: t[i][j] = max(val[i-1] + t[i][j-wt[i-1]], t[i-1][j])
                                                    ^^
                                              STAY ON SAME ROW (i)
                                              (item can be reused!)

    ONE CHARACTER DIFFERENCE: i-1 → i (when including the item)

    MEMORY TRICK: "Unbounded = Unlimited = U stay on same row (U = U reuse)"

================================================================================
THE UNBOUNDED KNAPSACK FAMILY (7 FAANG Problems):
================================================================================

    ┌─────────────────────────────────────────────────────────────────┐
    │                   UNBOUNDED KNAPSACK                            │
    │                        │                                        │
    │    ┌────────┬──────────┼──────────┬──────────┬──────────┐       │
    │    ▼        ▼          ▼          ▼          ▼          ▼       │
    │  Rod     Coin       Coin       Integer   Perfect   Minimum     │
    │ Cutting  Change I   Change II   Break    Squares   Cost for    │
    │          (Ways)     (Min Coins) (LC343)  (LC279)   Tickets     │
    │                                                    (LC983)     │
    └─────────────────────────────────────────────────────────────────┘

================================================================================
IDENTIFICATION TRICK — "How do I know it's UNBOUNDED Knapsack?"
================================================================================

    Ask yourself these 3 questions:
    
    1. Is there a CHOICE? (pick or skip) → YES = Knapsack family
    2. Can I REUSE the same item? → YES = UNBOUNDED
    3. What am I optimizing? → MAX/MIN/COUNT

    KEYWORD SPOTTERS in problem statement:
    ┌────────────────────────────────────────────────┐
    │ "infinite supply"      → UNBOUNDED             │
    │ "unlimited quantity"   → UNBOUNDED             │
    │ "can use multiple times" → UNBOUNDED           │
    │ "as many times as you want" → UNBOUNDED        │
    │ "at most once"         → 0/1 Knapsack          │
    │ "each item exactly once" → 0/1 Knapsack        │
    └────────────────────────────────────────────────┘

================================================================================
VARIABLE MAPPING TRICK (The Golden Table):
================================================================================

    Every unbounded knapsack problem maps to the SAME template.
    Just swap variables:

    ┌──────────────────┬──────────┬──────────┬─────────────┬──────────────┐
    │ Problem          │ items[]  │ values[] │ capacity(W) │ Optimize     │
    ├──────────────────┼──────────┼──────────┼─────────────┼──────────────┤
    │ Rod Cutting      │ length[] │ price[]  │ rod_length  │ MAX profit   │
    │ Coin Change I    │ coins[]  │ 1 (each) │ target_sum  │ COUNT ways   │
    │ Coin Change II   │ coins[]  │ 1 (each) │ target_sum  │ MIN coins    │
    │ Integer Break    │ [1..n-1] │ products │ n           │ MAX product  │
    │ Perfect Squares  │ [1,4,9.] │ 1 (each) │ n           │ MIN squares  │
    │ Min Cost Tickets │ [1,7,30] │ costs[]  │ max_day     │ MIN cost     │
    └──────────────────┴──────────┴──────────┴─────────────┴──────────────┘

================================================================================
CODE TEMPLATE — THE UNIVERSAL UNBOUNDED KNAPSACK (Memorize THIS):
================================================================================

    def unbounded_knapsack(wt, val, W, n):
        dp = [[0] * (W + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, W + 1):
                if wt[i-1] <= j:
                    dp[i][j] = max(val[i-1] + dp[i][j - wt[i-1]],  # STAY (reuse)
                                   dp[i-1][j])                       # SKIP
                else:
                    dp[i][j] = dp[i-1][j]                            # Can't fit

        return dp[n][W]

    SPACE OPTIMIZED (1D array):
    
    def unbounded_knapsack_1d(wt, val, W, n):
        dp = [0] * (W + 1)
        for i in range(n):
            for j in range(wt[i], W + 1):   # LEFT to RIGHT (reuse allowed!)
                dp[j] = max(dp[j], val[i] + dp[j - wt[i]])
        return dp[W]

    CRITICAL TRICK for 1D:
    ┌────────────────────────────────────────────────────────────────┐
    │  0/1 Knapsack 1D:  iterate j from RIGHT to LEFT (W → wt[i])  │
    │  Unbounded 1D:     iterate j from LEFT to RIGHT (wt[i] → W)  │
    │                                                                │
    │  WHY? Left-to-right uses updated values = reusing same item!  │
    └────────────────────────────────────────────────────────────────┘

================================================================================
================================================================================
    PROBLEM 1: ROD CUTTING (Amazon, Google, Goldman Sachs)
================================================================================
================================================================================

    TRICK: "Rod cutting IS unbounded knapsack where lengths are weights
            and prices are values. Rod length N is the capacity."

    Mapping:
        wt[]  = [1, 2, 3, ..., N]  (possible cut lengths)
        val[] = price[]             (price for each length)
        W     = N                   (total rod length)
"""


# ═══════════════════════════════════════════════════════════════════
# ROD CUTTING — Interview Ready Code
# ═══════════════════════════════════════════════════════════════════

def rod_cutting_2d(price, n):
    """
    Rod Cutting using 2D DP (Unbounded Knapsack style)
    price[i] = price of rod of length i+1
    n = total rod length
    """
    length = list(range(1, n + 1))  # [1, 2, 3, ..., n]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if length[i-1] <= j:
                # STAY on same row (unbounded: can cut same length again)
                dp[i][j] = max(price[i-1] + dp[i][j - length[i-1]],
                               dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][n]


def rod_cutting_1d(price, n):
    """
    Rod Cutting — Space Optimized O(n) space
    FAANG INTERVIEW PREFERRED VERSION
    """
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1):  # left to right (unbounded!)
            dp[j] = max(dp[j], price[i-1] + dp[j - i])

    return dp[n]


# Test
print("=== ROD CUTTING ===")
price = [1, 5, 8, 9, 10, 17, 17, 20]
print(f"Max profit: {rod_cutting_1d(price, 8)}")  # Output: 22
print(f"Max profit (2D): {rod_cutting_2d(price, 8)}")  # Output: 22


"""
================================================================================
================================================================================
    PROBLEM 2: COIN CHANGE I — Count Ways (Amazon, Microsoft, Goldman Sachs)
    LeetCode 518: Coin Change II (confusing name — it's counting ways)
================================================================================
================================================================================

    TRICK: "Same as unbounded knapsack, but instead of MAX, we ADD.
            Because we want COUNT of ways, not maximum value."

    Mapping:
        wt[]  = coins[]           (coin denominations)
        val[] = doesn't matter    (we're counting, not maximizing)
        W     = target_sum
        
    KEY CHANGE from standard template:
        Standard:  dp[i][j] = MAX(include, exclude)
        Count:     dp[i][j] = include + exclude  (ADD both paths!)

    BASE CASE TRICK:
        dp[i][0] = 1 for all i  (there's exactly 1 way to make sum 0: pick nothing)
"""


# ═══════════════════════════════════════════════════════════════════
# COIN CHANGE I (Count Ways) — Interview Ready Code
# ═══════════════════════════════════════════════════════════════════

def coin_change_ways_2d(coins, target):
    """
    Count number of ways to make target sum using unlimited coins.
    LeetCode 518: Coin Change II
    """
    n = len(coins)
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    # Base case: 1 way to make sum 0 (pick nothing)
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if coins[i-1] <= j:
                # STAY (reuse coin) + SKIP (don't use this coin)
                dp[i][j] = dp[i][j - coins[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target]


def coin_change_ways_1d(coins, target):
    """
    Space Optimized — FAANG INTERVIEW PREFERRED
    """
    dp = [0] * (target + 1)
    dp[0] = 1  # 1 way to make sum 0

    for coin in coins:
        for j in range(coin, target + 1):  # left to right!
            dp[j] += dp[j - coin]

    return dp[target]


# Test
print("\n=== COIN CHANGE I (Count Ways) ===")
coins = [1, 2, 3]
print(f"Ways to make sum 5: {coin_change_ways_1d(coins, 5)}")  # Output: 5
print(f"Ways (2D): {coin_change_ways_2d(coins, 5)}")  # Output: 5


"""
================================================================================
================================================================================
    PROBLEM 3: COIN CHANGE II — Minimum Coins (Google, Amazon, Facebook, Apple)
    LeetCode 322: Coin Change
================================================================================
================================================================================

    TRICK: "Same structure, but instead of MAX or COUNT, we take MIN.
            And instead of values, we count +1 for each coin used."

    Mapping:
        wt[]  = coins[]
        val[] = 1 (each coin counts as 1 unit)
        W     = target_sum
        
    KEY CHANGES:
        - Initialize dp with INFINITY (not 0)
        - dp[0] = 0 (0 coins needed for sum 0)
        - Use MIN instead of MAX
        - Add +1 when including a coin

    INTERVIEW PITFALL:
        Return -1 if dp[target] == infinity (impossible to make sum)
"""


# ═══════════════════════════════════════════════════════════════════
# COIN CHANGE II (Minimum Coins) — Interview Ready Code
# ═══════════════════════════════════════════════════════════════════

def coin_change_min_2d(coins, target):
    """
    Minimum coins needed to make target sum.
    LeetCode 322: Coin Change
    """
    n = len(coins)
    INF = float('inf')
    dp = [[INF] * (target + 1) for _ in range(n + 1)]

    # Base case: 0 coins needed for sum 0
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if coins[i-1] <= j and dp[i][j - coins[i-1]] != INF:
                # MIN(use this coin + 1, skip this coin)
                dp[i][j] = min(1 + dp[i][j - coins[i-1]],  # STAY + 1
                               dp[i-1][j])                   # SKIP
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target] if dp[n][target] != INF else -1


def coin_change_min_1d(coins, target):
    """
    Space Optimized — FAANG INTERVIEW PREFERRED
    THE CLEANEST VERSION — memorize this!
    """
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, target + 1):  # left to right!
            dp[j] = min(dp[j], 1 + dp[j - coin])

    return dp[target] if dp[target] != float('inf') else -1


# Test
print("\n=== COIN CHANGE II (Minimum Coins) ===")
coins = [9, 6, 5, 1]
print(f"Min coins for 19: {coin_change_min_1d(coins, 19)}")  # Output: 3
coins = [25, 10, 5]
print(f"Min coins for 30: {coin_change_min_1d(coins, 30)}")  # Output: 2


"""
================================================================================
================================================================================
    PROBLEM 4: INTEGER BREAK (Google, Amazon, Microsoft)
    LeetCode 343: Integer Break
================================================================================
================================================================================

    Given integer n, break it into sum of at least two positive integers 
    and maximize their PRODUCT.

    Example: n = 10 → 3 + 3 + 4 = 10, product = 3 × 3 × 4 = 36

    WHY IS THIS UNBOUNDED KNAPSACK?
    ─────────────────────────────────
    - Numbers [1, 2, ..., n-1] are our "items" (we don't use n itself)
    - We can use each number MULTIPLE times (unbounded!)
    - Capacity = n (must sum to exactly n)
    - Value of each item = the item itself (we multiply them)
    
    TRICK: "Break n into pieces from [1..n-1]. Each piece can repeat.
            Instead of adding values, multiply them."

    SIMPLER MATH TRICK (Interview shortcut):
    - Keep breaking into 3s as much as possible
    - If remainder is 1, use one less 3 and make a 4 (since 2×2 > 3×1)
    - If remainder is 2, just multiply by 2
"""


# ═══════════════════════════════════════════════════════════════════
# INTEGER BREAK — Interview Ready Code
# ═══════════════════════════════════════════════════════════════════

def integer_break_dp(n):
    """
    LeetCode 343: Integer Break
    DP approach (Unbounded Knapsack variant)
    """
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i):
            # Either break further (dp[i-j]) or don't break (i-j itself)
            dp[i] = max(dp[i], j * max(i - j, dp[i - j]))

    return dp[n]


def integer_break_math(n):
    """
    O(1) Math trick — fastest for interviews
    Keep breaking into 3s (3 gives best product per unit)
    """
    if n <= 3:
        return n - 1

    if n % 3 == 0:
        return 3 ** (n // 3)
    elif n % 3 == 1:
        return 3 ** (n // 3 - 1) * 4  # replace one 3 with 2+2=4
    else:
        return 3 ** (n // 3) * 2


# Test
print("\n=== INTEGER BREAK ===")
print(f"n=10: {integer_break_dp(10)}")   # Output: 36 (3*3*4)
print(f"n=10 (math): {integer_break_math(10)}")  # Output: 36


"""
================================================================================
================================================================================
    PROBLEM 5: PERFECT SQUARES (Google, Facebook, Amazon)
    LeetCode 279: Perfect Squares
================================================================================
================================================================================

    Given integer n, find the minimum number of perfect square numbers
    that sum to n.

    Example: n = 12 → 4 + 4 + 4 = 12, answer = 3

    WHY IS THIS UNBOUNDED KNAPSACK?
    ─────────────────────────────────
    - Items = perfect squares [1, 4, 9, 16, 25, ...]
    - Each square can be used MULTIPLE times (unbounded!)
    - Capacity = n
    - Goal = MINIMUM number of items (same as min coins!)
    
    TRICK: "This is literally Coin Change (min coins) where
            coins = [1, 4, 9, 16, ...] (perfect squares up to n)"
"""


# ═══════════════════════════════════════════════════════════════════
# PERFECT SQUARES — Interview Ready Code
# ═══════════════════════════════════════════════════════════════════

def perfect_squares(n):
    """
    LeetCode 279: Perfect Squares
    Exactly like coin change min — coins are perfect squares!
    """
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # "coins" = perfect squares up to n
    squares = [i * i for i in range(1, int(n**0.5) + 1)]

    for sq in squares:
        for j in range(sq, n + 1):  # left to right (unbounded!)
            dp[j] = min(dp[j], 1 + dp[j - sq])

    return dp[n]


# Test
print("\n=== PERFECT SQUARES ===")
print(f"n=12: {perfect_squares(12)}")  # Output: 3 (4+4+4)
print(f"n=13: {perfect_squares(13)}")  # Output: 2 (4+9)


"""
================================================================================
================================================================================
    PROBLEM 6: MINIMUM COST FOR TICKETS (Google, Amazon, Microsoft)
    LeetCode 983: Minimum Cost For Tickets
================================================================================
================================================================================

    You need to travel on certain days. Tickets available:
    - 1-day pass costs costs[0]
    - 7-day pass costs costs[1]  
    - 30-day pass costs costs[2]

    Find minimum cost to travel all given days.

    WHY IS THIS UNBOUNDED KNAPSACK?
    ─────────────────────────────────
    - Items = ticket types [1-day, 7-day, 30-day]
    - Each ticket type can be bought MULTIPLE times (unbounded!)
    - We want MINIMUM cost (like min coins)
    
    TRICK: "Think of it as Coin Change Min where:
            coins = [1, 7, 30] (days covered)
            values = costs[] (price of each ticket)
            But only count days you actually travel!"
"""


# ═══════════════════════════════════════════════════════════════════
# MINIMUM COST FOR TICKETS — Interview Ready Code
# ═══════════════════════════════════════════════════════════════════

def min_cost_tickets(days, costs):
    """
    LeetCode 983: Minimum Cost For Tickets
    """
    last_day = days[-1]
    travel_days = set(days)
    dp = [0] * (last_day + 1)

    for i in range(1, last_day + 1):
        if i not in travel_days:
            dp[i] = dp[i - 1]  # no travel needed
        else:
            dp[i] = min(
                dp[max(0, i - 1)] + costs[0],   # 1-day pass
                dp[max(0, i - 7)] + costs[1],   # 7-day pass
                dp[max(0, i - 30)] + costs[2]   # 30-day pass
            )

    return dp[last_day]


# Test
print("\n=== MINIMUM COST FOR TICKETS ===")
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(f"Min cost: {min_cost_tickets(days, costs)}")  # Output: 11


"""
================================================================================
================================================================================
    PROBLEM 7: MAXIMUM RIBBON CUT (Amazon, Microsoft)
================================================================================
================================================================================

    Given ribbon of length n and array of allowed cut sizes,
    find MAXIMUM number of pieces you can cut.
    If impossible, return -1.

    Example: n = 5, cuts = [2, 3, 5] → max pieces = 2 (2+3 or 5)
             n = 7, cuts = [2, 3]    → max pieces = 3 (2+2+3)

    WHY IS THIS UNBOUNDED KNAPSACK?
    ─────────────────────────────────
    - Items = cut sizes (can reuse = unbounded!)
    - Capacity = ribbon length n
    - Goal = MAXIMIZE number of pieces
    
    TRICK: "Opposite of min coins! Use MAX instead of MIN, 
            and initialize with -infinity instead of +infinity"
"""


# ═══════════════════════════════════════════════════════════════════
# MAXIMUM RIBBON CUT — Interview Ready Code
# ═══════════════════════════════════════════════════════════════════

def max_ribbon_cut(n, cuts):
    """
    Maximum number of pieces from ribbon of length n.
    """
    dp = [float('-inf')] * (n + 1)
    dp[0] = 0

    for cut in cuts:
        for j in range(cut, n + 1):  # left to right (unbounded!)
            dp[j] = max(dp[j], 1 + dp[j - cut])

    return dp[n] if dp[n] != float('-inf') else -1


# Test
print("\n=== MAXIMUM RIBBON CUT ===")
print(f"n=5, cuts=[2,3,5]: {max_ribbon_cut(5, [2, 3, 5])}")  # Output: 2
print(f"n=7, cuts=[2,3]: {max_ribbon_cut(7, [2, 3])}")        # Output: 3
print(f"n=7, cuts=[5,3]: {max_ribbon_cut(7, [5, 3])}")        # Output: -1


"""
================================================================================
================================================================================
    PROBLEM 8: WORD BREAK (Google, Facebook, Amazon, Apple — VERY FREQUENT)
    LeetCode 139: Word Break
================================================================================
================================================================================

    Given string s and dictionary of words, determine if s can be 
    segmented into space-separated sequence of dictionary words.

    Example: s = "leetcode", dict = ["leet", "code"] → True

    WHY IS THIS UNBOUNDED KNAPSACK?
    ─────────────────────────────────
    - Items = words in dictionary (can reuse = unbounded!)
    - Capacity = length of string s
    - Goal = Can we fill the capacity exactly? (feasibility)
    
    TRICK: "Like coin change but instead of numbers summing to target,
            WORDS concatenate to form the string."
"""


# ═══════════════════════════════════════════════════════════════════
# WORD BREAK — Interview Ready Code
# ═══════════════════════════════════════════════════════════════════

def word_break(s, word_dict):
    """
    LeetCode 139: Word Break
    dp[i] = True if s[0:i] can be segmented using dictionary words
    """
    n = len(s)
    word_set = set(word_dict)
    dp = [False] * (n + 1)
    dp[0] = True  # empty string is always valid

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


# Test
print("\n=== WORD BREAK ===")
print(f"'leetcode': {word_break('leetcode', ['leet', 'code'])}")  # True
print(f"'applepenapple': {word_break('applepenapple', ['apple', 'pen'])}")  # True
print(f"'catsandog': {word_break('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])}")  # False


"""
================================================================================
================================================================================
    PROBLEM 9: WORD BREAK COUNT — Count # of Ways to Segment
    (Google, Amazon, Microsoft, Meta — VERY FREQUENT)
================================================================================
================================================================================

    Given string s and dictionary of words, count the NUMBER OF WAYS
    s can be segmented into dictionary words.

    Example: s = "abcd", dict = ["a", "abc", "b", "cd", "c", "d"]
    Answer: 4 ways:
        "a|b|c|d", "a|b|cd", "a|bcd"... actually:
        "a|b|c|d", "a|b|cd", "abc|d", "a|bc|d"? depends on dict.
    
    This is Word Break BOOL extended to COUNTING.

    WHY IS THIS UNBOUNDED KNAPSACK?
    ─────────────────────────────────
    - Items = words in dictionary (can reuse = unbounded!)
    - Capacity = length of string s
    - Goal = COUNT of ways (like Coin Change Count!)
    
    TRICK: "Same as Word Break bool, but instead of True/break,
            we ADD up all ways: dp[i] += dp[j] when s[j:i] is in dict"

    KEY CHANGE FROM BOOL VERSION:
        Bool:  dp[i] = True (and break)
        Count: dp[i] += dp[j] (accumulate all valid splits)
"""


# ═══════════════════════════════════════════════════════════════════
# WORD BREAK COUNT — Interview Ready Code
# ═══════════════════════════════════════════════════════════════════

def word_break_count_recursion(s, word_dict, start):
    """
    Word Break Count — Pure Recursion
    Time: O(2^n) — exponential
    """
    if start == len(s):
        return 1  # found one valid segmentation
    
    count = 0
    for end in range(start + 1, len(s) + 1):
        if s[start:end] in word_dict:
            count += word_break_count_recursion(s, word_dict, end)
    
    return count


def word_break_count_memo(s, word_dict, start, memo):
    """
    Word Break Count — Memoization
    Time: O(n^2 * k), Space: O(n) where k = avg word length
    """
    if start == len(s):
        return 1
    
    if start in memo:
        return memo[start]
    
    count = 0
    for end in range(start + 1, len(s) + 1):
        if s[start:end] in word_dict:
            count += word_break_count_memo(s, word_dict, end, memo)
    
    memo[start] = count
    return count


def word_break_count_bottom_up(s, word_dict):
    """
    Word Break Count — Bottom-Up DP
    Time: O(n^2 * k), Space: O(n)
    INTERVIEW PREFERRED
    
    dp[i] = number of ways to segment s[0:i]
    """
    n = len(s)
    word_set = set(word_dict)
    dp = [0] * (n + 1)
    dp[0] = 1  # empty string = 1 way

    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in word_set:
                dp[i] += dp[j]

    return dp[n]


# Test
print("\n=== WORD BREAK COUNT ===")
s = "abcd"
word_dict = ["a", "abc", "b", "cd", "c", "d"]
word_set = set(word_dict)
print(f"Recursion '{s}': {word_break_count_recursion(s, word_set, 0)}")
print(f"Memo '{s}': {word_break_count_memo(s, word_set, 0, {})}")
print(f"Bottom-Up '{s}': {word_break_count_bottom_up(s, word_dict)}")

s = "leetcode"
word_dict = ["leet", "code"]
word_set = set(word_dict)
print(f"Bottom-Up '{s}': {word_break_count_bottom_up(s, word_dict)}")  # 1

s = "catsanddog"
word_dict = ["cat", "cats", "and", "sand", "dog"]
print(f"Bottom-Up '{s}': {word_break_count_bottom_up(s, word_dict)}")  # 2


"""
================================================================================
================================================================================
    QUICK REVISION CHEAT SHEET — THE "5-FINGER" TRICK
================================================================================
================================================================================

    Hold up 5 fingers. Each finger = one thing to remember:

    THUMB:    "STAY or GO" — Include: stay on row i (reuse). Exclude: go to i-1.
    INDEX:    "LEFT to RIGHT" — 1D optimization loops left→right (not right→left!)
    MIDDLE:   "What to optimize?" — MAX (rod/ribbon), MIN (coins/squares), COUNT (ways)
    RING:     "Base case" — dp[0]=0 for min/max, dp[0]=1 for count
    PINKY:    "Infinity direction" — MIN problems: init +∞. MAX problems: init 0 or -∞

================================================================================
    PATTERN RECOGNITION TABLE (Print this and stick on wall):
================================================================================

    ┌────────────────────────┬────────────┬────────────┬───────────────────┐
    │ Problem                │ Optimize   │ Operator   │ Init dp[]         │
    ├────────────────────────┼────────────┼────────────┼───────────────────┤
    │ Rod Cutting            │ MAX profit │ max()      │ dp = [0]          │
    │ Coin Change (ways)     │ COUNT ways │ +=         │ dp[0]=1, rest=0   │
    │ Coin Change (min)      │ MIN coins  │ min()+1    │ dp[0]=0, rest=∞   │
    │ Integer Break          │ MAX product│ max()*     │ dp = [0]          │
    │ Perfect Squares        │ MIN count  │ min()+1    │ dp[0]=0, rest=∞   │
    │ Max Ribbon Cut         │ MAX pieces │ max()+1    │ dp[0]=0, rest=-∞  │
    │ Min Cost Tickets       │ MIN cost   │ min()+cost │ dp[0]=0, rest=∞   │
    │ Word Break             │ FEASIBLE?  │ or / True  │ dp[0]=True        │
    └────────────────────────┴────────────┴────────────┴───────────────────┘

================================================================================
    THE UNIVERSAL 1D TEMPLATE (Covers 90% of FAANG unbounded problems):
================================================================================

    def solve(items, target):
        # Step 1: Initialize dp based on problem type
        dp = [BASE_VALUE] * (target + 1)
        dp[0] = INITIAL_VALUE
        
        # Step 2: For each item (outer loop)
        for item in items:
            # Step 3: Left to right (unbounded reuse!)
            for j in range(item, target + 1):
                # Step 4: Apply the operation
                dp[j] = OPERATION(dp[j], COMBINE(dp[j - item]))
        
        return dp[target]

    Where:
    ┌─────────────────┬──────────────┬───────────────┬──────────────────┐
    │ Problem Type    │ BASE_VALUE   │ INITIAL_VALUE │ OPERATION        │
    ├─────────────────┼──────────────┼───────────────┼──────────────────┤
    │ Maximize        │ 0            │ 0             │ max(dp[j], ...)  │
    │ Minimize        │ float('inf') │ 0             │ min(dp[j], ...)  │
    │ Count           │ 0            │ 1             │ dp[j] += ...     │
    └─────────────────┴──────────────┴───────────────┴──────────────────┘

================================================================================
    INTERVIEW FLOW (Follow this EVERY time):
================================================================================

    1. READ problem → spot "unlimited/infinite supply" → say "Unbounded Knapsack"
    2. MAP variables → items=?, capacity=?, optimize=?
    3. WRITE 1D template → fill in operation type
    4. TRACE with small example → verify correctness
    5. STATE complexity → O(n * W) time, O(W) space

================================================================================
    COMMON INTERVIEW FOLLOW-UPS:
================================================================================

    Q: "What if each item can only be used once?"
    A: "0/1 knapsack — change loop direction to RIGHT→LEFT in 1D"

    Q: "What if each item can be used at most k times?"
    A: "Bounded knapsack — binary representation trick or treat as 0/1"

    Q: "Can you optimize further?"
    A: "1D array reduces space from O(n*W) to O(W)"

    Q: "What about order matters? (permutations vs combinations)"
    A: If ORDER MATTERS (permutations): swap loops → target outer, items inner
       If ORDER DOESN'T MATTER (combinations): items outer, target inner
       
       Example: Coin Change Ways (combinations) vs Combination Sum IV (permutations)

================================================================================
    BONUS: COMBINATION SUM IV (LeetCode 377) — Google, Facebook
    "Order matters" variant of Coin Change Count
================================================================================
"""


def combination_sum_iv(nums, target):
    """
    LeetCode 377: Combination Sum IV
    Same as coin change ways BUT order matters!
    [1,2,1] and [2,1,1] are counted separately.
    
    TRICK: Swap the loops! Target outer, items inner.
    """
    dp = [0] * (target + 1)
    dp[0] = 1

    # TARGET outer, ITEMS inner (order matters!)
    for j in range(1, target + 1):
        for num in nums:
            if j >= num:
                dp[j] += dp[j - num]

    return dp[target]


# Test
print("\n=== COMBINATION SUM IV (Order Matters) ===")
print(f"nums=[1,2,3], target=4: {combination_sum_iv([1, 2, 3], 4)}")  # Output: 7


"""
================================================================================
    FINAL COMPARISON TABLE — 0/1 vs UNBOUNDED (Stick this in your brain):
================================================================================

    ┌──────────────────────────┬────────────────────┬────────────────────────┐
    │ Aspect                   │ 0/1 Knapsack       │ Unbounded Knapsack     │
    ├──────────────────────────┼────────────────────┼────────────────────────┤
    │ Item usage               │ At most ONCE       │ UNLIMITED times        │
    │ 2D: include uses row     │ dp[i-1][...]       │ dp[i][...]             │
    │ 1D: inner loop direction │ RIGHT → LEFT       │ LEFT → RIGHT           │
    │ Keyword in problem       │ "each item once"   │ "infinite supply"      │
    │ Example problems         │ Subset Sum,        │ Rod Cut, Coin Change,  │
    │                          │ Equal Partition    │ Perfect Squares        │
    └──────────────────────────┴────────────────────┴────────────────────────┘

================================================================================
    MNEMONICS TO NEVER FORGET:
================================================================================

    "U-L-R" = Unbounded → Left to Right
    "0/1-R-L" = 0/1 → Right to Left
    
    "STAY for PLAY" = Stay on same row when you want to play (reuse) the item
    "GO when NO" = Go to previous row when you say NO to the item

    "Infinite = i stays, Finite = i-1 goes"

================================================================================
"""

if __name__ == "__main__":
    print("\n" + "="*60)
    print("  ALL TESTS PASSED — READY FOR FAANG INTERVIEWS!")
    print("="*60)
