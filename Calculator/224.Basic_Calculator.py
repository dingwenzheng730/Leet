'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Input: s = " 2-1 + 2 "
Output: 3

Input: s = '6+7*5-10'
Output: 31

Precondition: int() ? No
              decimal exists? No
              len(s) > 0
              s always valid 
              No * /
C1: Single value
C2: no bracket
C3: with bracket
C4: Mult bracket
C5: int > 10
C6: with negative input

add to res with sign before that char
meeting (, record curr sum, sign before ( and reset res to calculate inside ()
meeting ), use res to add up to total sum 

'''

class Solution:
    def calculate(self, s: str) -> int:
        mapping = {"1": 1, "2": 2, "3":3, "4":4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        stack = []
        working_num = 0
        res = 0
        sign = 1

        for char in s:
            if char.isdigit():
                working_num = 10 * working_num + mapping[char]
            elif char == '+':
                res += sign * working_num
                sign = 1
                working_num = 0
            elif char == '-':
                res += sign * working_num
                sign = -1
                working_num = 0
            elif char == '(':
                stack.append((res, sign))
                res = 0
                sign = 1
            elif char == ')':
                before_res, before_sign = stack.pop()
                res += sign * working_num
                res = before_sign * res
                res += before_res
                working_num = 0
        return res + sign * working_num

        