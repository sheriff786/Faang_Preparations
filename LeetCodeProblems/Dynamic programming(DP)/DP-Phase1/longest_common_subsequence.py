'''
================================================================================
================================================================================
    LCS (LONGEST COMMON SUBSEQUENCE) — COMPLETE FAANG INTERVIEW GUIDE
================================================================================
================================================================================

PATTERN: LCS (the MOTHER of all string DP problems)
DIFFICULTY: Medium
FREQUENCY: Very High (Amazon, Google, Microsoft, Meta, Apple)

================================================================================
WHY LCS IS THE #1 STRING DP PATTERN:
================================================================================

    LCS is the foundation for 13+ other DP problems:

    ┌─────────────────────────────────────────────────────────────────┐
    │                         LCS                                     │
    │                          │                                      │
    │    ┌──────┬──────┬───────┼───────┬──────┬──────┬──────┐        │
    │    ▼      ▼      ▼       ▼       ▼      ▼      ▼      ▼       │
    │  Longest Shortest Print  Print  Min    Longest Longest Count   │
    │  Common  Common  LCS    SCS    Insert  Repeat  Palindr Palindr │
    │  Sub-    Super-               &Delete  Subseq  Subseq  Substr  │
    │  string  seq                                                    │
    └─────────────────────────────────────────────────────────────────┘

    Learn LCS ONCE → solve 13 problems automatically.

================================================================================
ALL 14 PROBLEMS BASED ON LCS:
================================================================================

    1)  Longest Common Subsequence (LCS)
    2)  Longest Common Substring
    3)  Print LCS
    4)  Shortest Common Supersequence (SCS)
    5)  Print SCS
    6)  Min # of Insertions & Deletions to convert A→B
    7)  Longest Repeating Subsequence
    8)  Length of longest subsequence of A which is a substring in B
    9)  Subsequence Pattern Matching (is A subsequence of B?)
    10) Count how many times A appears as subsequence in B
    11) Longest Palindromic Subsequence
    12) Longest Palindromic Substring
    13) Count of Palindromic Substrings
    14) Min # of deletions to make a string palindrome
        (= Min # of insertions to make a string palindrome)

================================================================================
TRICK TO IDENTIFY LCS PROBLEMS:
================================================================================

    Ask yourself:
    1. Are there TWO strings (or one string compared to its reverse)?
    2. Am I looking for something COMMON between them?
    3. Does ORDER matter but NOT contiguity? → SUBSEQUENCE
    4. Does ORDER and CONTIGUITY matter? → SUBSTRING

    KEYWORD SPOTTERS:
    ┌────────────────────────────────────────────────────────┐
    │ "subsequence"           → LCS variant                  │
    │ "substring" (contiguous)→ LCS with reset               │
    │ "palindrome"            → compare string with reverse  │
    │ "convert A to B"        → LCS to find common, rest=ops │
    │ "supersequence"         → combine both using LCS       │
    └────────────────────────────────────────────────────────┘

================================================================================
THE CHOICE DIAGRAM (Draw this in EVERY interview):
================================================================================

    For characters X[i-1] and Y[j-1]:

                  Compare X[i-1] vs Y[j-1]
                       /           \\
                      /             \\
              MATCH!                NO MATCH
         X[i-1] == Y[j-1]       X[i-1] != Y[j-1]
              |                    /          \\
              |                   /            \\
         1 + dp[i-1][j-1]    dp[i-1][j]    dp[i][j-1]
         (both move back)    (skip X[i-1]) (skip Y[j-1])
                              take MAX of both

    SUBSEQUENCE: dp[i][j] = max(dp[i-1][j], dp[i][j-1]) on mismatch
    SUBSTRING:   dp[i][j] = 0 on mismatch (RESET — must be contiguous)

================================================================================
BASE CASE TRICK:
================================================================================

    dp[0][j] = 0 for all j  (empty X = 0 common)
    dp[i][0] = 0 for all i  (empty Y = 0 common)

    "If either string is empty, nothing is common"

================================================================================
CONVERSION TABLE — How LCS solves ALL 14 problems:
================================================================================

    ┌──────────────────────────────────┬──────────────────────────────────────┐
    │ Problem                          │ Formula using LCS                    │
    ├──────────────────────────────────┼──────────────────────────────────────┤
    │ LCS length                       │ dp[m][n]                             │
    │ Longest Common Substring         │ max of dp[i][j] (reset on mismatch) │
    │ Shortest Common Supersequence    │ m + n - LCS(X, Y)                   │
    │ Min Insertions + Deletions       │ (m - LCS) + (n - LCS)               │
    │ Longest Palindromic Subsequence  │ LCS(s, reverse(s))                  │
    │ Min Deletions for Palindrome     │ n - LCS(s, reverse(s))              │
    │ Min Insertions for Palindrome    │ n - LCS(s, reverse(s))              │
    │ Longest Repeating Subsequence    │ LCS(s, s) with i != j condition     │
    │ Is A subsequence of B?           │ LCS(A, B) == len(A)                 │
    └──────────────────────────────────┴──────────────────────────────────────┘

================================================================================
LCS vs 0/1 KNAPSACK — Key Difference:
================================================================================

    ┌─────────────────────┬─────────────────────┬──────────────────────┐
    │                     │ 0/1 Knapsack         │ LCS                  │
    ├─────────────────────┼─────────────────────┼──────────────────────┤
    │ What changes?       │ items (n), capacity  │ index i, index j     │
    │ Choice              │ pick or skip item    │ match or skip char   │
    │ On match/pick       │ val + dp[i-1][w-wt]  │ 1 + dp[i-1][j-1]    │
    │ On mismatch/skip    │ dp[i-1][w]           │ max(dp[i-1][j],      │
    │                     │                     │     dp[i][j-1])      │
    │ Base case           │ dp[0][w] = 0         │ dp[0][j] = dp[i][0]=0│
    └─────────────────────┴─────────────────────┴──────────────────────┘

'''

'''
================================================================================
PROBLEM 1: LONGEST COMMON SUBSEQUENCE (LCS) — Amazon, Google, Microsoft
================================================================================

Given two strings X and Y, find the length of the longest common subsequence.
A subsequence is a sequence that can be derived by deleting some characters
without changing the order of remaining characters.

Example:
Input: X = "abcdgh", Y = "abedfhr"
Output: 4
Explanation: "abdh" is the LCS

Input: X = "AGGTAB", Y = "GXTXAYB"
Output: 4
Explanation: "GTAB" is the LCS

choice diagram:

    if X[i-1] == Y[j-1]:
        return 1 + LCS(X, Y, i-1, j-1)    ← both chars match, move both back
    else:
        return max(LCS(X, Y, i, j-1),      ← skip char from Y
                   LCS(X, Y, i-1, j))      ← skip char from X

base condition:
    if n == 0 or m == 0:  ← if either string is empty
        return 0

code variation from knapsack:
    wt[i-1] comparison → X[i-1] == Y[j-1] comparison
    max(pick, skip)    → max(skip_X, skip_Y) on mismatch
    1+dp[i-1][j-1]     → on match (both move diagonally)

[Naive Approach] Using Recursion — O(2^(m+n)) Time, O(m+n) Space


def LCS_recur(X, Y, n, m):

    if n == 0 or m == 0:
        return 0

    if X[n-1] == Y[m-1]:
        return 1 + LCS_recur(X, Y, n-1, m-1)
    else:
        return max(LCS_recur(X, Y, n, m-1),
                   LCS_recur(X, Y, n-1, m))


def lcs_recursion(X, Y):
    return LCS_recur(X, Y, len(X), len(Y))

if __name__ == "__main__":
    X = "abcdgh"
    Y = "abedfhr"
    print(lcs_recursion(X, Y))

Output
4


[Better Approach] Using Top-Down DP (Memoization) — O(m*n) Time, O(m*n) Space

Why memoization? Two changing parameters: n and m
So create dp[n+1][m+1] initialized with -1


def LCS_memo(X, Y, n, m, dp):

    if n == 0 or m == 0:
        return 0

    if dp[n][m] != -1:
        return dp[n][m]

    if X[n-1] == Y[m-1]:
        dp[n][m] = 1 + LCS_memo(X, Y, n-1, m-1, dp)
    else:
        dp[n][m] = max(LCS_memo(X, Y, n, m-1, dp),
                       LCS_memo(X, Y, n-1, m, dp))

    return dp[n][m]


def lcs_memo(X, Y):
    n, m = len(X), len(Y)
    dp = [[-1] * (m+1) for _ in range(n+1)]
    return LCS_memo(X, Y, n, m, dp)

if __name__ == "__main__":
    X = "abcdgh"
    Y = "abedfhr"
    print(lcs_memo(X, Y))

Output
4


[Expected Approach] Using Bottom-Up DP (Tabulation) — O(m*n) Time, O(m*n) Space

First row and first column = 0 (base case)
Fill rest using choice diagram


def lcs_bottomup(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

if __name__ == "__main__":
    X = "abcdgh"
    Y = "abedfhr"
    print(lcs_bottomup(X, Y))

Output
4

'''

