'''
Unbunded Knapsack

diffrenece in 0-1 knapsack and unbounded knapsack

problems 

1)Rod cutting
2)coin change
3)coin change 2
4)maximum ribbon cut

unbounded take multiple occurances 

if i say no for 1 item then i say noit processed and if i say yes than we can take multiple occurances

diffrence in matrix wise 

diffrence in code wise

if(wt[i-1]<=j)
    t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
else:
    t[i]=t[i-1][j]
    
unbounded kanpsack

if(wt[i-1]<=j)
    t[i][j] = max(val[i-1]+t[i][j-wt[i-1]],t[i-1][j])
else:
    t[i]=t[i-1][j]


minor changes

'''

'''

Rod cutting

approach flow:
1.probem statements
2.marketing
3.How to identify 0-1 or unbounded
4.code variiation if any


Rod Cutting
Last Updated :
9 Mar, 2026
Given a rod of length n and an array price[]. price[i] denotes the price of a piece of length i. Determine the maximum amount obtained by cutting the rod into pieces and selling the pieces.

Note: price[0] is always 0.

Input: price[] =  [0, 1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation:  The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5 + 17 = 22.

Input : price[] =  [0, 3, 5, 8, 9, 10, 17, 17, 20]
Output : 24
Explanation : The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1]= 8*3 = 24.

Input : price[] =  [0, 3]
Output : 3
Explanation: There is only 1 way to pick a piece of length 1.

Try It Yourself
redirect icon
Table of Content

Using Recursion - O(2^n) Time and O(n) Space
Using the idea of Unbounded Knapsack - O(n^2) time and O(n^2) space
Using Top-Down DP (Memoization) - O(n^2) Time and O(n) Space
Using Bottom-Up DP (Tabulation) - O(n^2) Time and O(n) Space
Using Recursion - O(2^n) Time and O(n) Space
For a rod of length i, try all possible cuts j (1 ≤ j ≤ i).
For each cut, add the price of length j with the best profit of remaining rod (i − j).
Take the maximum profit among all possible cuts.




def cutRodRecur(i, price):
​
    # Base case
    if i == 0:
        return 0
​
    ans = 0
​
    # Find maximum value for rod of length i
    # by considering each cut of length j 
    # such that j <= i
    for j in range(1, i + 1):
        ans = max(ans, price[j] + cutRodRecur(i - j, price))
​
    return ans
​
​
def cutRod(price):
    n = len(price) - 1
​
    return cutRodRecur(n, price)
​
if __name__ == "__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    print(cutRod(price))

Output
22
Using the idea of Unbounded Knapsack - O(n^2) time and O(n^2) space
This problem can be treated like an Unbounded Knapsack, where each cut length can be used multiple times.
For each cut length, we have two choices: take the cut (if it fits) or skip it.
We choose the maximum profit from these choices to get the best way to cut the rod.




# i - length of current rod
# j - remaining rod length
def cutRodRecur(i, j, price, dp):
​
    # base case 
    if i == 0 or j == 0:
        return 0
​
    # If value is stored in dp array
    if dp[i][j] != -1:
        return dp[i][j]
​
    # There are two options:
    # 1. Break it into (i) and (i-j) rods and 
    # take value of ith rod.
    take = 0
    if i <= j:
        take = price[i] + cutRodRecur(i, j - i, price, dp)
​
    # 2. Skip i'th length rod.
    noTake = cutRodRecur(i - 1, j, price, dp)
​
    dp[i][j] = max(take, noTake)
    return dp[i][j]
​
​
def cutRod(price):
    n = len(price) - 1
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
​
    return cutRodRecur(n, n, price, dp)
​
​
if __name__ == "__main__":
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    print(cutRod(price))

Output
22
Using Top-Down DP (Memoization) - O(n^2) Time and O(n) Space
In recursion, the same rod lengths are solved multiple times.
Since there are only n possible rod lengths, we store their results in a DP array.
If a result is already stored, we reuse it instead of recomputing, improving efficiency.




def cutRodRecur(i, price, dp):
​
    # Base case
    if i == 0:
        return 0
​
    # If answer for this dp 
    # state is already calculated
    if dp[i] != -1:
        return dp[i]
​
    ans = 0
​
    # Find maximum value for each cut.
    # Take value of rod of length j, and 
    # recursively find value of rod of 
    # length (i-j).
    for j in range(1, i + 1):
        ans = max(ans, price[j] + cutRodRecur(i - j, price, dp))
​
    dp[i] = ans
    return ans
​
​
def cutRod(price):
    n = len(price) - 1
    dp = [-1] * (n + 1)
    return cutRodRecur(n, price, dp)
​
if __name__ == "__main__":
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    print(cutRod(price))

Output
22
Using Bottom-Up DP (Tabulation) - O(n^2) Time and O(n) Space
We compute the maximum profit starting from smaller rod lengths and move to larger ones.
For a rod of length i, we try all cuts j and (i − j).
Since smaller lengths are already solved, we reuse their results to fill the DP table.




def cutRod(price):
    n = len(price) - 1
    dp = [0] * (n + 1)
​
    # Find maximum value for all 
    # rod of length i.
    for i in range(1, n + 1):
​
        # dividing rod of length i 
        # into smaller piecess recursively
        for j in range(1, i + 1):
            dp[i] = max(dp[i], price[j] + dp[i - j])
​
    return dp[n]
​
if __name__ == "__main__":
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    print(cutRod(price))

Output
22
'''

'''
ROD CUTTING

how to recognize it is unbounded or 0-1

'''
length=[1,2,3,4,5,6,7,8]
price=[1,5,8,9,10,17,17,20]
#profit should be maximum

#code variation
# wt--->length[]
# val--->price
# w--->N

# #code
# if(length[i-1]):
#     t[i][j]=max(price[i-1]+t[i][j-length[i-1]],t[i-1][j])
# else:
#     t[i][j]=t[i-1][j]
    
#     #unbounded knapsack

