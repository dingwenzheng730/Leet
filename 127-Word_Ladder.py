'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Precondition: len(s) >= 1
              len(wordlist) >= 1

C1: 0, if no exists
C2: return number in the shortest path
C3: Single word?
C4: endword not in list
Input: start='dog' end='gic' list= ['dig', 'gig', 'dgg', 'gic']
Output: 4

word -> rough word
dog -> _og, d_g, do_
{d_g: [dig, dgg]} 
mapping from rough word to all words
do BFS 
O(n)
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        worddict = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                rough_word = word[:i] + "_" + word[i+1:]
                worddict[rough_word].append(word)
        
        queue = deque([(beginWord, 1)])
        seen = set()

        while queue:
            curr_word, step = queue.popleft()
            seen.add(curr_word)
            for j in range(len(curr_word)):
                rough_word = curr_word[:j] + "_" + curr_word[j+1:]
                for next_word in worddict[rough_word]:
                    if next_word in seen:
                        continue
                    if next_word == endWord:
                        return step + 1
                    queue.append((next_word, step+1))
        return 0