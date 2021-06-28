'''
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".

Precondition: no repeat in given
              len(s) >= 1
              return any of the solution
C1: '?' only
C3: '????' All ?
C2: Combined Case
C4: more ? than possible words

TestCase:
'''
class Solution:
    MARK = '?'

    def __init__(self):
        self.pool = set(list(string.ascii_lowercase))

    def modifyString(self, s: str) -> str:
        s = list(s)
        
        for i in range(len(s)):
            if s[i] == Solution.MARK:
                self.pool -= set([s[i - 1] if i >= 1 else None, s[i + 1] if i <= len(s) - 2 else None])
                s[i] = self.pool.pop()
                if i >= 2:
                    self.pool.add(s[i-2])

        return ''.join(s)


