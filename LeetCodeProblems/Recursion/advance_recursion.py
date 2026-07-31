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