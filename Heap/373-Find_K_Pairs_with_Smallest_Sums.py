'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Input: nums1 = [1,2] nums =[1], k = 2
Output: [[1,1][1,2]]

Input: nums1 = [1,2,3], nums2 = [3,5,6], k =16
Output: [[1,3],[2,3],[1,5],[3,3],[1,6],[2,5],[2,6],[3,5],[3,6]]

Precondition:
len(nums1) = m 
len(nums2) = n

No int overflow
not valid k? possible

C1: General
C2: k > mn
C3: m != n
C4: m = n

Algo:
Brute Force: get mn pairs, sort, O(mn + mnlog(mn))

Get all pairs and use heap
Heap: O(klog(k)+mn)

Use heap when necessary:
Runtime: O(klogk)
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        heap = []
        heappush(heap,(0,0,0))
        seen = set()
        for _ in range(k):
            if heap:
                _ , ix1, ix2 = heappop(heap)
                result.append([nums1[ix1],nums2[ix2]])

                for new_ix1 , new_ix2 in [[ix1+1,ix2],[ix1,ix2+1]]:
                    if 0<=new_ix1 < len(nums1) and 0<=new_ix2<len(nums2) and not (new_ix1, new_ix2) in seen:
                        total_sum = nums1[new_ix1] + nums2[new_ix2]
                        heappush(heap,(total_sum,new_ix1,new_ix2) )
                        seen.add((new_ix1, new_ix2))
        return result
