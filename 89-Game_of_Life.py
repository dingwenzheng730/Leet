class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        C1: empty board
        C2: 1 cell board
        """
        rows = len(board)
        cols = len(board[0])
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        directions = [(1,1)(-1,-1)(1,-1)(-1,1)(0,1)(0,-1)(1,0)(-1,0)]
        for i in range(rows):
            for j in range(cols):
                nearby_count = 0
                for direction in directions:    
                    if 0 <= i + direction[0] < n and 0 <= j + direction[1] < n and if copy_board[i+direction[0]][j+direction[1]] == 1:
                        nearby_count += 1
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1


