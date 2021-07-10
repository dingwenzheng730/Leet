'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Input: nums = [10,9,2,5,3,7,101,18,19]
Output: 5
Explanation: The longest increasing subsequence is [2,3,7,18,19], therefore the length is 5.

Input:
Output:

Input:
Output:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

Precondition:
len(nums) = n
n >= 1
no int overflow

Postcondition:
nums unchange
return at least 1

C1: n = 1
C2: there is tie
C3: return 1

Algo:
Brute Force: for each element, we can choose to keep of delete it, O(2^n)

DP: 
Definition: dp[i] longest subsequence ending with index i 
Base Case: dp[0] = 1
RR: dp[i] = dp[j] + 1 for each j < i, if nums[j] > nums[i] 
result: max(dp)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)