'''
Coin Change problem -1 maximum # of ways

coin=[1,2,3]
sum=5

coins are unlimited 
1)problem statment

2+3=5
1+2+2=5
1+1+3=5
1+1+1+1+1=5
1+1+1+2=5

why it is knapsack we are getting the choices 

Coin Change - Count Ways to Make Sum
Last Updated :
24 Jan, 2026
Given an integer array coins[ ] representing different denominations of currency and an integer sum. We need to find the number of ways we can make sum by using different combinations from coins[ ]. 
Note: Assume that we have an infinite supply of each type of coin. Therefore, we can use any coin as many times as we want.

Examples: 

Input: sum = 4, coins[] = [1, 2, 3]
Output: 4
Explanation: There are four solutions: [1, 1, 1, 1], [1, 1, 2], [2, 2] and [1, 3]

Input: sum = 10, coins[] = [2, 5, 3, 6]
Output: 5
Explanation: There are five solutions: 
[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5] and [5, 5]

Try It Yourself
redirect icon
Table of Content

[Naive Approach] Using Recursion - O(2^sum) time and O(sum) space
[Better Approach 1] Using Top-Down DP (Memoization) - O(sum*n) time and O(sum*n) space
[Better Approach 2] Using Bottom-Up DP (Tabulation) – O(sum*n) time and O(sum*n) space
[Expected Approach] Using Space Optimized DP – O(sum*n) time and O(sum) space
[Naive Approach] Using Recursion - O(2^sum) time and O(sum) space
To solve this problem initially, we use recursion because at every step we have a choice: either we include the current coin or we do not include it.

For each coin, there are two possibilities:

Include the current coin
If we pick the current coin, then its value reduces the remaining target sum. Because coins are available in infinite supply, we can include the same coin again.
So the recursive call becomes: count(coins, n, sum - coins[n-1])
Exclude the current coin
If we decide not to pick the current coin, then we move to the previous coin while keeping the target sum unchanged.
So the recursive call becomes: count(coins, n-1, sum)
Since we are looking for all different combinations that form the given sum, the final answer will be the sum of both possibilities (include + exclude).

coin---------change_________





def countRecur(coins, n, sum):
    
    # If sum is 0 then there is 1 solution
    if sum == 0:
        return 1
​
    if sum < 0 or n == 0:
        return 0
​
    # count is sum of solutions
    # (i) including coins[n-1] (ii) excluding coins[n-1]
    return countRecur(coins, n, sum - coins[n - 1]) + \
           countRecur(coins, n - 1, sum)
​
​
def count(coins, sum):
    return countRecur(coins, len(coins), sum)
    
↔​

Output
5
[Expected Approach 1] Using Top-Down DP (Memoization) - O(sum*n) time and O(sum*n) space
In the previous recursive approach, we observed that many subproblems are solved repeatedly. This repetition increases time complexity. To handle this, we use Memoization.

We create a DP table of size n × (sum + 1), because the result of the recursion depends on two changing parameters: the number of coins considered and the remaining target sum So whenever we compute a subproblem count(i, sum), we store the result in the DP table. Next time when the same subproblem appears, instead of computing it again, we directly fetch it from the DP table, which saves a lot of time.






def countRecur(coins, n, sum, dp):
​
    # If sum is 0 then there is 1 solution
    if sum == 0: 
        return 1
​
    if sum < 0 or n == 0:
        return 0
​
    # If the subproblem is previously calculated then
    # simply return the result
    if dp[n-1][sum] != -1:
        return dp[n-1][sum]
​
    # count is sum of solutions (i)
    # including coins[n-1] (ii) excluding coins[n-1]
    dp[n-1][sum] = (
        countRecur(coins, n, sum - coins[n-1], dp) +
        countRecur(coins, n - 1, sum, dp)
    )
    return dp[n-1][sum]
​
​
def count(coins, sum):
    dp = [[-1 for _ in range(sum + 1)] for _ in range(len(coins))]
    return countRecur(coins, len(coins), sum, dp)
​
↔​

Output
5
[Better Approach 2] Using Bottom-Up DP (Tabulation) – O(sum*n) time and O(sum*n) space
In the memoization approach we solved each subproblem top-down using recursion, but in the tabulation approach we build the solution in a bottom-up manner by filling a DP table iteratively.

We first define the base cases for the DP table.

dp[0][0] = 1, meaning if we have 0 coins and target sum is 0, there is exactly one way — choose nothing.
For dp[0][j] where j > 0, the value is 0 because with zero coins we cannot make a positive sum.
For dp[i][0], the value is 1 for all i because there is only one way to make sum 0 — by not selecting any coin.
After the base initialization, we fill the table iteratively using the same idea.

1.webp1.webp







def count(coins, sum):
​
    n = len(coins)
​
    # Initialize DP table
    dp = [[0] * (sum + 1) for _ in range(n + 1)]
​
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(sum + 1):
​
            # Add the number of ways to make change without
            # using the current coin,
            dp[i][j] += dp[i - 1][j]
​
            if j - coins[i - 1] >= 0:
​
                # Add the number of ways to make change
                # using the current coin
                dp[i][j] += dp[i][j - coins[i - 1]]
​
    return dp[n][sum]
​
↔​

Output
5
[Expected Approach] Using Space Optimized DP – O(sum*n) time and O(sum) space
In previous approach of dynamic programming we have derive the relation between states as given below:

if (sum-coins[i]) is greater than 0, then dp[i][sum] = dp[i][sum-coins[i]] + dp[i+1][sum].
else dp[i][sum] = dp[i+1][sum].
If we observe that for calculating current dp[i][sum] state we only need previous row dp[i-1][sum] or current row dp[i][sum-coins[i]]. There is no need to store all the previous states just one previous state is used to compute result.





def count(coins, sum):
    n = len(coins)

    # dp[i] will be storing the number of solutions for
    # value i.
    dp = [0] * (sum + 1)
    dp[0] = 1

    # Pick all coins one by one and update the table[]
    # values after the index greater than or equal to the
    # value of the picked coin
    for i in range(n):
        for j in range(coins[i], sum + 1):
            dp[j] += dp[j - coins[i]]

    return dp[sum]
def count(coins, sum):
    n = len(coins)
​
    # dp[i] will be storing the number of solutions for
    # value i.
    dp = [0] * (sum + 1)
    dp[0] = 1
​
    # Pick all coins one by one and update the table[]
    # values after the index greater than or equal to the
    # value of the picked coin
    for i in range(n):
        for j in range(coins[i], sum + 1):
            dp[j] += dp[j - coins[i]]
​
    return dp[sum]
​
↔​

'''
#similar as count of subset

'''
coin change -2 minimum no of coins

need to take minimum number to mke sum 5
Coin Change - Minimum Coins to Make Sum
Last Updated :
14 Mar, 2025
Given an array of coins[] of size n and a target value sum, where coins[i] represent the coins of different denominations. You have an infinite supply of each of the coins. The task is to find the minimum number of coins required to make the given value sum. If it is not possible to form the sum using the given coins, return -1.

Examples:  

Input: coins[] = [25, 10, 5], sum = 30
Output: 2
Explanation : Minimum 2 coins needed, 25 and 5  

Input: coins[] = [9, 6, 5, 1], sum = 19
Output: 3
Explanation: 19 = 9 + 9 + 1

Input: coins[] = [5, 1], sum = 0
Output: 0
Explanation: For 0 sum, we do not need a coin

Input: coins[] = [4, 6, 2], sum = 5
Output: -1
Explanation: Not possible to make the given sum.

Try It Yourself
redirect icon
Table of Content

[Naive Approach ] Using Recursion – O(n^sum) Time and O(sum) Space
[Better Approach 1] Using Top-Down DP (Memoization) - O(n*sum) Time and O(n*sum) Space
[Better Approach 2] Using Bottom-Up DP (Tabulation) - O(n*sum) Time and O(n*sum) Space
[Expected Approach] Using Space Optimized DP – O(n*sum) Time and O(sum) Space
[Naive Approach ] Using Recursion – O(n^sum) Time and O(sum) Space
This problem is a variation of the problem Coin Change Problem. Here instead of finding the total number of possible solutions, we need to find the solution with the minimum number of coins.

The idea is to find the minimum number of coins required to reach the target sum by trying each coin denomination in the coins[] array. Starting from the target sum, for each coin coins[i], we can either include it or exclude it. If we include it, we subtract its value from sum and recursively try to make the remaining amount with the same coin denominations. If we exclude it, we move to the next coin in the list. 

Mathematically the recurrence relation will look like the following:

minCoins(i, sum, coins) = min(1 + minCoins(i, sum-coins[i], coins), minCoins(i+1, sum, coins))

Base cases:

minCoins(i, sum, coins) = 0, if sum = 0.
minCoins(i, sum, coins) = INTEGER MAX, if sum < 0 or i == size of coins.




# Python program to find minimum of coins
# to make a given change sum
​
def minCoinsRecur(i, sum, coins):
    
    # base case
    if sum == 0:
        return 0
    if sum < 0 or i == len(coins):
        return float('inf')
    
    take = float('inf')
    
    # take a coin only if its value
    # is greater than 0.
    if coins[i] > 0:
        take = minCoinsRecur(i, sum - coins[i], coins)
        if take != float('inf'):
            take += 1
    #not taking the coin
    noTake = minCoinsRecur(i + 1, sum, coins)
    
    return min(take, noTake)
​
def minCoins(coins, sum):
    ans = minCoinsRecur(0, sum, coins)
    return ans if ans != float('inf') else -1
​
if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    sum = 19
    print(minCoins(coins, sum))

Output
3
[Better Approach 1] Using Top-Down DP (Memoization) - O(n*sum) Time and O(n*sum) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:

1. Optimal Substructure: 

Minimum number of ways to make sum at index i, i.e., minCoins(i, sum, coins), depends on the optimal solutions of the subproblems minCoins(i, sum-coins[i], coins) , and minCoins(i+1, sum, coins). By comparing these optimal substructures, we can efficiently calculate the minimum number of coins to make target sum at index i.

2. Overlapping Subproblems: 

While applying a recursive approach in this problem, we notice that certain subproblems are computed multiple times. 

There are only are two parameters: i and sum that changes in the recursive solution. So we create a 2D matrix of size n*(sum+1) for memoization.
We initialize this matrix as -1 to indicate nothing is computed initially.
Now we modify our recursive solution to first check if the value is -1, then only make recursive calls. This way, we avoid re-computations of the same subproblems.




# Python program to find minimum of coins
# to make a given change sum
​
def minCoinsRecur(i, sum, coins, memo):
    
    # base case
    if sum == 0:
        return 0
    if sum < 0 or i == len(coins):
        return float('inf')
    
    if memo[i][sum] != -1:
        return memo[i][sum]
    
    take = float('inf')
    
    # take a coin only if its value
    # is greater than 0.
    if coins[i] > 0:
        take = minCoinsRecur(i, sum - coins[i], coins, memo)
        if take != float('inf'):
            take += 1
    #not take the coins 
    noTake = minCoinsRecur(i + 1, sum, coins, memo)
    
    memo[i][sum] = min(take, noTake)
    return memo[i][sum]
​
def minCoins(coins, sum):
    memo = [[-1] * (sum + 1) for _ in range(len(coins))]
    ans = minCoinsRecur(0, sum, coins, memo)
    return ans if ans != float('inf') else -1
​
if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    sum = 19
    print(minCoins(coins, sum))

Output
3
[Better Approach 2] Using Bottom-Up DP (Tabulation) - O(n*sum) Time and O(n*sum) Space
 The idea is to fill the DP table based on previous values. For each coin, we either include it or exclude it to compute the minimum number of coins needed for each sum. The table is filled in an iterative manner from i = n-1 to i = 0 and for each sum from 1 to sum. 

The dynamic programming relation is as follows: 

if (sum-coins[i]) is greater than 0, then dp[i][sum] = min(1+dp[i][sum-coins[i]], dp[i+1][sum])
else dp[i][sum] = dp[i+1][sum].




# Python program to find minimum of coins
# to make a given change sum
​
def minCoins(coins, sum):
    dp = [[0] * (sum + 1) for _ in range(len(coins))]
​
    for i in range(len(coins) - 1, -1, -1):
        for j in range(1, sum + 1):
            dp[i][j] = float('inf')
            take = float('inf')
            noTake = float('inf')
​
            # If we take coins[i] coin
            if j - coins[i] >= 0:
                take = dp[i][j - coins[i]]
                if take != float('inf'):
                    take += 1
​
            if i + 1 < len(coins):
                #not take the coins
                noTake = dp[i + 1][j]
​
            dp[i][j] = min(take, noTake)
​
    if dp[0][sum] != float('inf'):
        return dp[0][sum]
    return -1
​
if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    sum = 19
    print(minCoins(coins, sum))

Output
3
[Expected Approach] Using Space Optimized DP – O(n*sum) Time and O(sum) Space
In previous approach of dynamic programming we have derive the relation between states as given below:

if (sum-coins[i]) is greater than 0, then dp[i][sum] = min(1+dp[i][sum-coins[i]], dp[i+1][sum])
else dp[i][sum] = dp[i+1][sum].
If we observe that for calculating current dp[i][sum] state we only need previous row dp[i-1][sum] or current row dp[i][sum-coins[i]]. There is no need to store all the previous states just one previous state is used to compute result.





# Python program to find minimum of coins
def minCoins(coins, sum):
    
    # Initialize a list to store the minimum 
    # number of coins for each amount
    dp = [float('inf')] * (sum + 1)
    
    # Base case: 0 coins are needed to make the sum of 0
    dp[0] = 0 
    
    # Iterate over each coin in reverse order
    for i in range(len(coins) - 1, -1, -1):
        
        # Iterate through all amounts from 1 to sum
        for j in range(1, sum + 1):
            
            #  take variable for the current coin
            take = float('inf')  
            
            #  noTake variable for the current amount
            noTake = float('inf') 
            
            # If we can take the current coin
            if j - coins[i] >= 0 and coins[i] > 0:
                
                # Get the minimum coins needed 
                # for the remaining amount
                take = dp[j - coins[i]]
                
                # Increment the count if it's a valid take
                if take != float('inf'): 
                    take += 1
            
            # If there are coins left to consider
            if i + 1 < len(coins):
                
                # Get the minimum coins needed without
                # taking the current coin
                noTake = dp[j] 
                
            # Store the minimum of taking or not
            # taking the current coin
            dp[j] = min(take, noTake)
    
    # Return the result for the given sum,
    # or -1 if it's not possible
    return dp[sum] if dp[sum] != float('inf') else -1
​
if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    sum = 19 
    print(minCoins(coins, sum))

Output
3


'''



