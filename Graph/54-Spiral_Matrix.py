'''Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Precondition: m, n >= 1
              no overflow for int in the matrix

C1: single cell
C2: Square
C3: Not Square

Simulation
Runtime: O(mn)
Space: O(mn)

class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
'''
class Solution:
    DIRECTION_ROW = [0, 1, 0, -1]
    DIRECTION_COL = [1, 0, -1, 0]
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        seen = set()
        result = []
        r = c = direction = 0 
        for _ in range(R*C):
            result.append(matrix[r][c])
            seen.add((r,c))
            new_r, new_c = r + Solution.DIRECTION_ROW[direction], c + Solution.DIRECTION_COL[direction]
            if 0 <= new_r < R and 0 <= new_c < C and not (new_r,new_c) in seen:
                r, c = new_r, new_c
            else:
                direction = (direction + 1) % 4
                r, c = r + Solution.DIRECTION_ROW[direction], c + Solution.DIRECTION_COL[direction]
        return result


        
