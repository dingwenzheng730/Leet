'''
Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of black lonely pixels.

A black lonely pixel is a character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.

Input: picture = [["W"]]
Output: 0 

Input: picture = [["B"]]
Output: 1 

Input:
Output:

Precondition: 
m >=1, n >= 1
cell is 'B' or 'W'

C1: only one cell
C2: No B return 0
C3: exists lonely B
C4: No lonely B

Algo: 
get number of B for each row and col O(mn)
for each B on the map, check if that's the only one O(mn)

Runtime: O(mn)
Space: O(m+n)
'''
class Solution:
    def __init__(self):
        self.BLACK = 'B'
        self.WHITE = 'W'
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])

        row_b_count = [0 for _ in range(m)]
        col_b_count = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if picture[i][j] == self.BLACK:
                    row_b_count[i] += 1
                    col_b_count[j] += 1

        result = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == self.BLACK and row_b_count[i] == 1 and col_b_count[j] == 1:
                    result += 1
        return result
