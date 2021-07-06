'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Input: root =[]
Output: []

Input: root = [1]
Output: [#]

Precondition:
Complete Binary Tree
empty tree? Yes
Too much recursion? No
Int overflow? No
No extra space, recursion is ok

C1: Empty Tree
C2: only root
C3: General Case

Algo:
for each level, starting from left to right
conduct i) left child point to right child
        ii) right point to next.left if it has next

Runtime: O(n)
Space: O(1)
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root