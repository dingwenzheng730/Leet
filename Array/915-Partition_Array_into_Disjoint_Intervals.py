'''
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Input: nums = [4, 6, 6, 6, 6]
Output: [4] [6, 6, 6, 6]

Precondition: len(nums) >= 2
always exist

C1: only 2 
C2: left only 1
C3: General

Brute force: O(n^2)
for each possible break point, check max of left and min of right

for each possible break point index i , get max(i) and min(i)(starting from tail) separately
the first i that can achieve max(i) <= min(i)
Runtime: O(n)
Space: O(n)
'''

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [None] * n
        right_min = [None] * n

        curr_max = nums[0]
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            left_max[i] = curr_max

        curr_min = nums[-1]
        for i in range(-2, 0, -1):
            curr_min = min(curr_min, right_min[i])
            right_min[i] = curr_min

        for i in range(1, n):
            if left_max[i-1] <= right_min[i]:
                return i