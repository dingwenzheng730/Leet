'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Input: nums = [3,2,2,2]
Output: 0

Input: nums = [1,2,1,3,1]
Output: 3


Precondition:
n = len(nums)
n >= 1
before 0 and after n-1 is -inf
no int overflow
nums[i] != nums[i+1] for all i

Postcondition:
nums stay unchanged
return >= 0 
return be any of the peak index

C1: 0 is peak
C2: n-1 is peak
C3: peak between
C4: mult peak

Algo:
Binary Search:

Runtime: O(logn)
Space: O(1)
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums) 
        left, right = 0, n - 1
        while left < right:
            middle = (right + left) // 2
            if nums[middle] > nums[middle+1]:
                right = middle
            else:
                left = middle + 1
        return left
