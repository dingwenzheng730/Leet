import collections
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    '''
        Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
        C1: k = 0 arr->unique in arr
        C2: len(arr) < k not possible
        C3: len(arr) = 0 not possible
        C4: len(arr) = k return 0
        Precondition: n >= k
        Brute Force: O(n^k)
        Greedy: always remove the number with least occurance O(nlogn) by sorting
                                                              O(nk)
        '''
        if k == len(arr):
            return 0 
        cnts = collections.Counter(arr)
        if k == 0:
            return len(cnts)
        heap = []
        for key,val in cnts.items():
            heapq.heappush(heap, (val, key))
        while heap and k > 0:
            if heap[0][0] <= k:
                val, key = heapq.heappop(heap)
                k -= val
            else:
                break
        return len(heap)






