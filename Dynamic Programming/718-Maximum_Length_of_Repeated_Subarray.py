'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Input: num1 = [3], nums2 = [3]
Output: 1

Input: [1,2], [4,6]
Output: 0

Input: nums1 = [0,0,0,0], nums2 = [0,0,0,0,0]
Output: 4

Precondition:
len(nums1) = m
len(nums2) = n
m, n >= 1

C1: single elements in both, same
C2: single elements in both, not same
C3: 0 as a result
C4: result > 0
C5: result = len(min(m,n))

Algo:
Brute Force: O(mn*min(m,n))
For each element in nums1, try to find same element in nums2 O(mn)
if found, extend as long as possible
return the longest size

DP: 
dp[i][j]: common prefix length for nums1[i:] and nums2[j:]
dp[i][j] = dp[i+1][j+1] if nums1[i] = nums2[j]
dp[m][n] = 0
result: max of all possible i,j in dp[i][j]

Runtime: O(mn)
Space: O(mn)
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        return max(max(x) for x in dp)