'''
================================================================================
================================================================================
    UNBOUNDED KNAPSACK — ULTIMATE FAANG/MAANG TRICKS & REVISION GUIDE
================================================================================
================================================================================

════════════════════════════════════════════════════════════════════════════════
MASTER TRICK #1: "STAY on same row" vs "GO to previous row"
════════════════════════════════════════════════════════════════════════════════

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

════════════════════════════════════════════════════════════════════════════════
MASTER TRICK #2: 1D Loop Direction
════════════════════════════════════════════════════════════════════════════════

    ┌────────────────────────────────────────────────────────────────┐
    │  0/1 Knapsack 1D:  iterate j from RIGHT to LEFT (W → wt[i])  │
    │  Unbounded 1D:     iterate j from LEFT to RIGHT (wt[i] → W)  │
    │                                                                │
    │  WHY? Left-to-right uses updated values = reusing same item!  │
    └────────────────────────────────────────────────────────────────┘

    MNEMONIC: "U-L-R" = Unbounded → Left to Right
              "0/1-R-L" = 0/1 → Right to Left

════════════════════════════════════════════════════════════════════════════════
MASTER TRICK #3: IDENTIFICATION — "How do I know it's UNBOUNDED?"
════════════════════════════════════════════════════════════════════════════════

    Ask 3 questions:
    1. Is there a CHOICE? (pick or skip) → YES = Knapsack family
    2. Can I REUSE the same item? → YES = UNBOUNDED
    3. What am I optimizing? → MAX/MIN/COUNT

    KEYWORD SPOTTERS:
    ┌────────────────────────────────────────────────┐
    │ "infinite supply"        → UNBOUNDED           │
    │ "unlimited quantity"     → UNBOUNDED           │
    │ "can use multiple times" → UNBOUNDED           │
    │ "as many times as want"  → UNBOUNDED           │
    │ "at most once"           → 0/1 Knapsack        │
    └────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
MASTER TRICK #4: VARIABLE MAPPING TABLE (Every problem maps to same template)
════════════════════════════════════════════════════════════════════════════════

    ┌──────────────────┬──────────┬──────────┬─────────────┬──────────────┐
    │ Problem          │ items[]  │ values[] │ capacity(W) │ Optimize     │
    ├──────────────────┼──────────┼──────────┼─────────────┼──────────────┤
    │ Rod Cutting      │ length[] │ price[]  │ rod_length  │ MAX profit   │
    │ Coin Change I    │ coins[]  │ 1 (each) │ target_sum  │ COUNT ways   │
    │ Coin Change II   │ coins[]  │ 1 (each) │ target_sum  │ MIN coins    │
    │ Integer Break    │ [1..n-1] │ products │ n           │ MAX product  │
    │ Perfect Squares  │ [1,4,9.] │ 1 (each) │ n           │ MIN squares  │
    │ Min Cost Tickets │ [1,7,30] │ costs[]  │ max_day     │ MIN cost     │
    │ Max Ribbon Cut   │ cuts[]   │ 1 (each) │ ribbon_len  │ MAX pieces   │
    │ Word Break       │ words[]  │ bool     │ len(string) │ FEASIBLE?    │
    └──────────────────┴──────────┴──────────┴─────────────┴──────────────┘

════════════════════════════════════════════════════════════════════════════════
MASTER TRICK #5: THE "5-FINGER" REVISION TRICK
════════════════════════════════════════════════════════════════════════════════

    THUMB:    "STAY or GO" — Include: stay on row i. Exclude: go to i-1.
    INDEX:    "LEFT to RIGHT" — 1D loops left→right (not right→left!)
    MIDDLE:   "What to optimize?" — MAX (rod/ribbon), MIN (coins/squares), COUNT (ways)
    RING:     "Base case" — dp[0]=0 for min/max, dp[0]=1 for count
    PINKY:    "Infinity direction" — MIN: init +∞. MAX: init 0 or -∞.

════════════════════════════════════════════════════════════════════════════════
PATTERN RECOGNITION TABLE (Quick Revision):
════════════════════════════════════════════════════════════════════════════════

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

════════════════════════════════════════════════════════════════════════════════
UNIVERSAL 1D TEMPLATE (Covers 90% of FAANG unbounded problems):
════════════════════════════════════════════════════════════════════════════════

    def solve(items, target):
        dp = [BASE_VALUE] * (target + 1)
        dp[0] = INITIAL_VALUE
        
        for item in items:                        # outer: each item
            for j in range(item, target + 1):     # inner: LEFT to RIGHT!
                dp[j] = OPERATION(dp[j], COMBINE(dp[j - item]))
        
        return dp[target]

    ┌─────────────────┬──────────────┬───────────────┬──────────────────┐
    │ Problem Type    │ BASE_VALUE   │ INITIAL_VALUE │ OPERATION        │
    ├─────────────────┼──────────────┼───────────────┼──────────────────┤
    │ Maximize        │ 0            │ 0             │ max(dp[j], ...)  │
    │ Minimize        │ float('inf') │ 0             │ min(dp[j], ...)  │
    │ Count           │ 0            │ 1             │ dp[j] += ...     │
    └─────────────────┴──────────────┴───────────────┴──────────────────┘

════════════════════════════════════════════════════════════════════════════════
FINAL COMPARISON — 0/1 vs UNBOUNDED:
════════════════════════════════════════════════════════════════════════════════

    ┌──────────────────────────┬────────────────────┬────────────────────────┐
    │ Aspect                   │ 0/1 Knapsack       │ Unbounded Knapsack     │
    ├──────────────────────────┼────────────────────┼────────────────────────┤
    │ Item usage               │ At most ONCE       │ UNLIMITED times        │
    │ 2D: include uses row     │ dp[i-1][...]       │ dp[i][...]             │
    │ 1D: inner loop direction │ RIGHT → LEFT       │ LEFT → RIGHT           │
    │ Keyword in problem       │ "each item once"   │ "infinite supply"      │
    └──────────────────────────┴────────────────────┴────────────────────────┘

    MNEMONICS:
    "STAY for PLAY" = Stay on same row when you want to play (reuse) the item
    "GO when NO" = Go to previous row when you say NO to the item
    "Infinite = i stays, Finite = i-1 goes"

════════════════════════════════════════════════════════════════════════════════
INTERVIEW FLOW (Follow EVERY time):
════════════════════════════════════════════════════════════════════════════════

    1. READ problem → spot "unlimited/infinite supply" → say "Unbounded Knapsack"
    2. MAP variables → items=?, capacity=?, optimize=?
    3. WRITE 1D template → fill in operation type
    4. TRACE with small example → verify correctness
    5. STATE complexity → O(n * W) time, O(W) space

════════════════════════════════════════════════════════════════════════════════
COMMON INTERVIEW FOLLOW-UPS:
════════════════════════════════════════════════════════════════════════════════

    Q: "What if each item can only be used once?"
    A: "0/1 knapsack — change loop direction to RIGHT→LEFT in 1D"

    Q: "What about order matters? (permutations vs combinations)"
    A: ORDER MATTERS (permutations): swap loops → target outer, items inner
       ORDER DOESN'T MATTER (combinations): items outer, target inner

'''

