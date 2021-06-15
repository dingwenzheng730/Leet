class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        '''
        if grid[0][0] == 1:
            return -1
            
        n = len(grid)
        queue = deque([])
        queue.append((0, 0, 0))
        visited = set()

        while queue:
            curr_entry = queue.popleft()
            curr_lev = curr_entry[-1]
            curr_cell = curr_entry[0:2] 
            visited.add(curr_cell)
            for direction in Solution.DIRECTIONS:
                new_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
                if new_cell == (n-1, n-1):
                    return curr_lev + 1
                elif 0 <= new_cell[0] < n and 0 <= new_cell[1] < n and new_cell not in visited and grid[new_cell[0]][new_cell[1]] == 0:
                    new_entry = (new_cell[0], new_cell[1], curr_lev + 1)
                    queue.append(new_entry)
        return -1

