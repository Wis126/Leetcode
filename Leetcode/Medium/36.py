class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Kiểm tra mỗi hàng
        for row in board:
            seen = set()
            for digit in row:
                if digit != '.':
                    if digit in seen:
                        return False
                    seen.add(digit)

        # Kiểm tra mỗi cột
        for col in range(9):
            seen = set()
            for row in board:
                digit = row[col]
                if digit != '.':
                    if digit in seen:
                        return False
                    seen.add(digit)

        # Kiểm tra mỗi ô 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        digit = board[x][y]
                        if digit != '.':
                            if digit in seen:
                                return False
                            seen.add(digit)

        return True