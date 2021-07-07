'''
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Input: s = ['x']
Output: s = ['x']

Input: s = ["hi", "you", "guys"]
Output: s = ["guys", "you", "hi"]

Input: s = ['xman']
Output: s = ['xman']

Precondition:
len(s) >= 1
always one space
No extra spaces
s[i] is space or alphabet

C1: len(s) = 1
C2: only one word
C3: odd words
C4: even words

Algo:
n is total length of s
Reverse the whole s then reverse word
Runtime: O(n)
Space: O(1)
'''
class Solution:
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        
        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
                # reverse the word
            left = start
            right = end - 1
            while left < right:
                l[left], l[right] = l[right], l[left]
                left, right = left + 1, right - 1
            # move to the next word
            start = end + 1
            end += 1
            
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

        self.reverse_each_word(s)
