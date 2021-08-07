from collections import defaultdict
from collections import deque
import unittest
'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Preconditon:
length of word list: n
length of word: k
k >= 1
n >= 1
Only lowercase english word in both dict and word
may no valid transformation
all words are unique and in same length
begin != end

Postcondition:
no change for wordlist
return an int
if no valid, return 0

C1: No valid
C2: return 2
C3: return > 2

Algo:
BFS:
explore (word, depth) until word is what we want and return depth
build a dict from starword -> adjacent word
e.g. h*t: hit, hot 
for each word, transform it into starword, look up and exlopre all possible words
a seen set to avoid going back

Runtime: O(k^2*n)
Space: O(k^2*n)
'''

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        seen = set()
        mapping = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                star_word = word[:i] + '*' + word[i+1:] 
                mapping[star_word].append(word)
        queue = deque([(beginWord, 1)])
        while queue:
            word, depth = queue.popleft()
            if word == endWord:
                return depth
            seen.add(word)
            for i in range(len(word)):
                star_word = word[:i] + '*' + word[i+1:]
                for possible_word in mapping[star_word]:
                    if possible_word not in seen:
                        queue.append((possible_word,
                         depth+1))
        return 0

class SolutionTest(unittest.TestCase):
    def test_return_zero(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        s = Solution()
        result  = s.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 0)
    
    def test_return_one(self):
        beginWord = 'hit'
        endWord = 'hot'
        wordList = ['hot']
        s = Solution()
        result  = s.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 2)

    def test_return_more(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        s = Solution()
        result  = s.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
                
        