'''
================================================================================
PROBLEM 2: LONGEST COMMON SUBSTRING — Amazon, Microsoft
================================================================================

Given two strings X and Y, find the length of the longest CONTIGUOUS
common substring.

Example:
Input: X = "abcde", Y = "abfce"
Output: 2
Explanation: "ab" is the longest common substring

DIFFERENCE from LCS:
    LCS:       on mismatch → max(dp[i-1][j], dp[i][j-1])  (carry forward)
    Substring: on mismatch → dp[i][j] = 0                  (RESET! must be contiguous)

Answer = max value in entire dp table (not dp[n][m])

[Naive Approach] Using Recursion — O(3^(m+n)) Time


def LCSubstr_recur(X, Y, n, m, count):

    if n == 0 or m == 0:
        return count

    if X[n-1] == Y[m-1]:
        count = LCSubstr_recur(X, Y, n-1, m-1, count+1)

    # Also try skipping from either side
    return max(count,
               LCSubstr_recur(X, Y, n, m-1, 0),
               LCSubstr_recur(X, Y, n-1, m, 0))


def lcsubstr_recursion(X, Y):
    return LCSubstr_recur(X, Y, len(X), len(Y), 0)

if __name__ == "__main__":
    X = "abcde"
    Y = "abfce"
    print(lcsubstr_recursion(X, Y))

Output
2


[Better Approach] Using Bottom-Up DP (Tabulation) — O(m*n) Time, O(m*n) Space


def lcsubstr_bottomup(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]
    result = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0    # RESET (must be contiguous)

    return result

if __name__ == "__main__":
    X = "abcde"
    Y = "abfce"
    print(lcsubstr_bottomup(X, Y))

Output
2

'''

'''
================================================================================
PROBLEM 3: PRINT LCS — Amazon, Google
================================================================================

Print the actual LCS string (not just length).
Backtrack through the dp table from dp[n][m] to dp[0][0].

Example:
Input: X = "abcdgh", Y = "abedfhr"
Output: "abdh"

════════════════════════════════════════════════════════════════════════════════
STEP 1: FILL THE DP TABLE (same as LCS length)
════════════════════════════════════════════════════════════════════════════════

Let's use small example: X = "abcde", Y = "ace"

         ""   a   c   e
    ""  [ 0   0   0   0 ]
    a   [ 0   1   1   1 ]
    b   [ 0   1   1   1 ]
    c   [ 0   1   2   2 ]
    d   [ 0   1   2   2 ]
    e   [ 0   1   2   3 ]

    How to fill:
    - First row & first column = 0 (base case: empty string)
    - If X[i-1] == Y[j-1]: dp[i][j] = 1 + dp[i-1][j-1]  (diagonal + 1)
    - Else:                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])  (max of up, left)

    Example fills:
    dp[1][1]: X[0]='a' == Y[0]='a' → 1 + dp[0][0] = 1 + 0 = 1 ✓
    dp[2][1]: X[1]='b' != Y[0]='a' → max(dp[1][1], dp[2][0]) = max(1,0) = 1
    dp[3][2]: X[2]='c' == Y[1]='c' → 1 + dp[2][1] = 1 + 1 = 2 ✓
    dp[5][3]: X[4]='e' == Y[2]='e' → 1 + dp[4][2] = 1 + 2 = 3 ✓

    Answer = dp[5][3] = 3 (LCS length)

════════════════════════════════════════════════════════════════════════════════
STEP 2: BACKTRACK TO PRINT THE LCS STRING
════════════════════════════════════════════════════════════════════════════════

    Start at dp[n][m] = dp[5][3], move towards dp[0][0]

    RULES:
    ┌─────────────────────────────────────────────────────────────────┐
    │ If X[i-1] == Y[j-1]:  → ADD this char to result                │
    │                          move DIAGONAL ↖ (i-1, j-1)            │
    │                                                                 │
    │ Else:                  → DON'T add anything                     │
    │   If dp[i-1][j] > dp[i][j-1]: move UP ↑ (i-1, j)             │
    │   Else:                         move LEFT ← (i, j-1)           │
    └─────────────────────────────────────────────────────────────────┘

    Trace through the table:

         ""   a   c   e
    ""  [ 0   0   0   0 ]
    a   [ 0   1   1   1 ]
    b   [ 0   1   1   1 ]
    c   [ 0   1   2   2 ]
    d   [ 0   1   2   2 ]
    e   [ 0   1   2  *3*]  ← START here (i=5, j=3)

    Step 1: i=5, j=3 → X[4]='e', Y[2]='e' → MATCH! add 'e', move to (4,2)
    Step 2: i=4, j=2 → X[3]='d', Y[1]='c' → NO match
                        dp[3][2]=2 vs dp[4][1]=1 → dp[3][2] bigger → move UP to (3,2)
    Step 3: i=3, j=2 → X[2]='c', Y[1]='c' → MATCH! add 'c', move to (2,1)
    Step 4: i=2, j=1 → X[1]='b', Y[0]='a' → NO match
                        dp[1][1]=1 vs dp[2][0]=0 → dp[1][1] bigger → move UP to (1,1)
    Step 5: i=1, j=1 → X[0]='a', Y[0]='a' → MATCH! add 'a', move to (0,0)
    Step 6: i=0 → STOP (reached boundary)

    Collected (in reverse): ['e', 'c', 'a']
    Reverse it: "ace" ← This is the LCS!

════════════════════════════════════════════════════════════════════════════════
MEMORY TRICK:
════════════════════════════════════════════════════════════════════════════════

    "Match → GRAB the char and go DIAGONAL ↖"
    "No Match → just FOLLOW the bigger number (up or left)"
    "At the end, REVERSE the collected chars"

════════════════════════════════════════════════════════════════════════════════


def print_lcs(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]

    # Step 1: Fill the table
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Step 2: Backtrack from dp[n][m] to find the string
    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            result.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))

if __name__ == "__main__":
    X = "abcdgh"
    Y = "abedfhr"
    print(print_lcs(X, Y))

Output
abdh

'''

