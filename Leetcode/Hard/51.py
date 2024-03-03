from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for prev_row in range(row):
                prev_col = board[prev_row]
                if prev_col == col or \
                   prev_col - prev_row == col - row or \
                   prev_col + prev_row == col + row:
                    return False
            return True

        def place_queen(board, row):
            if row == n:
                result.append(["".join(["Q" if c == col else "." for col in range(n)]) for row, c in enumerate(board)])
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    place_queen(board, row + 1)
                    board[row] = -1

        result = []
        board = [-1] * n
        place_queen(board, 0)
        return result