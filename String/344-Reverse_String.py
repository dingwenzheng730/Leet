'''
Write a function that reverses a string. The input string is given as an array of characters s.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input:
Output:

Input:
Output:

Precondition: 
len(s) = n >= 1

C1: n = 1
C2: n is odd
C3: n is even

Algo:
two pointer, swap until meet
Runtime: O(n)
Space: O(1)
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