'''
================================================================================
PROBLEM 4: SHORTEST COMMON SUPERSEQUENCE (SCS) LENGTH — Amazon, Google
================================================================================

Find the length of the shortest string that has both X and Y as subsequences.

Example:
Input: X = "AGGTAB", Y = "GXTXAYB"
Output: 9

TRICK: SCS = m + n - LCS(X, Y)
    Why? LCS chars appear once (shared), rest appear as-is from both strings.


[Naive Approach] Using Recursion — O(2^(m+n)) Time

SCS length = m + n - LCS. So we just find LCS recursively.


def SCS_recur(X, Y, n, m):
    if n == 0 or m == 0:
        return 0
    if X[n-1] == Y[m-1]:
        return 1 + SCS_recur(X, Y, n-1, m-1)
    else:
        return max(SCS_recur(X, Y, n, m-1),
                   SCS_recur(X, Y, n-1, m))


def scs_length_recur(X, Y):
    lcs = SCS_recur(X, Y, len(X), len(Y))
    return len(X) + len(Y) - lcs

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(scs_length_recur(X, Y))

Output
9


[Better Approach] Using Memoization — O(m*n) Time, O(m*n) Space


def SCS_memo(X, Y, n, m, dp):
    if n == 0 or m == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if X[n-1] == Y[m-1]:
        dp[n][m] = 1 + SCS_memo(X, Y, n-1, m-1, dp)
    else:
        dp[n][m] = max(SCS_memo(X, Y, n, m-1, dp),
                       SCS_memo(X, Y, n-1, m, dp))
    return dp[n][m]


def scs_length_memo(X, Y):
    n, m = len(X), len(Y)
    dp = [[-1] * (m+1) for _ in range(n+1)]
    lcs = SCS_memo(X, Y, n, m, dp)
    return n + m - lcs

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(scs_length_memo(X, Y))

Output
9


[Expected Approach] Using Bottom-Up DP — O(m*n) Time, O(m*n) Space


def scs_length_bottomup(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs_len = dp[n][m]
    return n + m - lcs_len

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(scs_length_bottomup(X, Y))

Output
9

'''

'''
================================================================================
PROBLEM 5: PRINT SHORTEST COMMON SUPERSEQUENCE — Google, Amazon
================================================================================

Print the actual SCS string.

TRICK: Like Print LCS, but:
    - On match: add char once, move diagonal
    - On mismatch: add the char of the direction you move, then move


def print_scs(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            result.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            result.append(X[i-1])
            i -= 1
        else:
            result.append(Y[j-1])
            j -= 1

    while i > 0:
        result.append(X[i-1])
        i -= 1
    while j > 0:
        result.append(Y[j-1])
        j -= 1

    return ''.join(reversed(result))

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(print_scs(X, Y))

Output
AGXGTXAYB

'''

'''
================================================================================
PROBLEM 6: MIN INSERTIONS AND DELETIONS TO CONVERT A → B — Amazon, Microsoft
================================================================================

Given two strings A and B, find minimum operations (insert/delete) to convert A to B.

Example:
Input: A = "heap", B = "pea"
Output: Deletions = 2, Insertions = 1

TRICK:
    Deletions  = len(A) - LCS(A, B)    ← chars in A not in LCS must be deleted
    Insertions = len(B) - LCS(A, B)    ← chars in B not in LCS must be inserted


[Naive Approach] Using Recursion


def minOps_recur(A, B, n, m):
    if n == 0 or m == 0:
        return 0
    if A[n-1] == B[m-1]:
        return 1 + minOps_recur(A, B, n-1, m-1)
    else:
        return max(minOps_recur(A, B, n, m-1),
                   minOps_recur(A, B, n-1, m))


def min_insert_delete_recur(A, B):
    lcs = minOps_recur(A, B, len(A), len(B))
    return len(A) - lcs, len(B) - lcs

if __name__ == "__main__":
    d, i = min_insert_delete_recur("heap", "pea")
    print(f"Deletions: {d}, Insertions: {i}")

Output
Deletions: 2, Insertions: 1


[Better Approach] Using Memoization


def minOps_memo(A, B, n, m, dp):
    if n == 0 or m == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if A[n-1] == B[m-1]:
        dp[n][m] = 1 + minOps_memo(A, B, n-1, m-1, dp)
    else:
        dp[n][m] = max(minOps_memo(A, B, n, m-1, dp),
                       minOps_memo(A, B, n-1, m, dp))
    return dp[n][m]


def min_insert_delete_memo(A, B):
    n, m = len(A), len(B)
    dp = [[-1] * (m+1) for _ in range(n+1)]
    lcs = minOps_memo(A, B, n, m, dp)
    return n - lcs, m - lcs

if __name__ == "__main__":
    d, i = min_insert_delete_memo("heap", "pea")
    print(f"Deletions: {d}, Insertions: {i}")

Output
Deletions: 2, Insertions: 1


[Expected Approach] Using Bottom-Up DP


def min_insert_delete_bottomup(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs_len = dp[n][m]
    deletions = n - lcs_len
    insertions = m - lcs_len
    return deletions, insertions

if __name__ == "__main__":
    A = "heap"
    B = "pea"
    d, i = min_insert_delete_bottomup(A, B)
    print(f"Deletions: {d}, Insertions: {i}")

Output
Deletions: 2, Insertions: 1

'''

'''
================================================================================
PROBLEM 7: LONGEST REPEATING SUBSEQUENCE — Amazon, Google
================================================================================

Find the longest subsequence that appears at least twice in the string.

Example:
Input: s = "aabebcdd"
Output: 3
Explanation: "abd" repeats (indices differ)

TRICK: LCS(s, s) but with condition: i != j
    Same as LCS but characters at DIFFERENT positions must match.


[Naive Approach] Using Recursion


def LRS_recur(s, n, m):
    if n == 0 or m == 0:
        return 0
    if s[n-1] == s[m-1] and n != m:
        return 1 + LRS_recur(s, n-1, m-1)
    else:
        return max(LRS_recur(s, n, m-1),
                   LRS_recur(s, n-1, m))


def lrs_recursion(s):
    n = len(s)
    return LRS_recur(s, n, n)

if __name__ == "__main__":
    print(lrs_recursion("aabebcdd"))

Output
3


[Better Approach] Using Memoization


def LRS_memo(s, n, m, dp):
    if n == 0 or m == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if s[n-1] == s[m-1] and n != m:
        dp[n][m] = 1 + LRS_memo(s, n-1, m-1, dp)
    else:
        dp[n][m] = max(LRS_memo(s, n, m-1, dp),
                       LRS_memo(s, n-1, m, dp))
    return dp[n][m]


def lrs_memo(s):
    n = len(s)
    dp = [[-1] * (n+1) for _ in range(n+1)]
    return LRS_memo(s, n, n, dp)

if __name__ == "__main__":
    print(lrs_memo("aabebcdd"))

Output
3


[Expected Approach] Using Bottom-Up DP


def lrs_bottomup(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][n]

if __name__ == "__main__":
    print(lrs_bottomup("aabebcdd"))

Output
3

'''

'''
================================================================================
PROBLEM 8: SUBSEQUENCE PATTERN MATCHING — Is A subsequence of B?
================================================================================

Check if string A is a subsequence of string B.

Example:
Input: A = "aec", B = "abcde"
Output: False

TRICK: If LCS(A, B) == len(A), then A is a subsequence of B.


[Naive Approach] Using Recursion


def isSubseq_recur(A, B, n, m):
    if n == 0 or m == 0:
        return 0
    if A[n-1] == B[m-1]:
        return 1 + isSubseq_recur(A, B, n-1, m-1)
    else:
        return max(isSubseq_recur(A, B, n, m-1),
                   isSubseq_recur(A, B, n-1, m))


def is_subsequence_recur(A, B):
    lcs = isSubseq_recur(A, B, len(A), len(B))
    return lcs == len(A)

if __name__ == "__main__":
    print(is_subsequence_recur("ace", "abcde"))
    print(is_subsequence_recur("aec", "abcde"))

Output
True
False


[Better Approach] Using Memoization


def isSubseq_memo(A, B, n, m, dp):
    if n == 0 or m == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if A[n-1] == B[m-1]:
        dp[n][m] = 1 + isSubseq_memo(A, B, n-1, m-1, dp)
    else:
        dp[n][m] = max(isSubseq_memo(A, B, n, m-1, dp),
                       isSubseq_memo(A, B, n-1, m, dp))
    return dp[n][m]


def is_subsequence_memo(A, B):
    n, m = len(A), len(B)
    dp = [[-1] * (m+1) for _ in range(n+1)]
    lcs = isSubseq_memo(A, B, n, m, dp)
    return lcs == n

if __name__ == "__main__":
    print(is_subsequence_memo("ace", "abcde"))
    print(is_subsequence_memo("aec", "abcde"))

Output
True
False


[Expected Approach] Using Bottom-Up DP


def is_subsequence_bottomup(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m] == n

if __name__ == "__main__":
    print(is_subsequence_bottomup("ace", "abcde"))
    print(is_subsequence_bottomup("aec", "abcde"))

Output
True
False

'''

