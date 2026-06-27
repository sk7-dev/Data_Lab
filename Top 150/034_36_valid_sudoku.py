class Solution:
    def isValidSudoku(self, board):
        row_records = [set() for _ in range(9)]
        column_records = [set() for _ in range(9)]
        box_records = [set() for _ in range(9)]

        for row_index in range(9):
            for column_index in range(9):
                current_symbol = board[row_index][column_index]

                if current_symbol == ".":
                    continue

                box_index = (row_index // 3) * 3 + (column_index // 3)

                if (
                    current_symbol in row_records[row_index]
                    or current_symbol in column_records[column_index]
                    or current_symbol in box_records[box_index]
                ):
                    return False

                row_records[row_index].add(current_symbol)
                column_records[column_index].add(current_symbol)
                box_records[box_index].add(current_symbol)

        return True