'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Precondition:
At least one 0
m >= 1
n >= 1
Only 0, 1

Postcondition:
matrix can be changed in place
return the changed matrix

C1: Only one 0
C2: m = n = 1
C3: More 0

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0]]
Output: [[0]]

Input:
mat= [[1,0][1,1]]
Output: [[1,0][1,1]]

Algo:
BFS, add all 0 first and set all others -1
starting from 0, conduct BFS, everytime the new cell's value = old cells' value + 1

Runtime: O(mn)
Space: O(mn)

'''
class Solution:
    DIRECTION = [(1,0), (0,1), (-1,0), (0,-1)]
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        queue = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1
        
        while queue:
            r, c = queue.popleft()
            for direction in Solution.DIRECTION:
                new_r, new_c = r + direction[0], c + direction[1]
                if new_r < 0 or new_r == m or new_c < 0 or new_c == n or mat[new_r][new_c] != -1: continue
                mat[new_r][new_c] = mat[r][c] + 1
                queue.append((new_r, new_c))
        return mat