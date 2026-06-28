class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        first_row_contains_0 = False 
        first_col_contains_0 = False 

        for c in range(COLS):
            if matrix[0][c] == 0:
                first_row_contains_0 = True 
                break 
        
        for r in range(ROWS):
            if matrix[r][0] == 0:
                first_col_contains_0 = True 
                break 
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 
                    matrix[r][0] = 0 
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0 
        if first_row_contains_0:
            for c in range(COLS):
                matrix[0][c] = 0 
        if first_col_contains_0:
            for r in range(ROWS):
                matrix[r][0] = 0