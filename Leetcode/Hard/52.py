class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col, queens):
            for prev_row, prev_col in queens:
                if prev_col == col or \
                        abs(prev_row - row) == abs(prev_col - col):
                    return False
            return True

        def solve(row, queens):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if is_not_under_attack(row, col, queens):
                    queens.append((row, col))
                    solve(row + 1, queens)
                    queens.pop()

        count = 0
        solve(0, [])
        return count
