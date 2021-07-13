'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Precondition:
n = len(s)
n >= 1
char in ASCII 
single char exceeds 100? Yes

Postcondition:
s should be modified 

C1: only 1
C2: with 1 and > 1
C3: with > 10

Algo:
two pointer, left points to the modified word, right points to the original word
use a count for each group, if it is 1, count just one, if it is 2-9, count two, if it is > 10, count 3
Runtime: O(n)
Space: O(1)
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        count = 1
        
        while right < len(chars):
            char = chars[right]
            count = 0
            while right < len(chars) and chars[right] == char:
                right += 1
                count += 1
            chars[left] = char
            left += 1
            if 1 < count < 10:
                chars[left] = str(count)
                left += 1
            elif count >= 10:
                for c in str(count):
                    chars.insert(left, c)
                    left += 1
                    right += 1
        return left

        