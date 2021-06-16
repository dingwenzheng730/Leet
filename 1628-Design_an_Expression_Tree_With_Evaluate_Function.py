'''
Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression.

Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. For example, the postfix tokens of the expression 4*(5-(7+2)) are represented in the array postfix = ["4","5","7","2","+","-","*"].

The class Node is an interface you should use to implement the binary expression tree. The returned tree will be tested using the evaluate function, which is supposed to evaluate the tree's value. You should not remove the Node class; however, you can modify it as you wish, and you can define other classes to implement it if needed.

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with two children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

It's guaranteed that no subtree will yield a value that exceeds 109 in absolute value, and all the operations are valid (i.e., no division by zero).

Follow up: Could you design the expression tree such that it is more modular? For example, is your design able to support additional operators without making changes to your existing evaluate implementation?

Precondition: always complete, at least 1 nodes, No x/0 will happen

Input: ['3']
Output: 3

Input: ['+', '*', '2', '5', '6', NULL, NULL]
Output: 32

C1: 1 element -> return that
'''

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self):
        if not self.right and self.left:
            return self.val
        if self.val == '+':
            return self.evaluate(self.left) + self.evaluate(self.right)
        if self.val == '-':
            return self.evaluate(self.left) - self.evaluate(self.right)
        if self.val == '*':
            return self.evaluate(self.left) * self.evaluate(self.right)
        if self.val == '/':
            return self.evaluate(self.left) // self.evaluate(self.right)


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for char in postfix:
            if char.isdigit():
                stack.append(TreeNode(int(char)))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(TreeNode(char, left, right))
        return stack[-1]
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        