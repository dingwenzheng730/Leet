'''
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 2
Output: 10

Input: [[1,5,9],[10,11,13],[12,13,15]], k= 9
Output: 15

Input: [[2]], k= 1
Output: 2

Precondition: 
n >= 1
k <= n*n
No int overflow 

C1: Single element
C2: k = n^2
C3: k <= n
C4: k > n

Algo: 
Brute force: get elements and sort O(n^2logn^2)

Heap: 
x = min(k, n)
Runtime: klogx
Space: O(x)

if n >= k:
compare the first column is enough

if n < k 
for each row, we have a pointer, use a heap to record the pointer value, 
for k times, pop out the smaller pointer and update that pointer to its next value in its list

Init a heap, the heap size should be min of k and n()
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        x = min(n, k)

        min_heap = []
        for r in range(x):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        while k:
            element, r, c = heapq.heappop(min_heap)
            if c < n-1:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))
            k -=1
        return element
        
