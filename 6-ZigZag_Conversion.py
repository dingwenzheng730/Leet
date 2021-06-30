'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Precondition: len(s) >= 1 
              numRows >= 1

C1: numRows = 1  return s
C2: len(s) < k only have min(n, k) rows 
C3: General
len(s = n
numrows = k
Runtime: O(n)
space: O(n)
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        
        result = [[] for _ in range(min(numRows, len(s)))]
        curr_row = 0
        is_going_down = False
        
        for char in s:
            result[curr_row].append(char)
            if curr_row == 0 or curr_row == numRows - 1:
                is_going_down = not is_going_down
            curr_row = curr_row + 1 if is_going_down else curr_row -1

        for i in range(len(result)):
            result[i] = ''.join(result[i])
            
        return ''.join(result)