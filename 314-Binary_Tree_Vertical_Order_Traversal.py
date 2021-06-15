# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                        
        return [columnTable[x] for x in sorted(columnTable.keys())]
'''

class Solution:
    '''
    C1: empty
    C2: 1 node only
    '''
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:

        mapping = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, index = queue.popleft()
            if not node is None:
                mapping[index].append(node.val)

                queue.append((node.left, index-1))
                queue.append((node.right, index+1))
        return [mapping[x] for x in sorted(mapping.keys())]

        