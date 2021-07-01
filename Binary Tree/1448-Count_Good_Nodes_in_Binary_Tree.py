'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Precondition: 
Always Complete? No
number of node >= 1

C1: one node 
C2: only one good node 
C3: mult good nodes
C4: layer >= 3

Input: [4]
Output: 1

Input: [4, 3, 6]
Output: 2

Input: [4, 8, 6]
Output: 3

Runtime: O(n)
Space:O(h) = O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def count_good(root, curr_max):
            if not root:
                return 0
            middle = 0
            left = count_good(root.left, max(curr_max, root.val))
            right = count_good(root.right, max(curr_max, root.val))
            
            if root.val >= curr_max:
                middle = 1
            return left + middle + right

        
        result = count_good(root, root.val)
        return result
        
        

        
