def min_coins(coins, value):

    n = len(coins)
    INF = float('inf')

    t = [[0]*(value+1) for _ in range(n+1)]

    # First row
    for j in range(1,value+1):
        t[0][j] = INF

    # Second row
    for j in range(1,value+1):

        if j % coins[0] == 0:
            t[1][j] = j // coins[0]
        else:
            t[1][j] = INF

    # Fill remaining table
    for i in range(2,n+1):

        for j in range(1,value+1):

            if coins[i-1] <= j:

                t[i][j] = min(
                    1 + t[i][j-coins[i-1]],
                    t[i-1][j]
                )

            else:

                t[i][j] = t[i-1][j]

    return t[n][value]



def can_reach_last_house(maximum_jump_lengths):
    """
    Args:
     maximum_jump_lengths(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    n = len(arr)
    return 1 if canReach(0, arr, n) else 0


def canReach(i, arr, n):

    # Base Case
    if i >= n - 1:
        return True

    # Try all possible jumps
    for jump in range(1, arr[i] + 1):

        if canReach(i + jump, arr, n):
            return True

    return False


#memorization

def canReach(i, arr, n, dp):
    
    # Base Case: reached or crossed last index
    if i >= n - 1:
        return True

    # Already computed
    if dp[i] != -1:
        return dp[i]

    # Try all possible jumps
    for jump in range(1, arr[i] + 1):
        if canReach(i + jump, arr, n, dp):
            dp[i] = True
            return True

    dp[i] = False
    return False


def jump_game(arr):
    n = len(arr)

    # -1 = not computed
    dp = [-1] * n

    return 1 if canReach(0, arr, n, dp) else 0


# Test
arr = [2, 3, 1, 0, 4, 7]
print(jump_game(arr))  # Output: 1

arr = [3, 1, 1, 0, 2, 4]
print(jump_game(arr))  # Output: 0


#Now adding bottom up with forloop

def jump_game(arr):

    n = len(arr)

    dp = [False] * n

    # Base case
    dp[n - 1] = True

    # Fill from right to left
    for i in range(n - 2, -1, -1):

        for jump in range(1, arr[i] + 1):

            if i + jump < n and dp[i + jump]:
                dp[i] = True
                break

    return 1 if dp[0] else 0


# Test
arr = [2, 3, 1, 0, 4, 7]
print(jump_game(arr))