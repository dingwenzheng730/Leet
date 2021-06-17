'''
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Precondition: at least 1 word
              word[i] >= 0

Input: ['hello', 'world', 'helloworld']
Output: ['helloworld']

C1: no such => []
C2: can be divied, return all
C3: '' in the list
'''
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set()
        result = []
        words.sort(key=len)
        maxLen = 0
        for word in words:
            if self.WordBreak(word, wordset, maxLen):
                result.append(word)
            wordset.add(word) 
            maxLen = len(word)
        return result
        
    '''
    dp[i]: is word with length i breakable? starting from 0
    dp[i] = True if dp[j] and word[j:i] in worddict for some j in range 0 to i 
    '''

    def WordBreak(self, word, wordSet, maxLen):
        #if not word and not wordSet: return True 
        if not wordSet: return False  #[''] return False
        n = len(word)
        
        dp = [False] * (n + 1)
        dp[-1] = True 
        for start in range(n - 1, -1, -1):            
            for end in range(start, min(start + maxLen, n)):
                if dp[end + 1] and word[start: end + 1] in wordSet:
                    dp[start] = True
                    break
        return dp[0]