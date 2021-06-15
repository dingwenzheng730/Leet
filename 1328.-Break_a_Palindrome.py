'''
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

 Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

C1: empty not possible
C2: single word return ""
only lower engword? Y
'''

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        p_list = list(palindrome)
        is_odd_list = (len(p_list)%2 == 1)
        for i,e in enumerate(p_list):
            if e != 'a' and not(i == len(p_list)//2 and is_odd_list):
                p_list[i] = 'a'
                break
        else:
            p_list[-1] = 'b'
        return ''.join(p_list)
         