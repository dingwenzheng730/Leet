'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Input: columnNumber = 28
Output: "AB"

Input: columnNumber = 701
Output: "ZY"

Input:
Output:

Input:
Output:

Precondition: 
Int overflow? No
n >= 1

C1: one char output
C2: Mult char output

Runtime: O(logn)
n is the number
Space: O(1)
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            result = chr(65+columnNumber%26) + result
            columnNumber //= 26
        return result
        
