import unittest
'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Precondition:
len(word) = k
k >= 1
m >= 1
n >= 1
only upper case english word for board and word

Postcondition:
board stay unchanged
return bool

C1: no enough words in board 
C2: search return true
C3: search return false

Algo:
DFS: according to first char, conduct DFS for these cells
Runtime: O(nm*3^k)
Space: O(k)
'''
class Solution:
    def exist(self, board, word):
        r_size = len(board)
        c_size = len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def dfs(r, c, remain):
            result = False
            if len(remain) == 0:
                return True
            if r >= r_size or r < 0 or c >= c_size or c < 0 or board[r][c] != remain[0]:
                return False
            temp = board[r][c]
            board[r][c] = '#'
            for direction in directions:
                if dfs(r+direction[0], c+direction[1], remain[1:]):
                    result = True
                    break
            board[r][c] = temp
            return result
        
        for row in range(r_size):
            for col in range(c_size):
                if board[row][col] == word[0]:
                    if dfs(row, col, word):
                        return True 
        return False

class SolutionTest(unittest.TestCase):
    def test_search_success(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        s = Solution()
        result = s.exist(board, word)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()