'''
================================================================================
PROBLEM 9: COUNT SUBSEQUENCES — How many times A appears in B as subsequence
================================================================================

Count the number of times string A appears as a subsequence in B.

Example:
Input: A = "bag", B = "babgbag"
Output: 5

choice diagram:
    if A[i-1] == B[j-1]:
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                    ↑ use this match  ↑ skip this match (look for more)
    else:
        dp[i][j] = dp[i][j-1]
                    ↑ skip char in B


[Naive Approach] Using Recursion


def countSubseqRecur(A, B, n, m):

    if n == 0:
        return 1
    if m == 0:
        return 0

    if A[n-1] == B[m-1]:
        return countSubseqRecur(A, B, n-1, m-1) + \
               countSubseqRecur(A, B, n, m-1)
    else:
        return countSubseqRecur(A, B, n, m-1)


def count_subseq_recur(A, B):
    return countSubseqRecur(A, B, len(A), len(B))

if __name__ == "__main__":
    print(count_subseq_recur("bag", "babgbag"))

Output
5


[Better Approach] Using Memoization


def countSubseqMemo(A, B, n, m, dp):

    if n == 0:
        return 1
    if m == 0:
        return 0

    if dp[n][m] != -1:
        return dp[n][m]

    if A[n-1] == B[m-1]:
        dp[n][m] = countSubseqMemo(A, B, n-1, m-1, dp) + \
                   countSubseqMemo(A, B, n, m-1, dp)
    else:
        dp[n][m] = countSubseqMemo(A, B, n, m-1, dp)

    return dp[n][m]


def count_subseq_memo(A, B):
    n, m = len(A), len(B)
    dp = [[-1] * (m+1) for _ in range(n+1)]
    return countSubseqMemo(A, B, n, m, dp)

if __name__ == "__main__":
    print(count_subseq_memo("bag", "babgbag"))

Output
5


[Expected Approach] Using Bottom-Up DP


def count_subseq_bottomup(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for j in range(m+1):
        dp[0][j] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]

    return dp[n][m]

if __name__ == "__main__":
    print(count_subseq_bottomup("bag", "babgbag"))

Output
5

'''

'''
================================================================================
PROBLEM 10: LONGEST PALINDROMIC SUBSEQUENCE (LC 516) — Amazon, Google, Meta
================================================================================

Find the length of the longest palindromic subsequence in string s.

Example:
Input: s = "bbbab"
Output: 4
Explanation: "bbbb" is the longest palindromic subsequence

TRICK: LCS(s, reverse(s))
    Palindrome = reads same forwards & backwards
    So longest palindrome subsequence = what's common between s and its reverse


[Naive Approach] Using Recursion


def LPS_recur(s, i, j):

    if i > j:
        return 0
    if i == j:
        return 1

    if s[i] == s[j]:
        return 2 + LPS_recur(s, i+1, j-1)
    else:
        return max(LPS_recur(s, i+1, j),
                   LPS_recur(s, i, j-1))


def lps_recursion(s):
    return LPS_recur(s, 0, len(s)-1)

if __name__ == "__main__":
    print(lps_recursion("bbbab"))

Output
4


[Better Approach] Using Memoization


def LPS_memo(s, i, j, dp):

    if i > j:
        return 0
    if i == j:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    if s[i] == s[j]:
        dp[i][j] = 2 + LPS_memo(s, i+1, j-1, dp)
    else:
        dp[i][j] = max(LPS_memo(s, i+1, j, dp),
                       LPS_memo(s, i, j-1, dp))

    return dp[i][j]


def lps_memo(s):
    n = len(s)
    dp = [[-1] * n for _ in range(n)]
    return LPS_memo(s, 0, n-1, dp)

if __name__ == "__main__":
    print(lps_memo("bbbab"))

Output
4


[Expected Approach] Using Bottom-Up DP (LCS with reverse)


def lps_bottomup(s):
    rev = s[::-1]
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == rev[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][n]

if __name__ == "__main__":
    print(lps_bottomup("bbbab"))

Output
4

'''

'''
================================================================================
PROBLEM 11: MIN DELETIONS TO MAKE STRING PALINDROME — Amazon, Microsoft
================================================================================

Find minimum deletions to make string a palindrome.

Example:
Input: s = "agbcba"
Output: 1
Explanation: Delete 'g' → "abcba" (palindrome)

TRICK: Min deletions = n - LPS(s) = n - LCS(s, reverse(s))
    Keep the longest palindromic subsequence, delete the rest.


[Naive Approach] Using Recursion

Find LPS using recursion, then answer = n - LPS


def minDel_LPS_recur(s, i, j):
    if i > j:
        return 0
    if i == j:
        return 1
    if s[i] == s[j]:
        return 2 + minDel_LPS_recur(s, i+1, j-1)
    else:
        return max(minDel_LPS_recur(s, i+1, j),
                   minDel_LPS_recur(s, i, j-1))


def min_del_palindrome_recur(s):
    lps = minDel_LPS_recur(s, 0, len(s)-1)
    return len(s) - lps

if __name__ == "__main__":
    print(min_del_palindrome_recur("agbcba"))

Output
1


[Better Approach] Using Memoization


def minDel_LPS_memo(s, i, j, dp):
    if i > j:
        return 0
    if i == j:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i] == s[j]:
        dp[i][j] = 2 + minDel_LPS_memo(s, i+1, j-1, dp)
    else:
        dp[i][j] = max(minDel_LPS_memo(s, i+1, j, dp),
                       minDel_LPS_memo(s, i, j-1, dp))
    return dp[i][j]


def min_del_palindrome_memo(s):
    n = len(s)
    dp = [[-1] * n for _ in range(n)]
    lps = minDel_LPS_memo(s, 0, n-1, dp)
    return n - lps

if __name__ == "__main__":
    print(min_del_palindrome_memo("agbcba"))

Output
1


[Expected Approach] Using Bottom-Up DP (LCS with reverse)


def min_del_palindrome_bottomup(s):
    rev = s[::-1]
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == rev[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lps = dp[n][n]
    return n - lps

if __name__ == "__main__":
    print(min_del_palindrome_bottomup("agbcba"))

Output
1

'''

