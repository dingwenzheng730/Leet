'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Precondition:
number of nodes for the tree: n
n >= 0
value sum no overflow, can only be int
targetSum no overflow int

Postcondition:
no change on tree
result list of list of int(value for node)
rersult can be empty

C1: n = 0
C2: n = 1
C3: result is []

Algo:
DFS: for each node, if if curr val = remain value and it is a left, append
if not, explore in left and right

Runtime: O(n^2)
for n/2 leaf, we have to copy curr path(with time n), so in total O(n^2) 
Space: O(n)

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(node, remain, curr_path, path_list):
            if not node: return 
            curr_path.append(node.val)
            if remain == node.val and not node.left and not node.right:
                path_list.append(list(curr_path))
            else:
                dfs(node.left, remain - node.val, curr_path, path_list)
                dfs(node.right, remain - node.val, curr_path, path_list)

            curr_path.pop()

        path_list = []
        dfs(root, targetSum, [], path_list)
        return path_list



        