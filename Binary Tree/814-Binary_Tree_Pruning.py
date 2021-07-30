 '''
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Precondition:
n = number of nodes
n >= 0

Postcondition:
All nodes containing no 1 in subtree will be removed

C1: Empty
C2: One node 1
C3: One node 0
C4: leaf 0
C5: subtree 0

Algo:
Recursion:
for each node, check if right and left contains 1, if no, assign it to none
Runtime: O(n)
Space: O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def contain_one(node):
            if not node:
                return False
            left_contain_one = contain_one(node.left)
            right_contain_one = contain_one(node.right)
            if not left_contain_one:
                node.left = None
            if not right_contain_one:
                node.right = None
            return node.val or left_contain_one or right_contain_one
        if not contain_one(root):
            return None

        return root
            

        
        
