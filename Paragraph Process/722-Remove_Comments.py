'''
Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the ith line of the source code. This represents the result of splitting the original source code string by the newline character '\n'.

In C++, there are two types of comments, line comments, and block comments.

The string "//" denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored.
The string "/*" denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of "*/" should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string "/*/" does not yet end the block comment, as the ending would be overlapping the beginning.
The first effective comment takes precedence over others.

For example, if the string "//" occurs in a block comment, it is ignored.
Similarly, if the string "/*" occurs in a line or block comment, it is also ignored.
If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters.

For example, source = "string s = "/* Not a comment. */";" will not be a test case.
Also, nothing else such as defines or macros will interfere with the comments.

It is guaranteed that every open block comment will eventually be closed, so "/*" outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.


Precondition:
ASCII code
len(source) >= 1
len(source[i]) >= 0
no quote

n = total length of the graph
Runtime: O(n)
Space: O(n)
'''

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        program_string = '"'.join(source)
        result = []
        i = 0
        while i < len(program_string):
            if program_string[i] != '/' or i == len(program_string) - 1 or program_string[i + 1] not in '/*':
                result.append(program_string[i])
                i += 1
            elif program_string[i + 1] == '/':
                try:
                    i = program_string.index('"', i + 2)
                except ValueError:
                    break
            elif program_string[i + 1] == '*':
                try:
                    i = program_string.index('*/', i + 2) + 2
                except ValueError:
                    break
                    
        result = ''.join(result)
        return [s for s in result.split('"') if s]