'''
================================================================================
PROBLEM 12: MIN INSERTIONS TO MAKE STRING PALINDROME — Google, Amazon
================================================================================

Find minimum insertions to make string a palindrome.

TRICK: Same as min deletions! Min insertions = n - LCS(s, reverse(s))


[Naive Approach] Using Recursion


def minIns_LPS_recur(s, i, j):
    if i > j:
        return 0
    if i == j:
        return 1
    if s[i] == s[j]:
        return 2 + minIns_LPS_recur(s, i+1, j-1)
    else:
        return max(minIns_LPS_recur(s, i+1, j),
                   minIns_LPS_recur(s, i, j-1))


def min_ins_palindrome_recur(s):
    lps = minIns_LPS_recur(s, 0, len(s)-1)
    return len(s) - lps

if __name__ == "__main__":
    print(min_ins_palindrome_recur("aebcbda"))

Output
2


[Better Approach] Using Memoization


def minIns_LPS_memo(s, i, j, dp):
    if i > j:
        return 0
    if i == j:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i] == s[j]:
        dp[i][j] = 2 + minIns_LPS_memo(s, i+1, j-1, dp)
    else:
        dp[i][j] = max(minIns_LPS_memo(s, i+1, j, dp),
                       minIns_LPS_memo(s, i, j-1, dp))
    return dp[i][j]


def min_ins_palindrome_memo(s):
    n = len(s)
    dp = [[-1] * n for _ in range(n)]
    lps = minIns_LPS_memo(s, 0, n-1, dp)
    return n - lps

if __name__ == "__main__":
    print(min_ins_palindrome_memo("aebcbda"))

Output
2


[Expected Approach] Using Bottom-Up DP (LCS with reverse)


def min_ins_palindrome_bottomup(s):
    rev = s[::-1]
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == rev[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lps = dp[n][n]
    return n - lps

if __name__ == "__main__":
    print(min_ins_palindrome_bottomup("aebcbda"))

Output
2

'''

'''
================================================================================
PROBLEM 13: LONGEST PALINDROMIC SUBSTRING (LC 5) — Amazon, Google, Meta, Apple
================================================================================

Find the longest CONTIGUOUS palindromic substring.

Example:
Input: s = "babad"
Output: "bab" or "aba"

Input: s = "cbbd"
Output: "bb"


[Naive Approach] Using Recursion — Check all substrings O(n^3)


def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def longest_palindrome_substr_recur(s):
    n = len(s)
    result = ""
    for i in range(n):
        for j in range(i, n):
            if isPalindrome(s, i, j) and (j - i + 1) > len(result):
                result = s[i:j+1]
    return result

if __name__ == "__main__":
    print(longest_palindrome_substr_recur("babad"))

Output
bab


[Better Approach] Using DP Table (Memoization style) — O(n^2) Time, O(n^2) Space

dp[i][j] = True if s[i..j] is a palindrome


def longest_palindrome_substr_dp(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    # Every single char is palindrome
    for i in range(n):
        dp[i][i] = True

    # Check length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2

    # Check lengths 3 to n
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length

    return s[start:start + max_len]

if __name__ == "__main__":
    print(longest_palindrome_substr_dp("babad"))

Output
bab


[Expected Approach] Using Expand Around Center — O(n^2) Time, O(1) Space


def longest_palindrome_substr_expand(s):
    n = len(s)
    start, max_len = 0, 1

    def expand(left, right):
        nonlocal start, max_len
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

    for i in range(n):
        expand(i, i)      # odd length
        expand(i, i + 1)  # even length

    return s[start:start + max_len]

if __name__ == "__main__":
    print(longest_palindrome_substr_expand("babad"))

Output
bab

'''

'''
================================================================================
PROBLEM 14: COUNT PALINDROMIC SUBSTRINGS (LC 647) — Amazon, Google, Meta
================================================================================

Count all palindromic substrings in string s.

Example:
Input: s = "aaa"
Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa"

Input: s = "abc"
Output: 3
Explanation: "a", "b", "c"


[Naive Approach] Using Recursion — Check all substrings O(n^3)


def countPalin_recur(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            # check if s[i..j] is palindrome
            left, right = i, j
            is_palin = True
            while left < right:
                if s[left] != s[right]:
                    is_palin = False
                    break
                left += 1
                right -= 1
            if is_palin:
                count += 1
    return count

if __name__ == "__main__":
    print(countPalin_recur("aaa"))

Output
6


[Better Approach] Using DP Table — O(n^2) Time, O(n^2) Space

dp[i][j] = True if s[i..j] is palindrome


def countPalin_dp(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0

    # Every single char is palindrome
    for i in range(n):
        dp[i][i] = True
        count += 1

    # Check length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            count += 1

    # Check lengths 3 to n
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                count += 1

    return count

if __name__ == "__main__":
    print(countPalin_dp("aaa"))

Output
6


[Expected Approach] Using Expand Around Center — O(n^2) Time, O(1) Space


def countPalin_expand(s):
    n = len(s)
    count = 0

    def expand(left, right):
        nonlocal count
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(n):
        expand(i, i)      # odd length
        expand(i, i + 1)  # even length

    return count

if __name__ == "__main__":
    print(countPalin_expand("aaa"))

Output
6

'''

'''
================================================================================
QUICK REVISION — "5-FINGER" TRICK FOR LCS:
================================================================================

    THUMB:    "MATCH → diagonal (i-1,j-1) + 1"
    INDEX:    "MISMATCH → max(up, left) for SUBSEQUENCE, 0 for SUBSTRING"
    MIDDLE:   "Palindrome = LCS(s, reverse(s))"
    RING:     "SCS = m + n - LCS"
    PINKY:    "Min ops = (m - LCS) + (n - LCS)"

================================================================================
FORMULA CHEAT SHEET (memorize these 5 lines):
================================================================================

    LCS length          = dp[m][n]
    Longest Palindrome  = LCS(s, reverse(s))
    SCS length          = m + n - LCS
    Min deletions       = n - LCS(s, reverse(s))
    Min insert+delete   = (m - LCS) + (n - LCS)

'''


# ══════════════════════════════════════════════════════════════════════════════
# RUNNABLE CODE — ALL APPROACHES FOR ALL PROBLEMS
# ══════════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 1: LCS — ALL 3 APPROACHES
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def LCS_recur(X, Y, n, m):
    if n == 0 or m == 0:
        return 0
    if X[n-1] == Y[m-1]:
        return 1 + LCS_recur(X, Y, n-1, m-1)
    else:
        return max(LCS_recur(X, Y, n, m-1),
                   LCS_recur(X, Y, n-1, m))


def lcs_recursion(X, Y):
    return LCS_recur(X, Y, len(X), len(Y))


# Approach 2: Memoization
def LCS_memo(X, Y, n, m, dp):
    if n == 0 or m == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if X[n-1] == Y[m-1]:
        dp[n][m] = 1 + LCS_memo(X, Y, n-1, m-1, dp)
    else:
        dp[n][m] = max(LCS_memo(X, Y, n, m-1, dp),
                       LCS_memo(X, Y, n-1, m, dp))
    return dp[n][m]


def lcs_memo(X, Y):
    n, m = len(X), len(Y)
    dp = [[-1] * (m+1) for _ in range(n+1)]
    return LCS_memo(X, Y, n, m, dp)


# Approach 3: Bottom-Up
def lcs_bottomup(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]


if __name__ == "__main__":
    X = "abcdgh"
    Y = "abedfhr"
    print("=== LCS ===")
    print("Recursion:", lcs_recursion(X, Y))
    print("Memoization:", lcs_memo(X, Y))
    print("Bottom-Up:", lcs_bottomup(X, Y))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 2: LONGEST COMMON SUBSTRING
# ══════════════════════════════════════════════════════════════════════════════

def lcsubstr_bottomup(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]
    result = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0
    return result


