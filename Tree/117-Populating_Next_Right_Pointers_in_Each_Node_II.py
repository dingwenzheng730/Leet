'''
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Input: root = []
Output: []

Input: root = [1]
Output: [#]

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Precondition:
empty tree? Yes
Too much recursion? No
Int overflow? No
No extra space, recursion is ok

C1: no root
C2: one node
C3: Complete
C4: Not complete

Algo:
Since we add next node horizontally, so we can horizontally traverse the tree
Starting from each level left to right
set prev, leftmost to None at the begining for each level
when meeting first node in each level, set leftmost to that node
for each node, prev points to that node and update prev
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = self.process(curr.left, prev, leftmost)
                prev, leftmost = self.process(curr.right, prev, leftmost)
                curr = curr.next
        return root
    
    def process(self, node, prev, leftmost):
        if node:
            if prev:
                prev.next = node
            else:
                leftmost = node
            prev = node
        return prev, leftmost
        