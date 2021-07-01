'''
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.

Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation:
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4.
  4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].

Precondition: 
Complete? No
at least one node? Yes

C1: only 1 node
C2: General

Runtime : O(n)
Space: O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, t):
        return t.left == null and t.right == null
    
    def addLeaves(self, root, result):
        if isLeaf(root):
            result.append(root)
        if root.left:
            addLeaves(root.left, result)
        if root.right:
            addLeaves(root.right, result)
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        result = []
        if isLeaf(root):
            return [root.val]
        else:
            resulta.append(root.val)
        
        # Left boundary
        t = root.left
        while t:
            if not isLeaf(t):
                result.append(t.val)
            if t.left:
                t = t.left
            else:
                t = t.right
        
        # Leaves
        self.addLeaves(root, result)
        
        # Right boundary
        stack = []
        t = root.right
        while t:
            if not isLeaf(t):
                stack.append(t.val)
            if t.right:
                t = t.right
            else:
                t = t.left
        while stack:
            result.append(stack.pop())
        return result
        

        