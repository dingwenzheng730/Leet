import unittest
'''
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Postcondition:
m,n >= 1
only X and .
only 1*k and k*1, no adjacent

Postcondition:
board stayed unchanged
return int

C1: 0 ship
C2: 1 ship
C3: horizontal ship
C4: vertical ship
C5: combined

Algo:
check each cell, use the left-most or top-most X to count
Runtime: O(mn)
Space: O(1)
'''
class Solution:
    SHIPMARK = 'X'
    EMPTYMARK = '.'
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != Solution.SHIPMARK:
                    continue
                if i >= 1 and board[i-1][j] == Solution.SHIPMARK:
                    continue
                if j >= 1 and board[i][j-1] == Solution.SHIPMARK:
                    continue
                count += 1
        return count

class BattleShipTest(unittest.TestCase):
    def test_zero_ship(self):
        board = [[".",".",".","."],[".",".",".","."],[".",".",".","."]]
        s = Solution()
        result = s.countBattleships(board)
        self.assertEqual(result, 0)

    def test_combined_ship(self):
        board = [[".","X",".","."],[".",".","X","."],[".",".","X","."]]
        s = Solution()
        result = s.countBattleships(board)
        self.assertEqual(result, 2)

    def test_one_ship(self):
        board = [[".","X",".","."],[".",".",".","."],[".",".",".","."]]
        s = Solution()
        result = s.countBattleships(board)
        self.assertEqual(result, 1)




if __name__ == '__main__':
    unittest.main()