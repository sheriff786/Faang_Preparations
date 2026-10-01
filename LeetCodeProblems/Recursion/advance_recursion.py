'''
N queens problem with brute force solution

'''
class Solution:

    def isSafe(self, board, row, col, n):

        # Horizontal
        for j in range(n):
            if board[row][j] == 'Q':
                return False

        # Vertical
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        # Left Diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Right Diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True


    def nQueens(self, board, row, n, ans):

        # Base Case
        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for col in range(n):

            if self.isSafe(board, row, col, n):

                board[row][col] = 'Q'

                self.nQueens(board, row + 1, n, ans)

                board[row][col] = '.'


    def solveNQueens(self, n):

        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        self.nQueens(board, 0, n, ans)

        return ans
n=4
s=Solution()
print(s.solveNQueens(n))


'''Time complexity is O(!n)'''

'''optimize solution'''

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # Stores occupied columns
        col = set()

        # Stores occupied positive diagonals (row + col)
        posDiag = set()

        # Stores occupied negative diagonals (row - col)
        negDiag = set()

        res = []

        # Create empty board
        board = [["."] * n for _ in range(n)]

        def backtrack(r):

            # Base Case
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # Try every column in the current row
            for c in range(n):

                # Check if queen can be placed
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place Queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Move to next row
                backtrack(r + 1)

                # Backtrack
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)

        return res
    
'''
Sudoku

Problem
  
Sudoku Solver
Given a partially filled two-dimensional array, fill all the unfilled cells such that each row, each column and each 3 x 3 subgrid (as highlighted below by bolder lines) has every digit from 1 to 9 exactly once.

Unfilled cells have a value of 0 on the given board.

Example
Example one

{
"board": [
[8, 4, 9, 0, 0, 3, 5, 7, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 0, 9, 0, 0, 8, 3],
[0, 0, 0, 9, 4, 6, 7, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 4, 0],
[0, 0, 6, 8, 7, 2, 0, 0, 0],
[5, 7, 0, 0, 1, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 2, 1, 7, 0, 0, 8, 6, 5]
]
}
Output:

[
[8, 4, 9, 1, 6, 3, 5, 7, 2],
[3, 1, 5, 2, 8, 7, 4, 9, 6],
[7, 6, 2, 4, 9, 5, 1, 8, 3],
[1, 5, 3, 9, 4, 6, 7, 2, 8],
[2, 8, 7, 3, 5, 1, 6, 4, 9],
[4, 9, 6, 8, 7, 2, 3, 5, 1],
[5, 7, 8, 6, 1, 9, 2, 3, 4],
[6, 3, 4, 5, 2, 8, 9, 1, 7],
[9, 2, 1, 7, 3, 4, 8, 6, 5]
]
Notes
You can assume that any given puzzle will have exactly one solution.

Constraints:

Size of the input array is exactly 9 x 9
0 <= value in the input array <= 9
'''
#solution

def solve_sudoku_puzzle(board):
    """
    Args:
        board(list_list_int32)
    Returns:
        list_list_int32
    """

    solve(board, 0, 0)

    return board


def solve(board, row, col):

    # Base Case
    if row == 9:
        return True

    # Find next cell
    next_row = row
    next_col = col + 1

    if next_col == 9:
        next_row = row + 1
        next_col = 0

    # Skip filled cell
    if board[row][col] != 0:
        return solve(board, next_row, next_col)

    # Try digits 1 to 9
    for digit in range(1, 10):

        if isSafe(board, row, col, digit):

            # Place digit
            board[row][col] = digit

            # Recurse
            if solve(board, next_row, next_col):
                return True

            # Backtrack
            board[row][col] = 0

    return False


def isSafe(board, row, col, digit):

    # Check Row
    for j in range(9):
        if board[row][j] == digit:
            return False

    # Check Column
    for i in range(9):
        if board[i][col] == digit:
            return False

    # Check 3 x 3 Grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == digit:
                return False

    return True

'''
Word Search
Medium
Topics
Company Tags
Hints
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
Example 2:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
Constraints:

1 <= board.length, board[i].length <= 5
1 <= word.length <= 10
board and word consists of only lowercase and uppercase English letters.


'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

