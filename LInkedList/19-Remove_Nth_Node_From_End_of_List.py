'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1,2,3], n =3
Output: [2,3]

Input: [1], n = 1
Output: []

Precondition:
length of head = m
m >= 1 
n <= m

Postcondition:
head changed

C1: m = n
C2: n < m
C3: only one element

Algo:
get the length of the linkedlist O(m)
go to the m-n node, remove it O(n)

One pass
two pointer, the gap remains n 
Runtime: O(m)
Space: O(1)

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        left, right = dummy, dummy
        dummy.next = head

        for _ in range(n+1):
            right = right.next

        while right:
            right = right.next
            left = left.next
        left.next = left.next.next

        return dummy.next
        