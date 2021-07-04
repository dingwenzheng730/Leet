'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"

Precondition: 
len(s) >= 1

C1: Single word => return 
C2: Involing mult spaces
C3: General

split and use reverse
Runtime: O(n)
Space: O(n)
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))