'''
════════════════════════════════════════════════════════════════════════════════
════════════════════════════════════════════════════════════════════════════════
ALL UNBOUNDED KNAPSACK PROBLEMS — FAANG/MAANG (with code)
════════════════════════════════════════════════════════════════════════════════
════════════════════════════════════════════════════════════════════════════════

All problems follow the SAME unbounded knapsack pattern:
    - Identify: wt[], val[], W (capacity)
    - Code: take (STAY on same row i) or noTake (GO to previous row i-1)
    - 1D optimization: loop LEFT to RIGHT


════════════════════════════════════════════════════════════════════════════════
PROBLEM: ROD CUTTING — Amazon, Google, Goldman Sachs
════════════════════════════════════════════════════════════════════════════════

Given a rod of length n and an array price[] where price[i] denotes 
the price of a piece of length i. Find the maximum profit by cutting
the rod into pieces and selling them.

Example:
Input: price[] = [0, 1, 5, 8, 9, 10, 17, 17, 20], n = 8
Output: 22
Explanation: Cut into lengths 2 and 6 → 5 + 17 = 22

Input: price[] = [0, 3, 5, 8, 9, 10, 17, 17, 20], n = 8
Output: 24
Explanation: Cut into 8 pieces of length 1 → 8 × 3 = 24

How to identify unbounded knapsack?
- items = different cut lengths [1, 2, 3, ..., n]
- each length can be used MULTIPLE times (unlimited supply!)
- capacity = rod length n
- goal = MAXIMIZE profit

code variation:
    wt[] ---> length[] = [1, 2, 3, ..., n]
    val[] ---> price[]
    W ---> n (rod length)
    objective ---> MAXIMIZE profit

[Naive Approach] Using Recursion — O(2^n) Time, O(n) Space

For each cut length i, we have two choices: take (stay) or skip (move to next).


def cutRodRecur(i, j, price):

    # base case
    if i == 0 or j == 0:
        return 0

    take = 0
    # take cut of length i (stay at same i - can reuse!)
    if i <= j:
        take = price[i] + cutRodRecur(i, j - i, price)

    # not take (move to next smaller length)
    noTake = cutRodRecur(i - 1, j, price)

    return max(take, noTake)


def cutRod(price):
    n = len(price) - 1
    return cutRodRecur(n, n, price)


[Better Approach] Using Top-Down DP (Memoization) — O(n^2) Time, O(n^2) Space


def cutRodRecur(i, j, price, dp):

    if i == 0 or j == 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    take = 0
    if i <= j:
        take = price[i] + cutRodRecur(i, j - i, price, dp)

    noTake = cutRodRecur(i - 1, j, price, dp)

    dp[i][j] = max(take, noTake)
    return dp[i][j]


def cutRod(price):
    n = len(price) - 1
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    return cutRodRecur(n, n, price, dp)


[Better Approach 2] Using Bottom-Up DP (Tabulation) — O(n^2) Time, O(n^2) Space

dp[i][j] = max profit using lengths 1..i with rod length j

if(length[i-1] <= j):
    dp[i][j] = max(price[i-1] + dp[i][j - length[i-1]], dp[i-1][j])
                                  ^^^
                        STAY on same row i (unbounded - can reuse!)
else:
    dp[i][j] = dp[i-1][j]


def cutRod(price):
    n = len(price) - 1
    length = list(range(1, n + 1))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if length[i-1] <= j:
                take = price[i] + dp[i][j - length[i-1]]
                noTake = dp[i-1][j]
                dp[i][j] = max(take, noTake)
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][n]


[Expected Approach] Using Space Optimized DP — O(n^2) Time, O(n) Space


def cutRod(price):
    n = len(price) - 1
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] = max(dp[j], price[i] + dp[j - i])

    return dp[n]


Output
n=8 → 22


════════════════════════════════════════════════════════════════════════════════
PROBLEM: COIN CHANGE 1 — Count Ways (LeetCode 518) — Amazon, Goldman Sachs
════════════════════════════════════════════════════════════════════════════════

Given coins[] and a target sum, find the number of COMBINATIONS to make sum.
Infinite supply of each coin (unbounded!).

Example:
Input: coins = [1, 2, 3], sum = 5
Output: 5
Explanation: [1,1,1,1,1], [1,1,1,2], [1,1,3], [1,2,2], [2,3]

Input: coins = [2, 5, 3, 6], sum = 10
Output: 5

How to identify unbounded knapsack?
- items = coins (infinite supply = unbounded!)
- capacity = target sum
- goal = COUNT number of ways

code variation:
    wt[] ---> coins[]
    val[] ---> not needed (we are counting, not maximizing)
    W ---> sum (target)
    objective ---> COUNT ways
    
    KEY CHANGE: instead of max(take, noTake), we ADD: take + noTake

[Naive Approach] Using Recursion — O(2^sum) Time, O(sum) Space

For each coin: include (stay at same n - can reuse!) or exclude (move to n-1)


def countRecur(coins, n, sum):

    # If sum is 0 then there is 1 solution
    if sum == 0:
        return 1

    if sum < 0 or n == 0:
        return 0

    # include coins[n-1] (stay at n) + exclude coins[n-1] (go to n-1)
    take = countRecur(coins, n, sum - coins[n - 1])
    noTake = countRecur(coins, n - 1, sum)

    return take + noTake


def count(coins, sum):
    return countRecur(coins, len(coins), sum)


[Better Approach] Using Top-Down DP (Memoization) — O(sum*n) Time, O(sum*n) Space


def countRecur(coins, n, sum, dp):

    if sum == 0:
        return 1

    if sum < 0 or n == 0:
        return 0

    if dp[n-1][sum] != -1:
        return dp[n-1][sum]

    take = countRecur(coins, n, sum - coins[n-1], dp)
    noTake = countRecur(coins, n - 1, sum, dp)

    dp[n-1][sum] = take + noTake
    return dp[n-1][sum]


def count(coins, sum):
    dp = [[-1] * (sum + 1) for _ in range(len(coins))]
    return countRecur(coins, len(coins), sum, dp)


[Better Approach 2] Using Bottom-Up DP (Tabulation) — O(sum*n) Time, O(sum*n) Space

if(coins[i-1] <= j):
    dp[i][j] = dp[i][j - coins[i-1]] + dp[i-1][j]
               ^^^^^^^^^^^^^^^^^^^^     ^^^^^^^^^^
               take (STAY same row)     noTake (previous row)
else:
    dp[i][j] = dp[i-1][j]


def count(coins, sum):
    n = len(coins)
    dp = [[0] * (sum + 1) for _ in range(n + 1)]

    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(sum + 1):
            # noTake: don't use this coin
            dp[i][j] = dp[i - 1][j]

            # take: use this coin (stay on same row!)
            if j - coins[i - 1] >= 0:
                dp[i][j] += dp[i][j - coins[i - 1]]

    return dp[n][sum]


[Expected Approach] Using Space Optimized DP — O(sum*n) Time, O(sum) Space


def count(coins, sum):
    n = len(coins)
    dp = [0] * (sum + 1)
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], sum + 1):
            dp[j] += dp[j - coins[i]]

    return dp[sum]


Output
coins=[1,2,3], sum=5 → 5


════════════════════════════════════════════════════════════════════════════════
PROBLEM: COIN CHANGE 2 — Minimum Coins (LeetCode 322) — Google, Amazon, Apple
════════════════════════════════════════════════════════════════════════════════

Given coins[] and a target sum, find MINIMUM number of coins to make sum.
If not possible, return -1. Infinite supply of each coin.

Example:
Input: coins = [25, 10, 5], sum = 30
Output: 2
Explanation: 25 + 5 = 30

Input: coins = [9, 6, 5, 1], sum = 19
Output: 3
Explanation: 9 + 9 + 1 = 19

Input: coins = [4, 6, 2], sum = 5
Output: -1

How to identify unbounded knapsack?
- items = coins (infinite supply = unbounded!)
- capacity = target sum
- goal = MINIMIZE number of coins

code variation:
    wt[] ---> coins[]
    val[] ---> 1 (each coin counts as 1)
    W ---> sum (target)
    objective ---> MINIMIZE count
    
    KEY CHANGES from standard:
    - Use min() instead of max()
    - Initialize with float('inf') instead of 0
    - Add +1 when taking a coin
    - Return -1 if result is still infinity

[Naive Approach] Using Recursion — O(n^sum) Time, O(sum) Space

For each coin: take (stay at same i - can reuse!) or noTake (move to i+1)


def minCoinsRecur(i, sum, coins):

    # base case
    if sum == 0:
        return 0
    if sum < 0 or i == len(coins):
        return float('inf')

    take = float('inf')
    # take coin (stay at same index - unbounded!)
    if coins[i] > 0:
        take = minCoinsRecur(i, sum - coins[i], coins)
        if take != float('inf'):
            take += 1

    # not take (move to next coin)
    noTake = minCoinsRecur(i + 1, sum, coins)

    return min(take, noTake)


def minCoins(coins, sum):
    ans = minCoinsRecur(0, sum, coins)
    return ans if ans != float('inf') else -1


[Better Approach] Using Top-Down DP (Memoization) — O(n*sum) Time, O(n*sum) Space


def minCoinsRecur(i, sum, coins, memo):

    if sum == 0:
        return 0
    if sum < 0 or i == len(coins):
        return float('inf')

    if memo[i][sum] != -1:
        return memo[i][sum]

    take = float('inf')
    if coins[i] > 0:
        take = minCoinsRecur(i, sum - coins[i], coins, memo)
        if take != float('inf'):
            take += 1

    noTake = minCoinsRecur(i + 1, sum, coins, memo)

    memo[i][sum] = min(take, noTake)
    return memo[i][sum]


def minCoins(coins, sum):
    memo = [[-1] * (sum + 1) for _ in range(len(coins))]
    ans = minCoinsRecur(0, sum, coins, memo)
    return ans if ans != float('inf') else -1


[Better Approach 2] Using Bottom-Up DP (Tabulation) — O(n*sum) Time, O(n*sum) Space

if(coins[i] <= j):
    dp[i][j] = min(1 + dp[i][j - coins[i]], dp[i+1][j])
                       ^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^
                       take (STAY same row)  noTake (next row)
else:
    dp[i][j] = dp[i+1][j]


def minCoins(coins, sum):
    n = len(coins)
    dp = [[0] * (sum + 1) for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(1, sum + 1):
            dp[i][j] = float('inf')
            take = float('inf')
            noTake = float('inf')

            # take coin (stay on same row!)
            if j - coins[i] >= 0:
                take = dp[i][j - coins[i]]
                if take != float('inf'):
                    take += 1

            # noTake (go to next row)
            if i + 1 < n:
                noTake = dp[i + 1][j]

            dp[i][j] = min(take, noTake)

    return dp[0][sum] if dp[0][sum] != float('inf') else -1


[Expected Approach] Using Space Optimized DP — O(n*sum) Time, O(sum) Space


def minCoins(coins, sum):
    dp = [float('inf')] * (sum + 1)
    dp[0] = 0

    for i in range(len(coins) - 1, -1, -1):
        for j in range(1, sum + 1):
            take = float('inf')
            noTake = float('inf')

            if j - coins[i] >= 0 and coins[i] > 0:
                take = dp[j - coins[i]]
                if take != float('inf'):
                    take += 1

            if i + 1 < len(coins):
                noTake = dp[j]

            dp[j] = min(take, noTake)

    return dp[sum] if dp[sum] != float('inf') else -1


Output
coins=[9,6,5,1], sum=19 → 3
coins=[25,10,5], sum=30 → 2


════════════════════════════════════════════════════════════════════════════════
PROBLEM: PERFECT SQUARES (LeetCode 279) — Google, Facebook, Amazon
════════════════════════════════════════════════════════════════════════════════

Given n, return the minimum number of perfect square numbers that sum to n.

Example:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9

How to identify unbounded knapsack?
- items = perfect squares [1, 4, 9, 16, 25, ...]
- each square can be used MULTIPLE times (unlimited supply!)
- capacity = n
- goal = MINIMUM number of items

This is literally Coin Change (minimum coins) where coins = [1, 4, 9, 16, ...]

code variation:
    wt[] ---> squares[] = [1, 4, 9, 16, ...]
    val[] ---> 1 (each square counts as 1 item)
    W ---> n (target number)
    objective ---> MINIMIZE count

[Naive Approach] Using Recursion — O(sqrt(n)^n) Time, O(n) Space

For each remaining value, try subtracting every perfect square <= remaining.
Pick the one that gives minimum count.


def numSquaresRecur(i, n, squares):

    # base case
    if n == 0:
        return 0
    if n < 0 or i == len(squares):
        return float('inf')

    take = float('inf')

    # take the square (stay at same index - can reuse!)
    if squares[i] <= n:
        take = numSquaresRecur(i, n - squares[i], squares)
        if take != float('inf'):
            take += 1

    # not take (move to next square)
    noTake = numSquaresRecur(i + 1, n, squares)

    return min(take, noTake)


def numSquares(n):
    squares = [i*i for i in range(1, int(n**0.5) + 1)]
    return numSquaresRecur(0, n, squares)

if __name__ == "__main__":
    n = 12
    print(numSquares(n))

Output
3

[Better Approach] Using Top-Down DP (Memoization) — O(n * sqrt(n)) Time, O(n * sqrt(n)) Space


def numSquaresRecur(i, n, squares, memo):

    if n == 0:
        return 0
    if n < 0 or i == len(squares):
        return float('inf')

    if memo[i][n] != -1:
        return memo[i][n]

    take = float('inf')

    if squares[i] <= n:
        take = numSquaresRecur(i, n - squares[i], squares, memo)
        if take != float('inf'):
            take += 1

    noTake = numSquaresRecur(i + 1, n, squares, memo)

    memo[i][n] = min(take, noTake)
    return memo[i][n]


def numSquares(n):
    squares = [i*i for i in range(1, int(n**0.5) + 1)]
    memo = [[-1] * (n + 1) for _ in range(len(squares))]
    return numSquaresRecur(0, n, squares, memo)

if __name__ == "__main__":
    n = 12
    print(numSquares(n))

Output
3

[Expected Approach] Using Space Optimized DP — O(n * sqrt(n)) Time, O(n) Space

Same as coin change 1D optimization:
    dp[j] = min(dp[j], 1 + dp[j - squares[i]])


def numSquares(n):
    squares = [i*i for i in range(1, int(n**0.5) + 1)]

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(len(squares)):
        for j in range(squares[i], n + 1):
            dp[j] = min(dp[j], 1 + dp[j - squares[i]])

    return dp[n]

if __name__ == "__main__":
    n = 12
    print(numSquares(n))

Output
3


════════════════════════════════════════════════════════════════════════════════
PROBLEM: MAXIMUM RIBBON CUT (Amazon, Microsoft)
════════════════════════════════════════════════════════════════════════════════

Given a ribbon of length n and array of allowed cut lengths,
find the MAXIMUM number of pieces you can cut it into.
If not possible to cut exactly, return -1.

Example:
Input: n = 5, cuts = [2, 3, 5]
Output: 2
Explanation: 2 + 3 = 5 (2 pieces)

Input: n = 7, cuts = [2, 3]
Output: 3
Explanation: 2 + 2 + 3 = 7 (3 pieces)

Input: n = 7, cuts = [5, 3]
Output: -1
Explanation: Cannot make exactly 7

How to identify?
- items = cut lengths (can reuse = unbounded!)
- capacity = ribbon length n
- goal = MAXIMIZE number of pieces

This is OPPOSITE of coin change minimum!
    coin change min: minimize count, init +∞
    ribbon cut max:  maximize count, init -∞

code variation:
    wt[] ---> cuts[]
    val[] ---> 1 (each cut = 1 piece)
    W ---> n (ribbon length)
    objective ---> MAXIMIZE count

[Naive Approach] Using Recursion — O(k^n) Time, O(n) Space


def maxRibbonRecur(i, n, cuts):

    # base case
    if n == 0:
        return 0
    if n < 0 or i == len(cuts):
        return float('-inf')

    take = float('-inf')

    # take the cut (stay at same index - can reuse!)
    if cuts[i] <= n:
        take = maxRibbonRecur(i, n - cuts[i], cuts)
        if take != float('-inf'):
            take += 1

    # not take (move to next cut size)
    noTake = maxRibbonRecur(i + 1, n, cuts)

    return max(take, noTake)


def maxRibbon(n, cuts):
    ans = maxRibbonRecur(0, n, cuts)
    return ans if ans != float('-inf') else -1

if __name__ == "__main__":
    n = 7
    cuts = [2, 3]
    print(maxRibbon(n, cuts))

Output
3

[Better Approach] Using Top-Down DP (Memoization) — O(n * k) Time, O(n * k) Space


def maxRibbonRecur(i, n, cuts, memo):

    if n == 0:
        return 0
    if n < 0 or i == len(cuts):
        return float('-inf')

    if memo[i][n] != -1:
        return memo[i][n]

    take = float('-inf')

    if cuts[i] <= n:
        take = maxRibbonRecur(i, n - cuts[i], cuts, memo)
        if take != float('-inf'):
            take += 1

    noTake = maxRibbonRecur(i + 1, n, cuts, memo)

    memo[i][n] = max(take, noTake)
    return memo[i][n]


def maxRibbon(n, cuts):
    memo = [[-1] * (n + 1) for _ in range(len(cuts))]
    ans = maxRibbonRecur(0, n, cuts, memo)
    return ans if ans != float('-inf') else -1

if __name__ == "__main__":
    n = 7
    cuts = [2, 3]
    print(maxRibbon(n, cuts))

Output
3

[Expected Approach] Using Space Optimized DP — O(n * k) Time, O(n) Space

    dp[j] = max(dp[j], 1 + dp[j - cuts[i]])
    NOTE: init dp with -∞ (opposite of coin change which uses +∞)


def maxRibbon(n, cuts):

    dp = [float('-inf')] * (n + 1)
    dp[0] = 0

    for i in range(len(cuts)):
        for j in range(cuts[i], n + 1):
            if dp[j - cuts[i]] != float('-inf'):
                dp[j] = max(dp[j], 1 + dp[j - cuts[i]])

    return dp[n] if dp[n] != float('-inf') else -1

if __name__ == "__main__":
    n = 7
    cuts = [2, 3]
    print(maxRibbon(n, cuts))

Output
3


════════════════════════════════════════════════════════════════════════════════
PROBLEM: INTEGER BREAK (LeetCode 343) — Google, Amazon, Microsoft
════════════════════════════════════════════════════════════════════════════════

Given an integer n, break it into the sum of at least two positive integers
and maximize the product of those integers.

Example:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, and 3 × 3 × 4 = 36

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, and 1 × 1 = 1

How to identify?
- items = numbers [1, 2, 3, ..., n-1]
- can reuse same number (unbounded!)
- capacity = n (must sum to n)
- goal = MAXIMIZE product

code variation:
    wt[] ---> [1, 2, 3, ..., n-1] (possible pieces)
    val[] ---> the pieces themselves (we multiply them)
    W ---> n
    objective ---> MAXIMIZE product

[Naive Approach] Using Recursion — O(2^n) Time, O(n) Space

For each split j, we choose:
    take = j * solve(n - j)  (break further)
    OR    j * (n - j)        (don't break the remaining)


def intBreakRecur(n):

    if n == 1:
        return 1

    ans = 0
    for j in range(1, n):
        # j stays as-is
        # (n-j) either stays as-is OR gets broken further
        ans = max(ans, j * max(n - j, intBreakRecur(n - j)))

    return ans

if __name__ == "__main__":
    n = 10
    print(intBreakRecur(n))

Output
36

[Better Approach] Using Top-Down DP (Memoization) — O(n^2) Time, O(n) Space


def intBreakRecur(n, memo):

    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    ans = 0
    for j in range(1, n):
        ans = max(ans, j * max(n - j, intBreakRecur(n - j, memo)))

    memo[n] = ans
    return ans


def integerBreak(n):
    memo = [-1] * (n + 1)
    return intBreakRecur(n, memo)

if __name__ == "__main__":
    n = 10
    print(integerBreak(n))

Output
36

[Expected Approach] Using Bottom-Up DP — O(n^2) Time, O(n) Space


def integerBreak(n):

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i):
            # j * (i-j) = don't break further
            # j * dp[i-j] = break (i-j) further
            dp[i] = max(dp[i], j * max(i - j, dp[i - j]))

    return dp[n]

if __name__ == "__main__":
    n = 10
    print(integerBreak(n))

Output
36


════════════════════════════════════════════════════════════════════════════════
PROBLEM: MINIMUM COST FOR TICKETS (LeetCode 983) — Google, Amazon, Microsoft
════════════════════════════════════════════════════════════════════════════════

You are given days[] (days you need to travel) and costs[] where:
    costs[0] = price of 1-day pass
    costs[1] = price of 7-day pass
    costs[2] = price of 30-day pass

Find the minimum cost to travel on all given days.

Example:
Input: days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15]
Output: 11
Explanation: Buy 7-day pass on day 1 (covers 1-7) = 7
             Buy 1-day pass on day 8 = 2
             Buy 1-day pass on day 20 = 2
             Total = 11

How to identify?
- items = ticket types (1-day, 7-day, 30-day passes)
- can buy same type multiple times (unlimited!)
- goal = MINIMIZE total cost

This is coin change minimum where:
    coins = [1, 7, 30] (days covered)
    values = costs[] (price of each ticket)
    But only count days you actually travel!

code variation:
    wt[] ---> durations = [1, 7, 30]
    val[] ---> costs[]
    W ---> last travel day
    objective ---> MINIMIZE cost

[Naive Approach] Using Recursion — O(3^n) Time, O(n) Space


def minCostRecur(idx, days, costs):
    n = len(days)
    durations = [1, 7, 30]

    if idx >= n:
        return 0

    ans = float('inf')
    for k in range(3):
        # find next day NOT covered by this pass
        j = idx
        while j < n and days[j] < days[idx] + durations[k]:
            j += 1
        ans = min(ans, costs[k] + minCostRecur(j, days, costs))

    return ans


def mincostTickets(days, costs):
    return minCostRecur(0, days, costs)

if __name__ == "__main__":
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(mincostTickets(days, costs))

Output
11

[Better Approach] Using Top-Down DP (Memoization) — O(n) Time, O(n) Space


def minCostRecur(idx, days, costs, memo):
    n = len(days)
    durations = [1, 7, 30]

    if idx >= n:
        return 0

    if memo[idx] != -1:
        return memo[idx]

    ans = float('inf')
    for k in range(3):
        j = idx
        while j < n and days[j] < days[idx] + durations[k]:
            j += 1
        ans = min(ans, costs[k] + minCostRecur(j, days, costs, memo))

    memo[idx] = ans
    return ans


def mincostTickets(days, costs):
    memo = [-1] * len(days)
    return minCostRecur(0, days, costs, memo)

if __name__ == "__main__":
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(mincostTickets(days, costs))

Output
11

[Expected Approach] Using Bottom-Up DP — O(last_day) Time, O(last_day) Space


def mincostTickets(days, costs):
    last_day = days[-1]
    travel_days = set(days)

    dp = [0] * (last_day + 1)

    for i in range(1, last_day + 1):
        if i not in travel_days:
            # not a travel day, no cost needed
            dp[i] = dp[i - 1]
        else:
            # try all 3 passes, pick minimum
            dp[i] = min(
                dp[max(0, i - 1)] + costs[0],    # 1-day pass
                dp[max(0, i - 7)] + costs[1],    # 7-day pass
                dp[max(0, i - 30)] + costs[2]    # 30-day pass
            )

    return dp[last_day]

if __name__ == "__main__":
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(mincostTickets(days, costs))

Output
11


════════════════════════════════════════════════════════════════════════════════
PROBLEM: WORD BREAK (LeetCode 139) — Google, Facebook, Amazon, Apple
════════════════════════════════════════════════════════════════════════════════

Given a string s and a dictionary of words, determine if s can be 
segmented into a space-separated sequence of one or more dictionary words.

Example:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: True
Explanation: "leetcode" = "leet" + "code"

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: False

How to identify?
- items = words in dictionary (can reuse same word = unbounded!)
- capacity = length of string
- goal = can we fill capacity exactly? (FEASIBILITY)

This is like coin change where:
    coins = words (different lengths)
    sum = length of string
    But instead of numbers adding up, words concatenate!

code variation:
    wt[] ---> word lengths
    val[] ---> True/False (does the word match?)
    W ---> len(s)
    objective ---> FEASIBILITY (can we reach end?)

[Naive Approach] Using Recursion — O(2^n) Time, O(n) Space


def wordBreakRecur(start, s, wordSet):

    # reached end = successfully segmented
    if start == len(s):
        return True

    # try every possible end position
    for end in range(start + 1, len(s) + 1):
        # if s[start:end] is a valid word AND rest of string can be broken
        if s[start:end] in wordSet and wordBreakRecur(end, s, wordSet):
            return True

    return False


def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    return wordBreakRecur(0, s, wordSet)

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(wordBreak(s, wordDict))

Output
True

[Better Approach] Using Top-Down DP (Memoization) — O(n^2) Time, O(n) Space


def wordBreakRecur(start, s, wordSet, memo):

    if start == len(s):
        return True

    if memo[start] != -1:
        return memo[start]

    for end in range(start + 1, len(s) + 1):
        if s[start:end] in wordSet and wordBreakRecur(end, s, wordSet, memo):
            memo[start] = True
            return True

    memo[start] = False
    return False


def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    memo = [-1] * len(s)
    return wordBreakRecur(0, s, wordSet, memo)

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(wordBreak(s, wordDict))

Output
True

[Expected Approach] Using Bottom-Up DP — O(n^2) Time, O(n) Space

dp[i] = True means s[0:i] can be segmented into dictionary words


def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True    # empty string is always valid

    for i in range(1, n + 1):
        for j in range(i):
            # if s[0:j] is valid AND s[j:i] is a dictionary word
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return dp[n]

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(wordBreak(s, wordDict))

Output
True


════════════════════════════════════════════════════════════════════════════════
PROBLEM: COMBINATION SUM IV (LeetCode 377) — Google, Facebook
════════════════════════════════════════════════════════════════════════════════

Given nums[] and target, find the number of possible combinations
that add up to target. ORDER MATTERS! (different from coin change ways)

Example:
Input: nums = [1, 2, 3], target = 4
Output: 7
Explanation: 
(1,1,1,1), (1,1,2), (1,2,1), (1,3), (2,1,1), (2,2), (3,1)

DIFFERENCE from Coin Change Ways (LC 518):
    Coin Change Ways: [1,2,1] and [2,1,1] are SAME combination → items outer loop
    Combination Sum IV: [1,2,1] and [2,1,1] are DIFFERENT → target outer loop

TRICK: Just SWAP THE LOOPS!
    Combinations (LC 518):   for coin → for target  (items outer)
    Permutations (LC 377):   for target → for coin  (target outer)

code variation:
    wt[] ---> nums[]
    val[] ---> 1 (count)
    W ---> target
    objective ---> COUNT (but order matters!)

[Naive Approach] Using Recursion — O(n^target) Time, O(target) Space


def combinationRecur(nums, target):

    if target == 0:
        return 1
    if target < 0:
        return 0

    count = 0
    # try every number at each position (order matters!)
    for num in nums:
        count += combinationRecur(nums, target - num)

    return count


def combinationSum4(nums, target):
    return combinationRecur(nums, target)

if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 4
    print(combinationSum4(nums, target))

Output
7

[Better Approach] Using Top-Down DP (Memoization) — O(target * n) Time, O(target) Space


def combinationRecur(nums, target, memo):

    if target == 0:
        return 1
    if target < 0:
        return 0

    if memo[target] != -1:
        return memo[target]

    count = 0
    for num in nums:
        count += combinationRecur(nums, target - num, memo)

    memo[target] = count
    return count


def combinationSum4(nums, target):
    memo = [-1] * (target + 1)
    return combinationRecur(nums, target, memo)

if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 4
    print(combinationSum4(nums, target))

Output
7

[Expected Approach] Using Bottom-Up DP — O(target * n) Time, O(target) Space

KEY DIFFERENCE: target is OUTER loop (not items!)


def combinationSum4(nums, target):

    dp = [0] * (target + 1)
    dp[0] = 1

    # TARGET outer loop (order matters!)
    for j in range(1, target + 1):
        # ITEMS inner loop
        for num in nums:
            if j - num >= 0:
                dp[j] += dp[j - num]

    return dp[target]

if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 4
    print(combinationSum4(nums, target))

Output
7

'''

