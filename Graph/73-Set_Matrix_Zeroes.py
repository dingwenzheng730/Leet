'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: [1]
Output: [1]

Input: [[1,1],[1,1]]
Output: [[1,1],[1,1]]

Precondition:
m,n >= 1

C1: single cell matrix
C2: No zero at all
C3: Mult zero

Algo:
loop over to get all row and col that needs to set to be 0
set them to 0 according to the set
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row_set = set()
        col_set = set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row_set.add(r)
                    col_set.add(c)
        
        for row in row_set:
            for col in range(n):
                matrix[row][col] = 0

        for col in col_set:
            for row in range(m):
                matrix[row][col] = 0
        
