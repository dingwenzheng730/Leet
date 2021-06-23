'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ['fd', 'sdaf', '123ew']
Output: ''

Precondition: len(strs) >= 0  No guarantee there exists a common prefix

C1: len(strs) = 0
C2: No common prefix
C3: General

for each index, if anyone exceeds len or doesn't match or anyone, return 
Runtime: O(S) sum of all characters
Space: O(1)
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        return strs[0]


            