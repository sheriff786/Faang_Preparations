'''


Problem
  
How Many Binary Search Trees With N Nodes
Write a function that returns the number of distinct binary search trees that can be constructed with n nodes. For the purpose of this exercise, do solve the problem using recursion first even if you see some non-recursive approaches.

Example One
{
"n": 1
}
Output:

1
Example Two
{
"n": 2
}
Output:

2
Suppose the values are 1 and 2, then the two trees that are possible are

   (2)            (1)
  /       and       \
(1)                  (2)
Example Three
{
"n": 3
}
Output:

5
Suppose the values are 1, 2, 3 then the possible trees are

       (3)
      /
    (2)
   /
(1)

   (3)
  /
(1)
   \
   (2)

(1)
   \
    (2)
      \
       (3)

(1)
   \
    (3)
   /
(2)

   (2)
  /   \
(1)    (3)
Notes
Constraints:

1 <= n <= 16
'''


def how_many_bsts(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    total = count_bst(n)
    return total
def count_bst(n):
    # base cases
    if n == 0 or n == 1:
        return 1

    total = 0

    # try each node as root
    for root in range(1, n + 1):
        left = count_bst(root - 1)
        right = count_bst(n - root)

        total += left * right

    return total

'''
Memorize dp version
'''
def how_many_bsts(n):
    dp = [-1] * (n + 1)

    def count_bst(n):

        # Base case
        if n == 0 or n == 1:
            return 1

        # Already calculated?
        if dp[n] != -1:
            return dp[n]

        total = 0

        # Try every node as root
        for root in range(1, n + 1):

            left = count_bst(root - 1)
            right = count_bst(n - root)

            total += left * right

        # Store answer
        dp[n] = total

        return dp[n]

    return count_bst(n)

'''bottom up'''
def how_many_bsts(n):

    dp = [0] * (n + 1)

    # Base case
    dp[0] = 1

    if n >= 1:
        dp[1] = 1

    # Calculate from smaller problems
    for nodes in range(2, n + 1):

        total = 0

        # Try every node as root
        for root in range(1, nodes + 1):

            left = root - 1
            right = nodes - root

            total += dp[left] * dp[right]

        dp[nodes] = total

    return dp[n]

'''
Power question
Problem
  
Power
Given a base a and an exponent b. Your task is to find ab. The value could be large enough. So, calculate ab % 1000000007.

Example
{
"a": 2,
"b": 10
}
Output:

1024
Notes
Constraints:

0 <= a <= 104
0 <= b <= 109
a and b together won't be 0

'''
def calculate_power(a, b):
    MOD = 1000000007
    


# def power(base, exp, mod):
#     # base case
#     if exp == 0:
#         return 1

#     # recursive case
#     if exp % 2 == 0:
#         half = power(base, exp // 2, mod)
#         return (half * half) % mod
#     else:
#         return (base * power(base, exp - 1, mod)) % mod
    def power(a,b):
        
        if b==0:
            return 1
        half = power(a,b//2)
        if b%2 ==0:
            return (half*half)% MOD
        else:
            return (a*half*half)% MOD
    return power(a, b)

'''
tower of hanoi
Problem
  
Tower Of Hanoi
Tower of Hanoi is a mathematical puzzle where we have three pegs and n disks. The objective of the puzzle is to move the entire stack to another peg, obeying the following simple rules:

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.
Given n denoting the number of disks in the first peg, return all the steps required to move all disks from the first peg to the third peg in minimal number of steps.

Example
{
"n": 4
}
Output:

[
[1, 2],
[1, 3],
[2, 3],
[1, 2],
[3, 1],
[3, 2],
[1, 2],
[1, 3],
[2, 3],
[2, 1],
[3, 1],
[2, 3],
[1, 2],
[1, 3],
[2, 3]
]
Following steps:

[1, 2] = Shift top disk of the first peg to top of the second peg.
Picture after this step will be:
First peg: 2 3 4
Second peg: 1
Third peg: Empty

[1, 3] = Shift top disk of the first peg to top of the third peg.
Picture after this step will be:
First peg: 3 4
Second peg: 1
Third peg: 2

Similarly after following remaining steps, the final configuration will be:
First peg: Empty
Second peg: Empty
Third peg: 1 2 3 4

Hence, our objective is achieved.

Notes
Return a 2d integer array containing all the steps taken to move all n disks from the first peg to the third peg in minimal number of steps. Each row will have two integers denoting from peg and to peg, for example, if the ith row is [2, 3], then it means in this step, we moved the top disk on peg 2 to peg 3.
Constraints:


'''

def tower_of_hanoi(n):
    from_ = 1
    to = 3
    aux = 2
    return helper(n, from_, to, aux)

def helper(n, from_, to, aux):
    if n == 0:
        return []
    
    result = []
    
    # Step 1
    result += helper(n-1, from_, aux, to)
    
    # Step 2
    result.append([from_, to])
    
    # Step 3
    result += helper(n-1, aux, to, from_)
    
    return result

'''
Wild card

'''
def find_all_possibilities(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
#     result = []
#     s = list(s)

#     solve(s, 0, result)
#     return result
    



# def solve(s, i, result):

#     # Base Case
#     if i == len(s):
#         result.append("".join(s))
#         return

#     # If current character is not '?'
#     if s[i] != '?':
#         solve(s, i + 1, result)
#         return

#     # Choice 1 : Replace with '0'
#     s[i] = '0'
#     solve(s, i + 1, result)

#     # Choice 2 : Replace with '1'
#     s[i] = '1'
#     solve(s, i + 1, result)

#     # Optional Backtrack
#     s[i] = '?'
    
# def generate_strings(s):
    result = []
    path = []

    def backtrack(index):

        # Base case
        if index == len(s):
            result.append("".join(path))
            return

        # Fixed character
        if s[index] != '?':
            path.append(s[index])

            backtrack(index + 1)

            path.pop()

        # Wildcard character
        else:

            # Choice 1: add '0'
            path.append('0')
            backtrack(index + 1)
            path.pop()

            # Choice 2: add '1'
            path.append('1')
            backtrack(index + 1)
            path.pop()

    backtrack(0)

    return result

'''
letter case permutation
Problem
  
Letter Case Permutation
Given a string, return all strings that can be generated by changing case of one or more letters in it.

Example One
{
"s": "a1z"
}
Output:

["A1Z", "A1z", "a1Z", "a1z"]
Example Two
{
"s": "123"
}
Output:

["123"]
Notes
Return strings in any order.

Constraints:

Input string may contain only: 'a'..'z', 'A'..'Z', '0'..'9'
1 <= length of the string <= 12

'''

def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    result = []

    # Convert string to list because strings are immutable
    s = list(s)

    def solve(s, i, result):

        # Base Case
        if i == len(s):
            result.append("".join(s))
            return

        # If current character is a digit
        if s[i].isdigit():
            solve(s, i + 1, result)
            return

        # Choice 1 : Lowercase
        s[i] = s[i].lower()
        solve(s, i + 1, result)

        # Choice 2 : Uppercase
        s[i] = s[i].upper()
        solve(s, i + 1, result)

    solve(s, 0, result)

    return result
'''
Generate All Subsets Of A Set
Generate ALL possible subsets of a given set. The set is given in the form of a string s containing distinct lowercase characters 'a' - 'z'.

Example
{
"s": "xy"
}
Output:

["", "x", "y", "xy"]
Notes
Any set is a subset of itself.
Empty set is a subset of any set.
Output contains ALL possible subsets of given string.
Order of strings in the output does not matter. E.g. s = "a", arrays ["", "a"] and ["a", ""] both will be accepted.
Order of characters in any subset must be same as in the input string. For s = "xy", array ["", "x", "y", "xy"] will be accepted, but ["", "x", "y", "yx"] will not be accepted.
Constraints:

0 <= length of s <= 19
s only contains distinct lowercase English letters.

'''
def generate_all_subsets(s):
    """
    Args:
        s(str)
    Returns:
        list_str
    """

    result = []

    def solve(i, current):

        # Base Case
        if i == len(s):
            result.append("".join(current))
            return

        # Include
        current.append(s[i])
        solve(i + 1, current)
        current.pop()

        # Exclude
        solve(i + 1, current)

    solve(0, [])

    return result

'''
Problem
  
N Choose K Combinations
Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.

Example One
{
"n": 5,
"k": 2
}
Output:

[
[1, 2],
[1, 3],
[1, 4],
[1, 5],
[2, 3],
[2, 4],
[2, 5],
[3, 4],
[3, 5],
[4, 5]
]
Example Two
{
"n": 6,
"k": 6
}
Output:

[
[1, 2, 3, 4, 5, 6]
]
Notes
The answer can be returned in any order.

Constraints:

1 <= n <= 20
1 <= k <= n

'''

def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    res = []

    def solve(i, comb):

        # Got k elements
        if len(comb) == k:
            res.append(comb[:])
            return

        # No more numbers left
        if i > n:
            return

        # Include current number
        comb.append(i)
        solve(i + 1, comb)

        # Exclude current number
        comb.pop()
        solve(i + 1, comb)

    solve(1, [])
    return res
    
#Iterative approach
def combine(n, k):
    result = [[]]

    for num in range(1, n + 1):
        new_combinations = []

        for combination in result:
            if len(combination) < k:
                new_combinations.append(combination + [num])

        result += new_combinations

    return [x for x in result if len(x) == k]
    
#iterative approach 2
def combine(n, k):
    result = []

    stack = [([], 1)]

    while stack:
        path, start = stack.pop()

        if len(path) == k:
            result.append(path)
            continue

        for i in range(start, n + 1):
            stack.append((path + [i], i + 1))

    return result

'''generate-all_expressions'''

def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    # Write your code here.
    result = []

    def backtracking(i, expression, value, last):
        # Base case
        if i == len(s):
            if value == target:
                result.append(expression)
            return

        # Try every possible number starting from s[i]
        for j in range(i, len(s)):
            number = int(s[i:j+1])

            # First number — no operator before it
            if i == 0:
                backtracking(
                    j + 1,
                    s[i:j+1],
                    number,
                    number
                )

            else:
                # Choice 1: +
                backtracking(
                    j + 1,
                    expression + "+" + s[i:j+1],
                    value + number,
                    number
                )

                # Choice 2: *
                backtracking(
                    j + 1,
                    expression + "*" + s[i:j+1],
                    value - last + last * number,
                    last * number
                )

    backtracking(0, "", 0, 0)
    return result


'''
Recursion phone word problem

Problem
  
Words From Phone Number
Given a seven-digit phone number, return all the character combinations that can be generated according to the following mapping:

Graph

Return the combinations in the lexicographical order.

Example One
{
"phone_number": "1234567"
}
Output:

[
"adgjmp",
"adgjmq",
"adgjmr",
"adgjms",
"adgjnp",
...
"cfilns",
"cfilop",
"cfiloq",
"cfilor",
"cfilos"
]
First string "adgjmp" in the first line comes from the first characters mapped to digits 2, 3, 4, 5, 6 and 7 respectively. Since digit 1 maps to nothing, nothing is appended before 'a'. Similarly, the fifth string "adgjnp" generated from first characters of 2, 3, 4, 5 second character of 6 and first character of 7. All combinations generated in such a way must be returned in the lexicographical order.

Example Two
{
"phone_number": "1010101"
}
Output:

[""]
Notes
Return an array of the generated string combinations in the lexicographical order. If nothing can be generated, return a list with an empty string "".
Digits 0 and 1 map to nothing. Other digits map to either three or four different characters each.
Constraints:

Input string is 7 characters long; each character is a digit.

'''


def get_words_from_phone_number(phone_number):
    """
    Args:
     phone_number(str)
    Returns:
     list_str
    """
    # Write your code here.

    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []
    state = []

    def backtracking(i):

        # Base case
        if i == len(phone_number):
            result.append("".join(state))
            return

        digit = phone_number[i]

        # Digit 0 or 1 → no characters
        if digit not in mapping:
            backtracking(i + 1)
            return

        # Try every character mapped to this digit
        for character in mapping[digit]:

            # Make choice
            state.append(character)

            # Explore
            backtracking(i + 1)

            # Undo choice
            state.pop()

    backtracking(0)

    return result




