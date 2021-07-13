'''
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        int listLength = 0;
        ListNode currentNode = head;
        // find the length of linked list
        while (currentNode != null) {
            listLength++;
            currentNode = currentNode.next;
        }
        // set the front node at kth node
        ListNode frontNode = head;
        for (int i = 1; i < k; i++) {
            frontNode = frontNode.next;
        }
        //set the end node at (listLength - k)th node
        ListNode endNode = head;
        for (int i = 1; i <= listLength - k; i++) {
            endNode = endNode.next;
        }
        // swap the values of front node and end node
        int temp = frontNode.val;
        frontNode.val = endNode.val;
        endNode.val = temp;
        return head;
    }
}
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Input: [1], k = 1
Output: [1]

Input: [1,2,3], k = 2 
Output: [1,2,3]

Precondition:
len(head) = n
n >= 1
n >= k >= 1
Not int overflow

Postcondition:
return the head
modify the head in place

C1: n = k = 1
C2: n = k
C3: index of k from the begining = k from the end
C4: index of k from the begining > k from the end
C5: index of k from the begining < k from the end

Algo:
Two pointer:
find the length, O(n)
Determine left and right of reversing O(1)
Reverse a linkedlist O(n)

Runtime: O(n)
Space: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        ll_length = 0
        curr = head
        while curr:
            ll_length += 1
            curr = curr.next
        first = head
        second = head
        for _ in range(1, k):
            first = first.next
        for _ in range(1, ll_length-k+1):
            second = second.next
        first.val, second.val = second.val, first.val

        return head