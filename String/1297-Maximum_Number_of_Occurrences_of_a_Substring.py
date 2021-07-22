'''
Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.
 

Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3

Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0

Precondition:
0 <= minSize <= maxSize
len(s) >= 1
maxLetters >= 1
only ASCII words
no int overflow
len(s) = n

Postcondition:
s stay unchanged
return int

C1: n = 1
C2: n > 2
C3: maxSize = minSize
C4: minSize > n return 0

Algo:
Observation: We only care about the freq, not the substring,
so only care about minSize, do not care maxSize

Use hashmap:
for each index, try from minsize to maxsize, add qualified substring to the map
use set to check whether maxLetter condition is met 
return max of all values in the map
Runtime: O(n)
Space: O(n)
'''
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        mapping = defaultdict(int)
        for i in range(n-minSize+1):
            word = s[i:i+minSize]
            if len(set(w for w in word)) <= maxLetters:
                mapping[word] += 1
        return max(mapping.values()) if len(mapping.values()) > 0 else 0

