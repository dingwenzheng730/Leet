'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Input: s = "3+2*2"
Output: 7

Precondition:  len(s) >= 1
               int()? Yes
               Overflow? No
C1: Single Value
C2: with * /
C3: No * /

'''

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        operation_set = set(["+", "-", "*", "/"])
        stack = []
        curr_num = 0
        curr_op = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            if s[i] in operation_set or i == len(s)-1:
                if curr_op == '+':
                    stack.append(curr_num)
                elif curr_op == '-':
                    stack.append(-1*curr_num)
                elif curr_op == '*':
                    stack.append(stack.pop() * curr_num)
                elif curr_op == '/':
                    poped_val = stack.pop()
                    if poped_val >= 0:
                        stack.append(poped_val // curr_num)
                    else:
                        adjusted_num = (poped_val * (-1)) // curr_num
                        stack.append( -1 * adjusted_num )
                
                curr_num = 0
                curr_op = s[i]
                
        return sum(stack)