class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        '''
        C1: No food
        C2: No/One cell No possible
        starting from me, use queue to conduct BFS, mark the cell with the steps(since we don't go back to previously travelled cells), if we find food, return steps, or -1 if all cells are passed
        '''
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        me_cell = (0, 0)
        m = len(grid[0])
        n = len(grid[1])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    me_cell = (i, j)
        
        queue = deque([me_cell])
        grid[my_cell[0]][my_cell[1]] = 0
        while queue:
            r, c = queue.popleft()
            if grid[r][c] == "#":
                return grid[r][c]
            for direction in directions:
                new_row = r + direction[0]
                new_col = c + direction[1]
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == "O" or grid[new_row][new_col] == "#":
                    grid[new_row][new_col] = grid[r][c] + 1
                    queue.append((new_row, new_col))
                
                
                

