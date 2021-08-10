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
    OPERATIONS = {'Add': '+', 'Minus': '-', 'Multiply': '*', 'Divide': '/'}
    def calculate(self, s):
        stack = []
        curr_num = 0
        curr_operator = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            if s[i] in Solution.OPERATIONS.values() or i == len(s) - 1:
                if curr_operator == Solution.OPERATIONS['Add']:
                    stack.append(curr_num)
                elif curr_operator == Solution.OPERATIONS['Minus']:
                    stack.append(-1*curr_num)
                elif curr_operator == Solution.OPERATIONS['Multiply']:
                    working_num = stack.pop()
                    curr_num = working_num * curr_num
                    stack.append(curr_num)
                elif curr_operator == Solution.OPERATIONS['Divide']:
                    working_num = stack.pop()
                    curr_num = self.custom_divide(working_num, curr_num)
                    stack.append(curr_num)
                curr_operator = s[i]
                curr_num = 0

        return sum(stack)
    
    def custom_divide(self, num1, num2):
        if num1 >= 0:
            return num1 // num2
        else:
            return -1*(-1*num1 // num2)