# ══════════════════════════════════════════════════════════════════════════════
# RUNNABLE CODE — ALL APPROACHES FOR ALL PROBLEMS
# ══════════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════════
# ROD CUTTING
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def cutRodRecur(i, price):
    if i == 0:
        return 0
    ans = 0
    for j in range(1, i + 1):
        ans = max(ans, price[j] + cutRodRecur(i - j, price))
    return ans


def cutRod_recursion(price):
    n = len(price) - 1
    return cutRodRecur(n, price)


# Approach 2: Memoization (Top-Down)
def cutRodMemo(i, price, dp):
    if i == 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    ans = 0
    for j in range(1, i + 1):
        ans = max(ans, price[j] + cutRodMemo(i - j, price, dp))
    dp[i] = ans
    return ans


def cutRod_memo(price):
    n = len(price) - 1
    dp = [-1] * (n + 1)
    return cutRodMemo(n, price, dp)


# Approach 3: Bottom-Up (Tabulation)
def cutRod_bottomup(price):
    n = len(price) - 1
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], price[j] + dp[i - j])
    return dp[n]


if __name__ == "__main__":
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    print("=== ROD CUTTING ===")
    print("Recursion:", cutRod_recursion(price))
    print("Memoization:", cutRod_memo(price))
    print("Bottom-Up:", cutRod_bottomup(price))


