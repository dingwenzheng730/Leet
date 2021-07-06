'''
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Input: s='abbccc' 
Output: 0

Input: s='a'
Output: 0

Precondition: 
len(s) >= 1

C1: len(s)=1 return 0
C2: return 0
C3: General Case, not returning 0

Algo:
Record freq in a dict O(n)
build set for freq of word O(n)
for seen freq, delete it until not seen (n^2)
'''
class Solution:
    def minDeletions(self, s: str) -> int:
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1
        
        seen = set()
        removed = 0
        for key, value in freq_map.items():
            if value not in seen:
                seen.add(value)
            else:
                while value > 0 and value in seen:
                    removed += 1
                    value -= 1
                seen.add(value)
        return removed
                


        