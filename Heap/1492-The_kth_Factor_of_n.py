'''
Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

 

Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

Input: n = 12, k = 7
Output: -1

Input: n = 9, k = 3
Output: 9

Precondition:
n > 0
k > 0
no int overflow

Postcondition:
return int

C1: no k elements in factor list
C2: there is at least k in factor list
C3: perfect square

Algo:
First get the factor list, if the length is enough, stop
Brute Force: try from 1 to n O(n)
only iter through 1 to sqrt(n) use heap to keep always kth largest elements inside
Runtime: O(sqrt(n)logk)
Space: O(k)
'''
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # push into heap
        # by limiting size of heap to k
        def heappush_k(num):
            heappush(heap, - num)
            if len(heap) > k:
                heappop(heap)
            
        # Python heap is min heap 
        # -> to keep max element always on top,
        # one has to push negative values
        heap = []
        for x in range(1, int(n**0.5) + 1):
            if n % x == 0:
                heappush_k(x)
                if x != n // x:
                    heappush_k(n // x)
                
        return -heappop(heap) if k == len(heap) else -1