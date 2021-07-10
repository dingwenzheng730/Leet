'''
Given a string s, return true if a permutation of the string could form a palindrome.

Input: s = "code"
Output: false

Input: s = 'bbfhf'
Output: True

Input: s = 'fdfd'
Output: True

Input: s = 'f'
Output: Ture

Precondition:
n = len(s)
n >= 1
Only lower case English words

Postcondition:
s stay unchanged

C1: n is odd
C2: n is even
C3: n = 1

Algo:
Go thourh the str, count number of each char, O(n)
for every even count, it is ok, for odd count, if at most 1 is found, still true

Runtime: O(n)
Space: O(n)
'''
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0
        n = len(s)
        count_map = collections.Counter(s)
        for value in count_map.values():
            count += value % 2

        return count <= 1 