'''
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Input: s = '0000'
Output: 0

Input: s='100000'
Output: 1

Input: s='111110'
Output: 1

Precondition:
n = len(s)
n >= 1
only 0,1 in s

Postcondition:
return int: number of substr
''will not be counted

C1: return 0
C2: Left heavy
C3: Right heavy 

Algo:
Brute Force:
O(n^3)
try each start and end, and try from start to end
keep track of curr bit and its count, if meeting different and count remains, + 1 and switch curr bit
Two pointer:
use prev and curr to keep track of count of prev number and curr number, if end of str or pair not equal, add min of (prev, curr) to result
for each pair, compare whether they are equal, if equal, add to curr, else, switch prev count-> curr count, curr count -> 1 

Runtime: O(n)
Space: O(1)
'''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total_count, prev_count, curr_count = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                curr_count += 1
            else:
                total_count += min(prev_count, curr_count)
                prev_count = curr_count
                curr_count = 1
        return total_count + min(prev_count, curr_count)

