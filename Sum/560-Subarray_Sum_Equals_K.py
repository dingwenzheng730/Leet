'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1, 1, 2, 3, 5, 7], k = 5
Output: 2

Input: nums=[5], k=5
Output: 1

Input: nums=[3,5,3,4,-7], k=2
Output: 0

Precondition: 
len(nums) >= 1
len of subarray can be 1
can be negative or positive

C1: len(nums) = 1 and don't return 0
C2: return 0
C3: return >= 1
C4: contain element = k

Brute Force: O(n^2)
try each start and end

Two pointer: No solution

DP: Still O(n^2)

Hashmap: 
mapping contains all sum from index 0 to n
minus 2 elements in the mapping gets all possible sum for subarray
for each j, if sum - k in mapping and its the sum is i(can have more i), then subarray[i:j] is what we want

Runtime: O(n)
Space: O(n)
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, curr_sum = 0, 0
        mapping = defaultdict(int)
        mapping[0] = 1
        for i in range(len(nums)):
            curr_sum += nums[i]
            if mapping[curr_sum-k] != 0:
                count += mapping[curr_sum-k]
            mapping[curr_sum] += 1
        return count

