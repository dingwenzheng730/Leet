'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: [1], pos = 0
Output: True

Input: [1,2,35,6], pos=-1
Output: False

Precondition:
size of the linkedlist = n
pos 
n >= 1
no int overflow
length won't lead to out of memory

Postcondition:
List stay unchanged

C1: one single node with cycle
C2: one node without cycle
C2: return true
C3: return false

Algo: build a seen dict, traverse the ll, if node in seen, return true, if it hits null, return false
Runtime: O(n)
Space: O(n)

Two pointer:
fast pointer and slow pointer, if any hits none, return false
if they meets , return true
Runtime: O(n)
Space: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            else:
                seen.add(head)
            head = head.next
        return False
    '''
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True