# ══════════════════════════════════════════════════════════════════════════════
# COIN CHANGE 1 — COUNT WAYS (LC 518)
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def countWaysRecur(coins, n, sum):
    if sum == 0:
        return 1
    if sum < 0 or n == 0:
        return 0
    return countWaysRecur(coins, n, sum - coins[n - 1]) + \
           countWaysRecur(coins, n - 1, sum)


def coinWays_recursion(coins, sum):
    return countWaysRecur(coins, len(coins), sum)


# Approach 2: Memoization (Top-Down)
def countWaysMemo(coins, n, sum, dp):
    if sum == 0:
        return 1
    if sum < 0 or n == 0:
        return 0
    if dp[n-1][sum] != -1:
        return dp[n-1][sum]
    dp[n-1][sum] = (
        countWaysMemo(coins, n, sum - coins[n-1], dp) +
        countWaysMemo(coins, n - 1, sum, dp)
    )
    return dp[n-1][sum]


def coinWays_memo(coins, sum):
    dp = [[-1] * (sum + 1) for _ in range(len(coins))]
    return countWaysMemo(coins, len(coins), sum, dp)


# Approach 3: Bottom-Up (Tabulation)
def coinWays_bottomup(coins, sum):
    n = len(coins)
    dp = [[0] * (sum + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(sum + 1):
            dp[i][j] += dp[i - 1][j]
            if j - coins[i - 1] >= 0:
                dp[i][j] += dp[i][j - coins[i - 1]]
    return dp[n][sum]


# Approach 4: Space Optimized
def coinWays_optimized(coins, sum):
    n = len(coins)
    dp = [0] * (sum + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], sum + 1):
            dp[j] += dp[j - coins[i]]
    return dp[sum]


if __name__ == "__main__":
    coins = [1, 2, 3]
    target = 5
    print("\n=== COIN CHANGE WAYS (LC 518) ===")
    print("Recursion:", coinWays_recursion(coins, target))
    print("Memoization:", coinWays_memo(coins, target))
    print("Bottom-Up:", coinWays_bottomup(coins, target))
    print("Space Optimized:", coinWays_optimized(coins, target))


# ══════════════════════════════════════════════════════════════════════════════
# COIN CHANGE 2 — MINIMUM COINS (LC 322)
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def minCoinsRecur(i, sum, coins):
    if sum == 0:
        return 0
    if sum < 0 or i == len(coins):
        return float('inf')
    take = float('inf')
    if coins[i] > 0:
        take = minCoinsRecur(i, sum - coins[i], coins)
        if take != float('inf'):
            take += 1
    noTake = minCoinsRecur(i + 1, sum, coins)
    return min(take, noTake)


def coinMin_recursion(coins, sum):
    ans = minCoinsRecur(0, sum, coins)
    return ans if ans != float('inf') else -1


# Approach 2: Memoization (Top-Down)
def minCoinsMemo(i, sum, coins, memo):
    if sum == 0:
        return 0
    if sum < 0 or i == len(coins):
        return float('inf')
    if memo[i][sum] != -1:
        return memo[i][sum]
    take = float('inf')
    if coins[i] > 0:
        take = minCoinsMemo(i, sum - coins[i], coins, memo)
        if take != float('inf'):
            take += 1
    noTake = minCoinsMemo(i + 1, sum, coins, memo)
    memo[i][sum] = min(take, noTake)
    return memo[i][sum]


def coinMin_memo(coins, sum):
    memo = [[-1] * (sum + 1) for _ in range(len(coins))]
    ans = minCoinsMemo(0, sum, coins, memo)
    return ans if ans != float('inf') else -1


# Approach 3: Bottom-Up (Tabulation)
def coinMin_bottomup(coins, sum):
    n = len(coins)
    dp = [[0] * (sum + 1) for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(1, sum + 1):
            dp[i][j] = float('inf')
            take = float('inf')
            noTake = float('inf')
            if j - coins[i] >= 0:
                take = dp[i][j - coins[i]]
                if take != float('inf'):
                    take += 1
            if i + 1 < n:
                noTake = dp[i + 1][j]
            dp[i][j] = min(take, noTake)
    return dp[0][sum] if dp[0][sum] != float('inf') else -1


# Approach 4: Space Optimized
def coinMin_optimized(coins, sum):
    dp = [float('inf')] * (sum + 1)
    dp[0] = 0
    for i in range(len(coins) - 1, -1, -1):
        for j in range(1, sum + 1):
            take = float('inf')
            noTake = float('inf')
            if j - coins[i] >= 0 and coins[i] > 0:
                take = dp[j - coins[i]]
                if take != float('inf'):
                    take += 1
            if i + 1 < len(coins):
                noTake = dp[j]
            dp[j] = min(take, noTake)
    return dp[sum] if dp[sum] != float('inf') else -1


if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    target = 19
    print("\n=== COIN CHANGE MIN (LC 322) ===")
    print("Recursion:", coinMin_recursion(coins, target))
    print("Memoization:", coinMin_memo(coins, target))
    print("Bottom-Up:", coinMin_bottomup(coins, target))
    print("Space Optimized:", coinMin_optimized(coins, target))


# ══════════════════════════════════════════════════════════════════════════════
# PERFECT SQUARES (LC 279)
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def numSqRecur(i, n, squares):
    if n == 0:
        return 0
    if n < 0 or i == len(squares):
        return float('inf')
    take = float('inf')
    if squares[i] <= n:
        take = numSqRecur(i, n - squares[i], squares)
        if take != float('inf'):
            take += 1
    noTake = numSqRecur(i + 1, n, squares)
    return min(take, noTake)


def perfectSq_recursion(n):
    squares = [i*i for i in range(1, int(n**0.5) + 1)]
    return numSqRecur(0, n, squares)


# Approach 2: Memoization (Top-Down)
def numSqMemo(i, n, squares, memo):
    if n == 0:
        return 0
    if n < 0 or i == len(squares):
        return float('inf')
    if memo[i][n] != -1:
        return memo[i][n]
    take = float('inf')
    if squares[i] <= n:
        take = numSqMemo(i, n - squares[i], squares, memo)
        if take != float('inf'):
            take += 1
    noTake = numSqMemo(i + 1, n, squares, memo)
    memo[i][n] = min(take, noTake)
    return memo[i][n]


def perfectSq_memo(n):
    squares = [i*i for i in range(1, int(n**0.5) + 1)]
    memo = [[-1] * (n + 1) for _ in range(len(squares))]
    return numSqMemo(0, n, squares, memo)


# Approach 3: Bottom-Up (Space Optimized)
def perfectSq_bottomup(n):
    squares = [i*i for i in range(1, int(n**0.5) + 1)]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(len(squares)):
        for j in range(squares[i], n + 1):
            dp[j] = min(dp[j], 1 + dp[j - squares[i]])
    return dp[n]


if __name__ == "__main__":
    n = 12
    print("\n=== PERFECT SQUARES (LC 279) ===")
    print("Recursion n=12:", perfectSq_recursion(n))
    print("Memoization n=12:", perfectSq_memo(n))
    print("Bottom-Up n=12:", perfectSq_bottomup(n))


# ══════════════════════════════════════════════════════════════════════════════
# MAXIMUM RIBBON CUT
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def ribbonRecur(i, n, cuts):
    if n == 0:
        return 0
    if n < 0 or i == len(cuts):
        return float('-inf')
    take = float('-inf')
    if cuts[i] <= n:
        take = ribbonRecur(i, n - cuts[i], cuts)
        if take != float('-inf'):
            take += 1
    noTake = ribbonRecur(i + 1, n, cuts)
    return max(take, noTake)


def ribbon_recursion(n, cuts):
    ans = ribbonRecur(0, n, cuts)
    return ans if ans != float('-inf') else -1


# Approach 2: Memoization (Top-Down)
def ribbonMemo(i, n, cuts, memo):
    if n == 0:
        return 0
    if n < 0 or i == len(cuts):
        return float('-inf')
    if memo[i][n] != -1:
        return memo[i][n]
    take = float('-inf')
    if cuts[i] <= n:
        take = ribbonMemo(i, n - cuts[i], cuts, memo)
        if take != float('-inf'):
            take += 1
    noTake = ribbonMemo(i + 1, n, cuts, memo)
    memo[i][n] = max(take, noTake)
    return memo[i][n]


def ribbon_memo(n, cuts):
    memo = [[-1] * (n + 1) for _ in range(len(cuts))]
    ans = ribbonMemo(0, n, cuts, memo)
    return ans if ans != float('-inf') else -1


# Approach 3: Bottom-Up (Space Optimized)
def ribbon_bottomup(n, cuts):
    dp = [float('-inf')] * (n + 1)
    dp[0] = 0
    for i in range(len(cuts)):
        for j in range(cuts[i], n + 1):
            if dp[j - cuts[i]] != float('-inf'):
                dp[j] = max(dp[j], 1 + dp[j - cuts[i]])
    return dp[n] if dp[n] != float('-inf') else -1


if __name__ == "__main__":
    print("\n=== MAXIMUM RIBBON CUT ===")
    print("Recursion n=7:", ribbon_recursion(7, [2, 3]))
    print("Memoization n=7:", ribbon_memo(7, [2, 3]))
    print("Bottom-Up n=7:", ribbon_bottomup(7, [2, 3]))


# ══════════════════════════════════════════════════════════════════════════════
# INTEGER BREAK (LC 343)
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def intBreakRecur(n):
    if n == 1:
        return 1
    ans = 0
    for j in range(1, n):
        ans = max(ans, j * max(n - j, intBreakRecur(n - j)))
    return ans


# Approach 2: Memoization (Top-Down)
def intBreakMemo(n, memo):
    if n == 1:
        return 1
    if memo[n] != -1:
        return memo[n]
    ans = 0
    for j in range(1, n):
        ans = max(ans, j * max(n - j, intBreakMemo(n - j, memo)))
    memo[n] = ans
    return ans


def intBreak_memo(n):
    memo = [-1] * (n + 1)
    return intBreakMemo(n, memo)


# Approach 3: Bottom-Up (Tabulation)
def intBreak_bottomup(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * max(i - j, dp[i - j]))
    return dp[n]


if __name__ == "__main__":
    n = 10
    print("\n=== INTEGER BREAK (LC 343) ===")
    print("Recursion n=10:", intBreakRecur(n))
    print("Memoization n=10:", intBreak_memo(n))
    print("Bottom-Up n=10:", intBreak_bottomup(n))


# ══════════════════════════════════════════════════════════════════════════════
# MINIMUM COST FOR TICKETS (LC 983)
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def ticketsRecur(idx, days, costs):
    n = len(days)
    durations = [1, 7, 30]
    if idx >= n:
        return 0
    ans = float('inf')
    for k in range(3):
        j = idx
        while j < n and days[j] < days[idx] + durations[k]:
            j += 1
        ans = min(ans, costs[k] + ticketsRecur(j, days, costs))
    return ans


def tickets_recursion(days, costs):
    return ticketsRecur(0, days, costs)


# Approach 2: Memoization (Top-Down)
def ticketsMemo(idx, days, costs, memo):
    n = len(days)
    durations = [1, 7, 30]
    if idx >= n:
        return 0
    if memo[idx] != -1:
        return memo[idx]
    ans = float('inf')
    for k in range(3):
        j = idx
        while j < n and days[j] < days[idx] + durations[k]:
            j += 1
        ans = min(ans, costs[k] + ticketsMemo(j, days, costs, memo))
    memo[idx] = ans
    return ans


def tickets_memo(days, costs):
    memo = [-1] * len(days)
    return ticketsMemo(0, days, costs, memo)


# Approach 3: Bottom-Up (Tabulation)
def tickets_bottomup(days, costs):
    last_day = days[-1]
    travel_days = set(days)
    dp = [0] * (last_day + 1)
    for i in range(1, last_day + 1):
        if i not in travel_days:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(
                dp[max(0, i - 1)] + costs[0],
                dp[max(0, i - 7)] + costs[1],
                dp[max(0, i - 30)] + costs[2]
            )
    return dp[last_day]


if __name__ == "__main__":
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print("\n=== MINIMUM COST FOR TICKETS (LC 983) ===")
    print("Recursion:", tickets_recursion(days, costs))
    print("Memoization:", tickets_memo(days, costs))
    print("Bottom-Up:", tickets_bottomup(days, costs))


# ══════════════════════════════════════════════════════════════════════════════
# WORD BREAK (LC 139)
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def wordBreakRecur(start, s, wordSet):
    if start == len(s):
        return True
    for end in range(start + 1, len(s) + 1):
        if s[start:end] in wordSet and wordBreakRecur(end, s, wordSet):
            return True
    return False


def wordBreak_recursion(s, wordDict):
    wordSet = set(wordDict)
    return wordBreakRecur(0, s, wordSet)


# Approach 2: Memoization (Top-Down)
def wordBreakMemo(start, s, wordSet, memo):
    if start == len(s):
        return True
    if memo[start] != -1:
        return memo[start]
    for end in range(start + 1, len(s) + 1):
        if s[start:end] in wordSet and wordBreakMemo(end, s, wordSet, memo):
            memo[start] = True
            return True
    memo[start] = False
    return False


def wordBreak_memo(s, wordDict):
    wordSet = set(wordDict)
    memo = [-1] * len(s)
    return wordBreakMemo(0, s, wordSet, memo)


# Approach 3: Bottom-Up (Tabulation)
def wordBreak_bottomup(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[n]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print("\n=== WORD BREAK (LC 139) ===")
    print("Recursion:", wordBreak_recursion(s, wordDict))
    print("Memoization:", wordBreak_memo(s, wordDict))
    print("Bottom-Up:", wordBreak_bottomup(s, wordDict))


# ══════════════════════════════════════════════════════════════════════════════
# COMBINATION SUM IV (LC 377)
# ══════════════════════════════════════════════════════════════════════════════

# Approach 1: Recursion
def comboRecur(nums, target):
    if target == 0:
        return 1
    if target < 0:
        return 0
    count = 0
    for num in nums:
        count += comboRecur(nums, target - num)
    return count


def combo_recursion(nums, target):
    return comboRecur(nums, target)


# Approach 2: Memoization (Top-Down)
def comboMemo(nums, target, memo):
    if target == 0:
        return 1
    if target < 0:
        return 0
    if memo[target] != -1:
        return memo[target]
    count = 0
    for num in nums:
        count += comboMemo(nums, target - num, memo)
    memo[target] = count
    return count


def combo_memo(nums, target):
    memo = [-1] * (target + 1)
    return comboMemo(nums, target, memo)


# Approach 3: Bottom-Up (Tabulation)
def combo_bottomup(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for j in range(1, target + 1):
        for num in nums:
            if j - num >= 0:
                dp[j] += dp[j - num]
    return dp[target]


if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 4
    print("\n=== COMBINATION SUM IV (LC 377) ===")
    print("Recursion:", combo_recursion(nums, target))
    print("Memoization:", combo_memo(nums, target))
    print("Bottom-Up:", combo_bottomup(nums, target))
