'''
In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Input: grid = [[0,1],[1,0]]
Output: 1

Input: grid = [[0, 1, 1][0, 0, 0][1, 0, 0]]
Output: 2

Input: grid[[1,1,1,0][1,1,1,0][1,1,1,0][0,0,0,1]]
Output: 1

Precondition:
result >= 1
grid size: m * n
m >= 2
n >= 2

C1: Min size
C2: Single cell islands
C3: General Case
C4: islands bigger than 3*3

Runtime: O(mn)
Space: O(mn)
'''

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r,c):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] != 1:
                return
            grid[r][c] = 2
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1) 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
            else: 
                continue
            break

        # BFS
        min_distance = 0
        queue = deque([(r,c,min_distance) for r in range(m) for c in range(n) if grid[r][c] == 2])  
        seen = set()
        while queue:
            r, c, min_distance = queue.popleft()
            new_location = [(r,c+1),(r,c-1),(r-1,c),(r+1,c)]
            for new_r, new_c in new_location:
                if new_r in range(m) and new_c in range(n) and (new_r,new_c) not in seen:
                    if grid[new_r][new_c] == 1:
                        return min_distance
                    queue.append((new_r, new_c, min_distance+1))
                    seen.add((new_r,new_c))



        