if __name__ == "__main__":
    print("\n=== LONGEST COMMON SUBSTRING ===")
    print("Bottom-Up:", lcsubstr_bottomup("abcde", "abfce"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 3: PRINT LCS
# ══════════════════════════════════════════════════════════════════════════════

def print_lcs(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            result.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(result))


if __name__ == "__main__":
    print("\n=== PRINT LCS ===")
    print("LCS string:", print_lcs("abcdgh", "abedfhr"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 4: SCS LENGTH
# ══════════════════════════════════════════════════════════════════════════════

def scs_length(X, Y):
    lcs = lcs_bottomup(X, Y)
    return len(X) + len(Y) - lcs


if __name__ == "__main__":
    print("\n=== SCS LENGTH ===")
    print("SCS length:", scs_length("AGGTAB", "GXTXAYB"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 5: PRINT SCS
# ══════════════════════════════════════════════════════════════════════════════

def print_scs(X, Y):
    n, m = len(X), len(Y)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            result.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            result.append(X[i-1])
            i -= 1
        else:
            result.append(Y[j-1])
            j -= 1
    while i > 0:
        result.append(X[i-1])
        i -= 1
    while j > 0:
        result.append(Y[j-1])
        j -= 1
    return ''.join(reversed(result))


if __name__ == "__main__":
    print("\n=== PRINT SCS ===")
    print("SCS string:", print_scs("AGGTAB", "GXTXAYB"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 6: MIN INSERTIONS & DELETIONS
# ══════════════════════════════════════════════════════════════════════════════

def min_insert_delete(A, B):
    lcs = lcs_bottomup(A, B)
    return len(A) - lcs, len(B) - lcs


if __name__ == "__main__":
    print("\n=== MIN INSERT & DELETE ===")
    d, i = min_insert_delete("heap", "pea")
    print(f"Deletions: {d}, Insertions: {i}")


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 7: LONGEST REPEATING SUBSEQUENCE
# ══════════════════════════════════════════════════════════════════════════════

def longest_repeating_subseq(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]


if __name__ == "__main__":
    print("\n=== LONGEST REPEATING SUBSEQUENCE ===")
    print("LRS:", longest_repeating_subseq("aabebcdd"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 8: SUBSEQUENCE PATTERN MATCHING
# ══════════════════════════════════════════════════════════════════════════════

def is_subsequence(A, B):
    lcs = lcs_bottomup(A, B)
    return lcs == len(A)


if __name__ == "__main__":
    print("\n=== SUBSEQUENCE PATTERN MATCHING ===")
    print("'ace' in 'abcde':", is_subsequence("ace", "abcde"))
    print("'aec' in 'abcde':", is_subsequence("aec", "abcde"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 9: COUNT SUBSEQUENCES — ALL 3 APPROACHES
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def countSubseqRecur(A, B, n, m):
    if n == 0:
        return 1
    if m == 0:
        return 0
    if A[n-1] == B[m-1]:
        return countSubseqRecur(A, B, n-1, m-1) + \
               countSubseqRecur(A, B, n, m-1)
    else:
        return countSubseqRecur(A, B, n, m-1)


def count_subseq_recur(A, B):
    return countSubseqRecur(A, B, len(A), len(B))


# Approach 2: Memoization
def countSubseqMemo(A, B, n, m, dp):
    if n == 0:
        return 1
    if m == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if A[n-1] == B[m-1]:
        dp[n][m] = countSubseqMemo(A, B, n-1, m-1, dp) + \
                   countSubseqMemo(A, B, n, m-1, dp)
    else:
        dp[n][m] = countSubseqMemo(A, B, n, m-1, dp)
    return dp[n][m]


def count_subseq_memo(A, B):
    n, m = len(A), len(B)
    dp = [[-1] * (m+1) for _ in range(n+1)]
    return countSubseqMemo(A, B, n, m, dp)


# Approach 3: Bottom-Up
def count_subseq_bottomup(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for j in range(m+1):
        dp[0][j] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[n][m]


if __name__ == "__main__":
    print("\n=== COUNT SUBSEQUENCES ===")
    print("Recursion:", count_subseq_recur("bag", "babgbag"))
    print("Memoization:", count_subseq_memo("bag", "babgbag"))
    print("Bottom-Up:", count_subseq_bottomup("bag", "babgbag"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 10: LONGEST PALINDROMIC SUBSEQUENCE — ALL 3 APPROACHES
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def LPS_recur(s, i, j):
    if i > j:
        return 0
    if i == j:
        return 1
    if s[i] == s[j]:
        return 2 + LPS_recur(s, i+1, j-1)
    else:
        return max(LPS_recur(s, i+1, j), LPS_recur(s, i, j-1))


def lps_recursion(s):
    return LPS_recur(s, 0, len(s)-1)


# Approach 2: Memoization
def LPS_memo(s, i, j, dp):
    if i > j:
        return 0
    if i == j:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i] == s[j]:
        dp[i][j] = 2 + LPS_memo(s, i+1, j-1, dp)
    else:
        dp[i][j] = max(LPS_memo(s, i+1, j, dp), LPS_memo(s, i, j-1, dp))
    return dp[i][j]


def lps_memo(s):
    n = len(s)
    dp = [[-1] * n for _ in range(n)]
    return LPS_memo(s, 0, n-1, dp)


# Approach 3: Bottom-Up (using LCS with reverse)
def lps_bottomup(s):
    rev = s[::-1]
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == rev[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]


if __name__ == "__main__":
    print("\n=== LONGEST PALINDROMIC SUBSEQUENCE ===")
    print("Recursion:", lps_recursion("bbbab"))
    print("Memoization:", lps_memo("bbbab"))
    print("Bottom-Up:", lps_bottomup("bbbab"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 11: MIN DELETIONS FOR PALINDROME
# ══════════════════════════════════════════════════════════════════════════════

def min_del_palindrome(s):
    return len(s) - lps_bottomup(s)


if __name__ == "__main__":
    print("\n=== MIN DELETIONS FOR PALINDROME ===")
    print("Min deletions:", min_del_palindrome("agbcba"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 12: MIN INSERTIONS FOR PALINDROME
# ══════════════════════════════════════════════════════════════════════════════

def min_ins_palindrome(s):
    return len(s) - lps_bottomup(s)


if __name__ == "__main__":
    print("\n=== MIN INSERTIONS FOR PALINDROME ===")
    print("Min insertions:", min_ins_palindrome("aebcbda"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 13: LONGEST PALINDROMIC SUBSTRING (LC 5)
# ══════════════════════════════════════════════════════════════════════════════

def longest_palindrome_substring(s):
    n = len(s)
    start, max_len = 0, 1

    def expand(left, right):
        nonlocal start, max_len
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

    for i in range(n):
        expand(i, i)
        expand(i, i + 1)

    return s[start:start + max_len]


if __name__ == "__main__":
    print("\n=== LONGEST PALINDROMIC SUBSTRING ===")
    print("Longest:", longest_palindrome_substring("babad"))


# ══════════════════════════════════════════════════════════════════════════════
# PROBLEM 14: COUNT PALINDROMIC SUBSTRINGS (LC 647)
# ══════════════════════════════════════════════════════════════════════════════

def count_palindrome_substrings(s):
    n = len(s)
    count = 0

    def expand(left, right):
        nonlocal count
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(n):
        expand(i, i)
        expand(i, i + 1)

    return count


if __name__ == "__main__":
    print("\n=== COUNT PALINDROMIC SUBSTRINGS ===")
    print("Count:", count_palindrome_substrings("aaa"))


'''
================================================================================
================================================================================
    PROBLEM 15: LEVENSHTEIN DISTANCE / EDIT DISTANCE (LC 72 — Hard)
    (Google, Amazon, Microsoft, Meta, Apple — VERY FREQUENT)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given two strings word1 and word2, find the minimum number of operations
    to convert word1 into word2. Allowed operations:
        1. INSERT a character
        2. DELETE a character
        3. REPLACE a character

    Example:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: horse → rorse (replace h→r) → rose (delete r) → ros (delete e)

WHY IS THIS AN LCS VARIANT?
    Edit Distance is the INVERSE of LCS — instead of "what's common,"
    we ask "what must change."
    
    RELATIONSHIP: edit_distance ≥ max(m, n) - LCS(word1, word2)
    But Edit Distance also allows REPLACE (which LCS doesn't model directly),
    so it needs its own DP formulation.

IDENTIFICATION TRICK:
    "convert string A to B" + "insert/delete/replace" → Edit Distance
    "minimum operations" + "two strings" → Edit Distance
    "spell check", "autocorrect", "string similarity" → Edit Distance

================================================================================
THE CHOICE DIAGRAM:
================================================================================

    Compare word1[i-1] vs word2[j-1]:

                  word1[i-1] vs word2[j-1]
                       /           \\
                      /             \\
              MATCH!                NO MATCH
              (free!)           pick MIN of 3 operations:
                |                 /       |       \\
                |                /        |        \\
         dp[i-1][j-1]     INSERT     DELETE    REPLACE
         (0 cost,         dp[i][j-1]  dp[i-1][j]  dp[i-1][j-1]
          both advance)      +1          +1          +1

    MATCH:     dp[i][j] = dp[i-1][j-1]  (no operation needed)
    NO MATCH:  dp[i][j] = 1 + min(dp[i][j-1],      ← INSERT into word1
                                   dp[i-1][j],      ← DELETE from word1
                                   dp[i-1][j-1])    ← REPLACE in word1

MEMORY TRICK FOR THE 3 OPERATIONS:
    dp[i][j-1]   = INSERT  → "I added a char to word1, now match word2[j-1]"
                              word1 stays at i, word2 moves back to j-1
    dp[i-1][j]   = DELETE  → "I deleted word1[i-1], try next char"
                              word1 moves back to i-1, word2 stays at j
    dp[i-1][j-1] = REPLACE → "I replaced word1[i-1] with word2[j-1]"
                              both move back

BASE CASES:
    dp[i][0] = i  (delete all i chars from word1 to get empty string)
    dp[0][j] = j  (insert all j chars to build word2 from empty string)

COMPARISON WITH LCS:
    ┌─────────────────────┬────────────────────┬──────────────────────┐
    │                     │ LCS                 │ Edit Distance        │
    ├─────────────────────┼────────────────────┼──────────────────────┤
    │ On match            │ 1 + dp[i-1][j-1]   │ dp[i-1][j-1] (free)  │
    │ On mismatch         │ max(up, left)       │ 1 + min(up,left,diag)│
    │ Base case           │ dp[i][0]=dp[0][j]=0 │ dp[i][0]=i, dp[0][j]=j│
    │ Optimize            │ MAXIMIZE             │ MINIMIZE             │
    └─────────────────────┴────────────────────┴──────────────────────┘

================================================================================
APPROACH 1: RECURSION
================================================================================
'''


def edit_distance_recursion(word1, word2, m, n):
    """
    Edit Distance — Pure Recursion
    Time: O(3^(m+n)) — exponential
    Space: O(m+n) — recursion stack
    """
    if m == 0:
        return n  # insert n chars
    if n == 0:
        return m  # delete m chars
    
    if word1[m - 1] == word2[n - 1]:
        return edit_distance_recursion(word1, word2, m - 1, n - 1)
    else:
        insert = edit_distance_recursion(word1, word2, m, n - 1)
        delete = edit_distance_recursion(word1, word2, m - 1, n)
        replace = edit_distance_recursion(word1, word2, m - 1, n - 1)
        return 1 + min(insert, delete, replace)


'''
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================

    WHAT CHANGES? → m and n (lengths of remaining substrings)
    Memo: dp[m+1][n+1] initialized to -1
'''


def edit_distance_memo(word1, word2, m, n, dp):
    """
    Edit Distance with Memoization
    Time: O(m*n), Space: O(m*n)
    """
    if m == 0:
        return n
    if n == 0:
        return m
    
    if dp[m][n] != -1:
        return dp[m][n]
    
    if word1[m - 1] == word2[n - 1]:
        dp[m][n] = edit_distance_memo(word1, word2, m - 1, n - 1, dp)
    else:
        insert = edit_distance_memo(word1, word2, m, n - 1, dp)
        delete = edit_distance_memo(word1, word2, m - 1, n, dp)
        replace = edit_distance_memo(word1, word2, m - 1, n - 1, dp)
        dp[m][n] = 1 + min(insert, delete, replace)
    
    return dp[m][n]


'''
================================================================================
APPROACH 3: BOTTOM-UP (Tabulation)
================================================================================

    dp[i][j] = min operations to convert word1[0..i-1] to word2[0..j-1]
================================================================================
DP TABLE TRACE for word1 = "horse", word2 = "ros":
================================================================================

         ""   r   o   s
    ""  [ 0   1   2   3 ]  ← insert j chars
    h   [ 1   1   2   3 ]
    o   [ 2   2   1   2 ]
    r   [ 3   2   2   2 ]
    s   [ 4   3   3   2 ]
    e   [ 5   4   4   3 ]

    Answer: dp[5][3] = 3

    HOW TO READ:
    dp[1][1]=1: "h"→"r" = 1 replace
    dp[2][2]=1: "ho"→"ro" = 1 replace (h→r, o matches)
    dp[5][3]=3: "horse"→"ros" = 3 operations
'''


def edit_distance_bottom_up(word1, word2):
    """
    Edit Distance — Bottom-Up DP
    Time: O(m*n), Space: O(m*n)
    INTERVIEW PREFERRED
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # delete i chars
    for j in range(n + 1):
        dp[0][j] = j  # insert j chars
    
    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # match: free
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],      # insert
                                   dp[i - 1][j],      # delete
                                   dp[i - 1][j - 1])  # replace
    
    return dp[m][n]


def edit_distance_space_optimized(word1, word2):
    """
    Edit Distance — Space Optimized O(n)
    Only need previous row + current row
    """
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))
    
    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(curr[j - 1], prev[j], prev[j - 1])
        prev = curr
    
    return prev[n]


if __name__ == "__main__":
    print("\n=== LEVENSHTEIN DISTANCE (EDIT DISTANCE) ===")
    w1, w2 = "horse", "ros"
    print(f"Recursion ('{w1}','{w2}'): {edit_distance_recursion(w1, w2, len(w1), len(w2))}")
    dp = [[-1] * (len(w2) + 1) for _ in range(len(w1) + 1)]
    print(f"Memo ('{w1}','{w2}'): {edit_distance_memo(w1, w2, len(w1), len(w2), dp)}")
    print(f"Bottom-Up ('{w1}','{w2}'): {edit_distance_bottom_up(w1, w2)}")
    print(f"Space-Opt ('{w1}','{w2}'): {edit_distance_space_optimized(w1, w2)}")
    w1, w2 = "intention", "execution"
    print(f"Bottom-Up ('{w1}','{w2}'): {edit_distance_bottom_up(w1, w2)}")  # 5


'''
================================================================================
EDIT DISTANCE — INTERVIEW TRICKS:
================================================================================

    TRICK 1: Base case is NOT 0! dp[i][0]=i, dp[0][j]=j
             (converting to/from empty string costs i or j operations)
    
    TRICK 2: Match = FREE (dp[i-1][j-1], no +1)
             Mismatch = 1 + min(3 choices)
    
    TRICK 3: Space optimize: only need 2 rows (previous + current)
    
    TRICK 4: To PRINT the operations, backtrack through dp table:
             - Came from diagonal (same val) → match, no op
             - Came from diagonal + 1 → replace
             - Came from left + 1 → insert
             - Came from above + 1 → delete

    TRICK 5: If only INSERT and DELETE allowed (no REPLACE):
             edit_distance = m + n - 2 * LCS(word1, word2)
             (This reduces to the min-insertions-deletions problem!)

    COMPANIES: Google, Amazon, Microsoft, Meta, Apple, Goldman Sachs
================================================================================
'''


'''
================================================================================
================================================================================
    PROBLEM 16: INTERLEAVING STRINGS (LC 97 — Medium)
    (Google, Amazon, Microsoft, Meta)
================================================================================
================================================================================

PROBLEM IN 10 SECONDS:
    Given strings s1, s2, s3, determine if s3 is formed by interleaving s1 & s2.
    
    Interleaving = merge s1 and s2 character by character, maintaining relative
    order of each string.

    Example:
    s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"  → True
    s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"  → False

WHY IS THIS AN LCS VARIANT?
    Like LCS, we compare characters from TWO strings.
    But instead of finding what's common, we check if both strings
    can MERGE to form the third string.

IDENTIFICATION TRICK:
    "interleave two strings" + "maintain relative order" → 2-string DP
    "form string s3 from s1 and s2" → Interleaving Strings

KEY INSIGHT:
    dp[i][j] = can s1[0..i-1] and s2[0..j-1] interleave to form s3[0..i+j-1]?
    
    At each position in s3, the character must come from either s1 or s2.
    If s3[i+j-1] == s1[i-1] → it came from s1 → check dp[i-1][j]
    If s3[i+j-1] == s2[j-1] → it came from s2 → check dp[i][j-1]

BASE CASES:
    dp[0][0] = True (both empty → s3 empty)
    dp[i][0] = dp[i-1][0] AND s1[i-1] == s3[i-1]  (only using s1)
    dp[0][j] = dp[0][j-1] AND s2[j-1] == s3[j-1]  (only using s2)

QUICK CHECK: if len(s1) + len(s2) != len(s3) → False immediately

================================================================================
APPROACH 1: RECURSION
================================================================================
'''


def interleave_recursion(s1, s2, s3, i, j, k):
    """
    Interleaving Strings — Pure Recursion
    Time: O(2^(m+n)) — exponential
    """
    if i == len(s1) and j == len(s2) and k == len(s3):
        return True
    if k == len(s3):
        return False
    
    take_s1 = (i < len(s1) and s1[i] == s3[k] and 
               interleave_recursion(s1, s2, s3, i + 1, j, k + 1))
    take_s2 = (j < len(s2) and s2[j] == s3[k] and 
               interleave_recursion(s1, s2, s3, i, j + 1, k + 1))
    
    return take_s1 or take_s2


'''
================================================================================
APPROACH 2: MEMOIZATION (Top-Down)
================================================================================

    WHAT CHANGES? → i and j (k = i + j, so only 2 variables needed!)
'''


def interleave_memo(s1, s2, s3, i, j, memo):
    """
    Interleaving Strings with Memoization
    Time: O(m*n), Space: O(m*n)
    """
    if i == len(s1) and j == len(s2):
        return True
    
    if (i, j) in memo:
        return memo[(i, j)]
    
    k = i + j  # position in s3
    
    take_s1 = (i < len(s1) and s1[i] == s3[k] and 
               interleave_memo(s1, s2, s3, i + 1, j, memo))
    take_s2 = (j < len(s2) and s2[j] == s3[k] and 
               interleave_memo(s1, s2, s3, i, j + 1, memo))
    
    memo[(i, j)] = take_s1 or take_s2
    return memo[(i, j)]


'''
================================================================================
APPROACH 3: BOTTOM-UP (Tabulation)
================================================================================

    dp[i][j] = can s1[0..i-1] and s2[0..j-1] form s3[0..i+j-1]?
================================================================================
DP TABLE TRACE for s1="aab", s2="axy", s3="aaxaby":
================================================================================

         ""    a    x    y
    ""  [ T    T    T    F ]
    a   [ T    T    T    T ]
    a   [ T    T    F    T ]
    b   [ F    F    F    T ]

    Answer: dp[3][3] = True ✓
    s3 = "aaxaby" is interleaving of "aab" and "axy"
'''


def interleave_bottom_up(s1, s2, s3):
    """
    Interleaving Strings — Bottom-Up DP
    Time: O(m*n), Space: O(m*n)
    INTERVIEW PREFERRED
    """
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    dp[0][0] = True
    
    # First column: only s1
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
    
    # First row: only s2
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
    
    # Fill rest
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            k = i + j - 1  # position in s3
            dp[i][j] = ((dp[i - 1][j] and s1[i - 1] == s3[k]) or
                        (dp[i][j - 1] and s2[j - 1] == s3[k]))
    
    return dp[m][n]


def interleave_space_optimized(s1, s2, s3):
    """
    Space Optimized — O(n) space
    """
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    
    dp = [False] * (n + 1)
    
    for i in range(m + 1):
        for j in range(n + 1):
            k = i + j - 1
            if i == 0 and j == 0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j - 1] and s2[j - 1] == s3[k]
            elif j == 0:
                dp[j] = dp[j] and s1[i - 1] == s3[k]
            else:
                dp[j] = ((dp[j] and s1[i - 1] == s3[k]) or
                         (dp[j - 1] and s2[j - 1] == s3[k]))
    
    return dp[n]


if __name__ == "__main__":
    print("\n=== INTERLEAVING STRINGS ===")
    s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
    print(f"Recursion: {interleave_recursion(s1, s2, s3, 0, 0, 0)}")  # True
    print(f"Memo: {interleave_memo(s1, s2, s3, 0, 0, {})}")  # True
    print(f"Bottom-Up: {interleave_bottom_up(s1, s2, s3)}")  # True
    print(f"Space-Opt: {interleave_space_optimized(s1, s2, s3)}")  # True
    s3 = "aadbbbaccc"
    print(f"Bottom-Up (False case): {interleave_bottom_up(s1, s2, s3)}")  # False


'''
================================================================================
INTERLEAVING STRINGS — INTERVIEW TRICKS:
================================================================================

    TRICK 1: k = i + j, so you DON'T need a 3rd variable!
             dp is 2D (m×n), not 3D.
    
    TRICK 2: Quick reject: if len(s1) + len(s2) != len(s3) → False
    
    TRICK 3: dp[i][j] is OR of two choices:
             - s3[k] came from s1 → check dp[i-1][j] AND s1[i-1]==s3[k]
             - s3[k] came from s2 → check dp[i][j-1] AND s2[j-1]==s3[k]
    
    TRICK 4: Space optimize to O(min(m,n)) — only need 1 row

    COMPANIES: Google, Amazon, Microsoft, Meta, Uber
================================================================================

================================================================================
UPDATED CONVERSION TABLE — LCS FAMILY (now 16 problems):
================================================================================

    ┌──────────────────────────────────┬──────────────────────────────────────┐
    │ Problem                          │ Formula / Approach                   │
    ├──────────────────────────────────┼──────────────────────────────────────┤
    │ 1. LCS length                    │ dp[m][n]                             │
    │ 2. Longest Common Substring      │ max of dp[i][j] (reset on mismatch) │
    │ 3. Print LCS                     │ backtrack through dp table           │
    │ 4. SCS length                    │ m + n - LCS(X, Y)                   │
    │ 5. Print SCS                     │ backtrack, add non-LCS chars too    │
    │ 6. Min Insert + Delete           │ (m - LCS) + (n - LCS)               │
    │ 7. Longest Repeating Subseq      │ LCS(s, s) with i != j               │
    │ 8. Is A subsequence of B?        │ LCS(A, B) == len(A)                 │
    │ 9. Count subsequences            │ dp + on match, carry on mismatch   │
    │ 10. Longest Palindromic Subseq   │ LCS(s, reverse(s))                  │
    │ 11. Min deletions palindrome     │ n - LCS(s, reverse(s))              │
    │ 12. Min insertions palindrome    │ n - LCS(s, reverse(s))              │
    │ 13. Longest Palindromic Substr   │ expand around center O(n²)          │
    │ 14. Count Palindromic Substrs    │ expand around center O(n²)          │
    │ 15. Levenshtein/Edit Distance    │ 1 + min(insert, delete, replace)    │
    │ 16. Interleaving Strings         │ dp[i][j] = OR(from s1, from s2)     │
    └──────────────────────────────────┴──────────────────────────────────────┘

================================================================================
'''