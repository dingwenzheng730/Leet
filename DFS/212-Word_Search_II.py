import unittest
'''
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Precondition:
only lower case english words in board and words
size of board: m*n
size of words: k
max length of word: l
m >= 1, n>= 1, k>= 1
unique in words? Yes

Postcondition:
No changes for board and words
return list of str
Do not return repeat occured word

C1: return []
C2: return 1 word
C3: return more than 1
C4: Same word occurs more than once

Algo:
Brute Force: for each word in word list, try to search, using DFS
use trie to stop earier, conduct DFS for each cell on the board

Runtime: O(mn*3^l)
Space: O(nl)
'''
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ENDING = '$'
        MARKED = '#'
        DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]
        m, n = len(board), len(board[0])
        
        # build trie
        result = set()
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[ENDING] = word
        
        def dfs(r, c, curr_node):
            char = board[r][c]
            next_node = curr_node[char]
            if ENDING in next_node:
                result.add(next_node[ENDING])
            board[r][c] = MARKED

            for direction in DIRECTIONS:
                new_r = r + direction[0]
                new_c = c + direction[1]
                if new_r >= m or new_r < 0 or new_c >= n or new_c < 0:
                    continue
                if not board[new_r][new_c] in next_node:
                    continue 
                dfs(new_r, new_c, next_node)
            board[r][c] = char
        
        for r in range(m):
            for c in range(n):
                if board[r][c] in trie:
                    dfs(r, c, trie)
        return sorted(list(result))

class SolutionTest(unittest.TestCase):
    def testZeroWord(self):
        board = [["o","a","a","n"],["a","t","a","e"],["t","h","k","r"],["h","f","l","v"]]
        words = ["motherfucker"]
        s = Solution()
        result = s.findWords(board, words)
        self.assertEqual(result, []) 
        
    def testMultWord(self):
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        s = Solution()
        result = s.findWords(board, words)
        self.assertEqual(result, ["eat","oath"]) 
    
    def testRepeatWord(self):
        board = [["o","a","a","n"],["a","t","a","e"],["t","h","k","r"],["h","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        s = Solution()
        result = s.findWords(board, words)
        self.assertEqual(result, ["eat","oath"]) 

if __name__ == '__main__':
    unittest.main()




